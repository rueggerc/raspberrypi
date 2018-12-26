from sense_hat import SenseHat
import datetime
import time
import socket


def getData():

	now = datetime.datetime.now()
	id = (now.hour * 10000) + (now.minute * 100) + now.second
 	datakey = str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(id)
        sense = SenseHat()
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()
        print('')
	print('ID=' + str(id))
	print('datakey=' + datakey)
        print('Hostname=' + socket.gethostname())
        print('DateTime=' + datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))
        print('Temperature={0:0.2f} C'.format(t))
        print('Pressure={0:0.2f} Millibars'.format(p))
        print('Humidity={0:0.2f} %rH'.format(h))
        sense.show_message("Get Data")

getData()
