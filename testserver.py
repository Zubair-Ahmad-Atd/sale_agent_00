# from fastapi import FastAPI 
# from fastapi import FastAPI, Request
# from twilio.twiml.voice_response import VoiceResponse
# from dotenv import load_dotenv

# load_dotenv()

# app = FastAPI()


# bravo = FastAPI()

# @bravo.get("/")
# def get_bravo():
#     return { 
#         "message": "Fast api is a framework to build a server whereas server needs a server engine which is a uvicorn"
#     } 
# @bravo.get("/{name}")
# def get_name(name:str):
#     return { 
#          f"hello Mr.{name}, How are you"
#     } 

# from fastapi import FastAPI, Response
# from twilio.twiml.voice_response import VoiceResponse

# app = FastAPI()

# @app.get("/voice")
# def voice_webhook():
#     # 1. Create a TwiML response object
#     vr = VoiceResponse()
#     vr.say("Hello! Your FastAPI server is now returning TwiML instead of JSON.")
    
#     # 2. Return it as a string with the correct Media Type
#     return Response(content=str(vr), media_type="application/xml")

# @app.api_route("/voice", methods=["GET", "POST"])
# def voice_webhook():
#     twiml_content = """<?xml version="1.0" encoding="UTF-8"?>
#     <Response>
#         <Say>voice is running and returning XML</Say>
#     </Response>"""
    
#     return Response(content=twiml_content, media_type="application/xml")
# @app.post("/process")
# def process_webhook():
#     return{ 
#         "status":"Post is running"
#     }
    # response = VoiceResponse()

    # response.say(
    #     "Hello! This is an AI assistant calling you. How can I help you today?",
    #     voice="alice"
    # )

    # return str(response) 

from fastapi import FastAPI
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI(redirect_slashes=False)

@app.api_route("/voice", methods=["GET", "POST"])
async def voice():
    vr = VoiceResponse()
    vr.say("Hello Zubair, Twilio is connected successfully.")
    return Response(content=str(vr), media_type="application/xml")
