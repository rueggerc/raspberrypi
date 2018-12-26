
from kafka import KafkaConsumer, KafkaProducer
import time

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
        _producer = KafkaProducer(bootstrap_servers=['hp1:9092'], api_version=(0, 10))
        print("Got Producer")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

topic = "foobar1"
key = 'sensor2'
value = "Hello From Python on Raspberry PI"   

print('Here we go====')
kafka_producer = connect_kafka_producer()
for x in range(10):
  publish_message(kafka_producer, topic, 'key', value)
  time.sleep(1)
