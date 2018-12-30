
from kafka import KafkaConsumer, KafkaProducer
import time
import socket
import sys


def publish_message(producer_instance, topic_name, key, value):
    print ('publish message=' + value)
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer():
    _producer = None
    try:
        brokers = "captain:9092,godzilla:9092,oscar:9092,darwin:9092"
        _producer = KafkaProducer(bootstrap_servers=brokers, api_version=(0, 10))
        print("Got Producer")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


numParms = len(sys.argv)
for x in range(numParms):
    print("Next Parm=" + sys.argv[x])

host = socket.gethostname()
topic = sys.argv[1]
key = host
value = "Hello From Python on " + host   

print('Here we go====')
kafka_producer = connect_kafka_producer()
while True:
  publish_message(kafka_producer, topic, key, value)
  time.sleep(60)
