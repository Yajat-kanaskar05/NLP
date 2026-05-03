from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

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
        return JSONResponse(content={
            "fulfillmentText": f"Received intent: {intent}" 
        })

    # Fallback for unhandled intents
    return JSONResponse(content={
        "fulfillmentText": "I received your request but don't have a handler for it."
    })

    
        