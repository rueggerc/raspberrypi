
from kafka import KafkaProducer
from datetime import datetime
from sense_hat import SenseHat
import random
import time
import socket
import sys

def getReadings():
    sense = SenseHat()
    t = sense.get_temperature()
    h = sense.get_humidity()
    sense.show_message("READ");
    return (t, h)

def getMessage():
    host = socket.gethostname()
    #temp = 100*random.uniform(0.0,1.0)
    temperature, humidity = getReadings()
    #temperature = (9/5 * temperature)  + 32
    temperature = (9/5 * temperature)  - 2
    millis = int(round(time.time() * 1000))
    timestamp=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    msg = '{},{:#5.2f},{:#5.2f},{}'.format(host,temperature,humidity,millis,timestamp)
    print(msg)
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
        #brokers = "HP1:9092,godzilla:9092,oscar:9092,darwin:9092"
        brokers = "HP1:9092"
        _producer = KafkaProducer(bootstrap_servers=brokers, api_version=(0, 10))
        print("Got Producer")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer
    
def main():
    
    #GPIO.setwarnings(False)
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(40, GPIO.OUT)
    #GPIO.output(40, GPIO.HIGH)    
    
    key = socket.gethostname()
    topic = sys.argv[1]
    kafka_producer = connect_kafka_producer()
    while True:
        value = getMessage()
        publish_message(kafka_producer, topic, key, value)
        time.sleep(60)
    
if __name__ == '__main__':
    main()
    
    

