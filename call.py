from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

call = client.calls.create(
    to="+923343543723",          # customer number
    from_=os.getenv("TWILIO_PHONE_NUMBER"),
    url = "https://small-beds-mate.loca.lt/voice"
    # url = "https://burl-beefiest-uncontestedly.ngrok-free.dev/voice" #NGROK URL
    # url = "https://handler.twilio.com/twiml/EHaca37f80fc5ad9cc9c7f6e702f2941df" Twilio Bin URL
    # url = "https://burl-beefiest-uncontestedly.ngrok-free.dev/voice" # NGROK
    # url = "https://gprze-154-91-163-118.a.free.pinggy.link/voice"   # piggy 
    # url = "https://tthf81qr-8000.euw.devtunnels.ms/voice"  # VS code tunnel forwarding url
    #   url = "https://burl-beefiest-uncontestedly.ngrok-free.dev/voice" #ngrok new tunnel
    # url = "https://presenting-transparent-characterization-basics.trycloudflare.com/voice"

    # url = "https://rokox-154-198-118-95.a.free.pinggy.link/voice"
    # url = "http://demo.twilio.com/docs/voice.xml" twilio demo url
      
)

print("Call SID:", call.sid)
