import paho.mqtt.publish as publish
 
MQTT_SERVER = "captain"
MQTT_PATH = "/home/chris/sensor1"
 
publish.single(MQTT_PATH, "Temp=42.88", hostname=MQTT_SERVER)