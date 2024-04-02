from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']

    if intent == "client.detail":
        # return JSONResponse(content={
        #     "fulfillmentText": '''Received  =={intent}== in the backend'''
        # })
        return book_session(parameters)


def book_session(parameters: dict):
    pass
