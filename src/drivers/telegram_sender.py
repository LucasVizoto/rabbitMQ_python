import requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()



token = getenv("BOT_TOKEN")
chat_id = getenv("CHAT_ID")
def send_telegram_message(message: str) -> None:

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    print(url)
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    try:
        response = requests.post(url= url, data = payload)
        response.raise_for_status()  # Lança uma exceção para códigos de erro HTTP (4xx ou 5xx)

        # Se a requisição foi bem-sucedida, você pode inspecionar a resposta
        print(f"Requisição bem-sucedida com status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")

