
from kafka import KafkaProducer
from datetime import datetime
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import random
import time
import socket
import sys

def getTemperature():
    timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    h,t = dht.read_retry(dht.DHT22,20)
    t = (t * 9/5) + 32
    print('{0} {1:4.2f} {2:4.2f}'.format(timestamp,t,h))
    return t; 

def getMessage():
    host = socket.gethostname()
    #temp = 100*random.uniform(0.0,1.0)
    temp = getTemperature()
    millis = int(round(time.time() * 1000))
    timestamp=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    msg = '{},{:#5.2f},{},{}'.format(host,temp,millis,timestamp)
    return msg

def publish_message(producer_instance, topic_name, key, value):
    #print ('message=' + value)
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        #print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        # brokers = "captain:9092,godzilla:9092,oscar:9092,darwin:9092"
        brokers = "HP1:9092,godzilla:9092,oscar:9092,darwin:9092"
        _producer = KafkaProducer(bootstrap_servers=brokers, api_version=(0, 10))
        print("Got Producer")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer
    
def main():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)
    GPIO.output(40, GPIO.HIGH)    
    
    key = socket.gethostname()
    topic = sys.argv[1]
    kafka_producer = connect_kafka_producer()
    while True:
        value = getMessage()
        publish_message(kafka_producer, topic, key, value)
        time.sleep(60)
    
if __name__ == '__main__':
    main()
    
    

