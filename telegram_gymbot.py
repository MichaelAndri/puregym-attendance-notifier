import os, asyncio
from telegram import Bot
from telegram.error import BadRequest
from puregym_client import get_current_count

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_IDS       = []
THRESHOLD      = 200

bot = Bot(token=TELEGRAM_TOKEN)

def run():
    # pull creds from env or config
    email = os.getenv("PUREGYM_EMAIL")
    pin   = os.getenv("PUREGYM_PIN")
    count = get_current_count(email, pin)
    if count < THRESHOLD:
        asyncio.run(send_alert(count))

async def send_alert(count):
    text = f"🏋️‍♂️ There are {count} people in the gym."
    # gather lets us fire them off in parallel
    print(count)
    await asyncio.gather(*(bot.send_message(chat_id=cid, text=text) for cid in CHAT_IDS))
