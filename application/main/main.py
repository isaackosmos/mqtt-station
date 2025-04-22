import time
from dotenv import load_dotenv
import os
from .mqtt_connection.mqtt_client_connection import MqttClientConnection

load_dotenv(dotenv_path="../configs/.env")


def start():
    mqtt_client_connection = MqttClientConnection(
        broker_ip=os.getenv("BROKER_IP", "localhost"),
        port=int(os.getenv("BROKER_PORT", 1882)),
        client_name=os.getenv("CLIENT_NAME", "mqtt_client_project"),
        keepalive=int(os.getenv("KEEPALIVE", 60))
    )
    mqtt_client_connection.start_connection()
    while True: time.sleep(0.001)