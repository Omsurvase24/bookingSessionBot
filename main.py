from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    session_id = generic_helper.extract_session_id(output_contexts[0]['name'])

    if intent == "client.detail":
        name = parameters.get('person', {}).get('name')
        phone_number = parameters.get('phone-number')
        address = parameters.get('address')
        db_helper.insert_client_detail(name, phone_number, address)
        fulfillment_text = f'''Received {name}, {
            phone_number}, {address}. Please enter date when you want to book the session'''
    elif intent == "book.date":
        date = parameters.get('date-time')
        db_helper.insert_date(date)
        fulfillment_text = f'''Your booking has been done on {date}.'''

    return JSONResponse(content={"fulfillmentText": fulfillment_text})


# def book_session(parameters: dict, session_id):
#     phone_number = parameters.get('phone-number')
#     name = parameters.get('person', {}).get('name')
#     address = parameters.get('address')

#     details = {
#         "phone_number": phone_number,
#         "name": name,
#         "address": address
#     }

#     if name and phone_number and address:
#         fulfillment_text = f'''Received {name} and {
#             phone_number} and {address} in the backend'''

#     return JSONResponse(content={
#         "fulfillmentText": fulfillment_text
#     })


# def end_booking(parameters: dict, session_id):
#     date = parameters.get('date-time')

#     if date:
#         fulfillment_text = f'''Received {date}
#             in the backend for end booking'''
#     else:
#         fulfillment_text = "Missing date parameter for end booking."

#     return JSONResponse(content={"fulfillmentText": fulfillment_text})
