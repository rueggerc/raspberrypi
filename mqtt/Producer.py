

from datetime import datetime
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import socket
import sys

def getReadings():
    timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    h,t = dht.read_retry(dht.DHT22,20)
    t = (t * 9/5) + 32
    # print('{0} {1:4.2f} {2:4.2f}'.format(timestamp,t,h))
    return (t, h)

def getMessage():
    host = socket.gethostname()
    temperature, humidity = getReadings()
    millis = int(round(time.time() * 1000))
    timestamp=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    msg = '{},{:#5.2f},{:#5.2f},{}'.format(host,temperature,humidity,millis,timestamp)
    return msg


def on_connect(client, userdata, flags, rc):
    print("Connect to Broker with resultCode=" + str(rc))
    client.subscribe("home/sensors/sensor3");

def on_message(client, userdata, msg):
    print("got Message")
    message = str(msg.payload)
    print(msg.topic+":" + message)

def on_publish(mosq,obj,mid):
    print("WE ARE Publishing")
    print("mid: " + str(mid))


def main():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)
    GPIO.output(40, GPIO.HIGH)    

    # MQTT
    client = mqtt.Client()
    client.connect("captain", 1883, 60)

    #client.on_connect = on_connect
    #client.on_message = on_message
    #client.loop_start()

    
    hostname = socket.gethostname()
    topic = "/home/sensors/" + hostname
    print ("topic={0}".format(topic));
    while True:
        msg = getMessage()
        print("msg = " + msg);
        client.publish("/home/sensors/sensor3", msg)
        time.sleep(5)
    
if __name__ == '__main__':
    main()
    
    

