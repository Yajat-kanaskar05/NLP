
# This is sample json diagnostic response from dialogflow
# Points to note ->
# 1. 'number' is inside parameters which is furthur inside queryResult.
# 2. To access order_id in main.py , we have to use 'number' 

'''
{
  "responseId": "a868ccce-6c63-41b4-a009-411aae4c3f51-1958ef91",
  "queryResult": {
    "queryText": "41",
    "parameters": {
      "number": 41
    },
    "allRequiredParamsPresent": true,
    "fulfillmentText": "The order status for order ID : 41 is in transit",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "The order status for order ID : 41 is in transit"
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": "projects/first-agent-opba/agent/sessions/674763d7-04d1-1b79-ce85-9ecb97ed8a55/contexts/ongoing-tracking",
        "lifespanCount": 5,
        "parameters": {
          "number": 41,
          "number.original": "41"
        }
      }
    ],
    "intent": {
      "name": "projects/first-agent-opba/agent/intents/74860e0f-441a-4c03-93f8-1e247d9958c3",
      "displayName": "Track.Order - context : ongoing-tracking"
    },
    "intentDetectionConfidence": 1,
    "diagnosticInfo": {
      "webhook_latency_ms": 597
    },
    "languageCode": "en"
  },
  "webhookStatus": {
    "message": "Webhook execution successful"
  }
}

'''