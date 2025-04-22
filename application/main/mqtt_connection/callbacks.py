from dotenv import load_dotenv
import os

load_dotenv()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to MQTT broker. {client}")
        client.subscribe(os.getenv("TOPIC", "/messages"))
    else:
        print(f"Failed to connect to MQTT broker. Return code: {rc}")

def on_subscribe(client, userdata, mid, granted_qos):
    topic = os.getenv("TOPIC", "/messages")
    print(f"Subscribed to topic: {topic} with QoS: {granted_qos}")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} , from topic: {msg.topic}")