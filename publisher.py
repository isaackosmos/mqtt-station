import paho.mqtt.client as mqtt
import random
import json
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

BROKER_PORT = os.getenv("BROKER_PORT", 1882)
BROKER_IP = os.getenv("BROKER_IP", "localhost")
TOPIC = os.getenv("TOPIC", "/messages")
soil_sensor = {
    "soil": {
        "temp": (15, 35),
        "moisture": (0, 100),
        "ph": (4.5, 8.5),
    },
}


def generate_sensor_data():
    sensor_data = {"timestamp": datetime.now().isoformat()}
    for param, (min_val, max_val) in soil_sensor['soil'].items():
        sensor_data[param] = round(random.uniform(min_val, max_val), 2)
    return sensor_data


def publish():
    mqtt_client = mqtt.Client(client_id='CLIENT_ID', callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.connect(host=BROKER_IP, port=BROKER_PORT)
    data = generate_sensor_data()
    payload = json.dumps(data)
    mqtt_client.publish(TOPIC, payload, qos=1)


if __name__ == "__main__":
    publish()
