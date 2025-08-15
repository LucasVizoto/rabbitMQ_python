from requests import post, Response
from dotenv import load_dotenv
from os import getenv
load_dotenv()



def send_telegram_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    post(url, data = payload)

token = getenv("BOT_TOKEN")
chat_id = getenv("CHAT_ID")
message = "Olá Mundo !!"

send_telegram_message(token, chat_id, message)