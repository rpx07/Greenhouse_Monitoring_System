# Greenhouse_Monitoring_System
Softwares and Libraries
1. Arduino IDE: Open and run the Adafruit_Publisher_Code in the Arduino IDE environment.
2. Install the libraries:
   <ESP8266WiFi.h>  /* WiFi library for ESP8266 */
   <WiFi.h>          /* WiFi library for ESP32 */
   <PubSubClient.h>  /* MQTT Messaging */
   <DHT.h>           /* DHT11 sensor library */
3. Connect to the local wifi network
   wifi_ssid "iPhone 15 Pro"
   wifi_password "12345qwerty"
4. Start the Mosquitto MQTT Broker in background.
5. Find the IP address for the connect network by writing the command in the Command Prompt: ipconfig
6. Add the credentials of IP in the Adafruit_Publisher_Code:
   mqtt_server "IP_address"
8. Run the program code
9. Now open Visual Studio Code Environment and open the mqtt.py file in it.
10. Install the following libraries:
    paho.mqtt.client: pip install paho-mqtt
    requests: pip install requests
    json: pip install json
11. Now configure ThingSpeak, start by visiting ThingSpeak.com.
12. Create a MathWorks account for free or sign in using an existing account.
13. Choose the ThingSpeak channel for your data stream; if new, create a channel by entering a name and description, add fields, and save.
14. Once created, obtain the Channel ID, Author name, access control type, and keys for your records.
15. Configure following:
    thingspeak_channel_id
    thingspeak_write_api_key
    thingspeak_update_url
16. Now run the mqtt.py file
