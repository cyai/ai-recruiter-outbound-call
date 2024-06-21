from twilio.rest import Client 
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


async def create_call():
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
    MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

    client = Client(account_sid=TWILIO_ACCOUNT_SID, password=TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        url=f"https://{os.getenv("SERVER")}/incoming",
        to=MY_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
    )

if __name__ == "__main__":
    asyncio.run(create_call())
