
import Adafruit_DHT as dht
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.HIGH)

while True:
  timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
  h,t = dht.read_retry(dht.DHT22,20)
  t = (t * 9/5) + 32
  print('{0} {1:4.2f} {2:4.2f}'.format(timestamp,t,h))
  time.sleep(5)





