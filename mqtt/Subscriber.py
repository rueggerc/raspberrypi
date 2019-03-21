
import paho.mqtt.client as mqtt
 
MQTT_SERVER = "captain"
MQTT_PATH = "/home/chris/sensor1"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    
    print("message received=",str(message.payload.decode("utf-8")))
    payload = str(message.payload.decode("utf-8"))
    print("The message is {}".format(payload))
    
    # print("Got Message:" + str(msg.payload))
    # print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()