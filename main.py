from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()

in_progress_order = {}

@app.post('/')
async def handle_request(request: Request):
    
    #Retrieve json data
    payload = await request.json()

    #extract necessary info from payload
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    session_id = generic_helper.extract_session_id(output_contexts[0]['name'])

    intent_handler_dict = {
        "Track.Order - context : ongoing-tracking" : track_order,
        "Order.Add - context : ongoing-order" : add_to_order,
        "Order.Complete - context : ongoing-order" : complete_order,
        "Order.Remove - context : ongoing-order" : remove_from_order
    }

    return intent_handler_dict[intent](parameters , session_id)


def add_to_order(parameters:dict , session_id: str):
    
    food_items = parameters['food-item']
    quantities = parameters['number']

    if len(food_items) != len(quantities):
        fulfillment_text = f"Sorry , I didn't understand. Can you specify the food item and its quantity?"
    
    else:
        new_food_dict = dict(zip(food_items , quantities))

        if session_id in in_progress_order:
            current_food_dict = in_progress_order[session_id]
            current_food_dict.update(new_food_dict)
            in_progress_order[session_id] = current_food_dict
        else:
            in_progress_order[session_id] = new_food_dict   


        fulfillment_text = f"recieved food item {food_items} with quantity {quantities}"
    
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text 
    })    



def complete_order():
    pass

def remove_from_order():
    pass

    
def track_order(parameters: dict):

    order_id = int(parameters['number']) # in the json file of diagnostic info , the 'number' is under parameters in form of dict. See dialogflow_sample.py to see more
    order_status = db_helper.get_order_status(order_id)

    if order_status:
        fulfillment_text = f"The order status for order ID : {order_id} is {order_status}"
    else:
        fulfillment_text = f"Sorry, I couldn't find any information for order ID: {order_id}"

    return JSONResponse(content={
            "fulfillmentText": fulfillment_text 
    })