from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()

@app.post('/')
async def handle_request(request: Request):
    
    #Retrieve json data
    payload = await request.json()

    #extract necessary info from payload
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "Track.Order - context : ongoing-tracking":

        return track_order(parameters)

        

    # Fallback for unhandled intents
    return JSONResponse(content={
        "fulfillmentText": "I received your request but don't have a handler for it."
    })

    
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