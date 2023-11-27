import paho.mqtt.client as mqtt
import requests
import json

# MQTT Broker Configuration
mqtt_broker = "192.168.161.124"
mqtt_port = 1883
humidity = "1"
tcelsius = "2"
tfahrenheit = "sensor/DHT11/temperature_fahrenheit"

# ThingSpeak Configuration
thingspeak_channel_id = "2354792"
thingspeak_write_api_key = "4L6W9ZC9LBS7SGXK"
thingspeak_update_url = f"https://api.thingspeak.com/update?api_key={thingspeak_write_api_key}"

# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    # Subscribe to MQTT topics
    client.subscribe(humidity)
    client.subscribe(tcelsius)
    client.subscribe(tfahrenheit)

# Callback when MQTT message is received
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    print(f"Received message from topic: {topic}, payload: {payload}")


    # Extract sensor data and update ThingSpeak
    if topic == humidity:
        print("Updating ThingSpeak field3 with payload: {}".format(payload))
        update_thingspeak({"field3": payload})
    elif topic == tcelsius:
        print("Updating ThingSpeak field1 with payload: {}".format(payload))
        update_thingspeak({"field1": payload})
    elif topic == tfahrenheit:
        print("Updating ThingSpeak field2 with payload: {}".format(payload))
        update_thingspeak({"field2": payload})

# Function to update ThingSpeak with sensor data
def update_thingspeak(data):
    try:
        response = requests.post(thingspeak_update_url, data)
        print(f"ThingSpeak update status: {response.status_code}")
    except Exception as e:
        print(f"Error updating ThingSpeak: {e}")

# Create MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
client.connect(mqtt_broker, mqtt_port, 60)

# Loop to handle MQTT events
client.loop_start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting script")
    client.disconnect()