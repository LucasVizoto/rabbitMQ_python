import pika, json

from dotenv import load_dotenv
from os import getenv
load_dotenv()

class RabbitMQPublisher:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = "minha_exchange"
        self.__routing_key = ""
        self.__channel = self.create_chanel()
    
    def create_chanel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password= self.__password
            )
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        print(channel)
        return channel
    
rabbi_mq_publisher = RabbitMQPublisher()