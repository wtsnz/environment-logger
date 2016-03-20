#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import signal
import time
import socket
import getopt
from Adafruit_BME280 import *

def main(argv):

    statsd_server = ""
    statsd_port = 0

    try:
        opts, args = getopt.getopt(argv, '', ['statsd-server=', 'statsd-port='])
    except getopt.GetoptError:
        print 'main.py -statsd-server <server> -statsd-port <port>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('--statsd-server'):
            statsd_server = arg
        elif opt in ('--statsd-port'):
            statsd_port = int(arg)

    # Read the Sensor data
    sensor = BME280(mode=BME280_OSAMPLE_8)

    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()

    degrees_string = '{0:0.3f}'.format(degrees)
    hectopascals_string = '{0:0.2f}'.format(hectopascals)
    humidity_string = '{0:0.2f}'.format(humidity)

    # Print the stats (useful for logging)
    # print 'Timestamp = {0:0.3f}'.format(sensor.t_fine)
    # print 'Temp      = {0:0.3f} deg C'.format(degrees)
    # print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
    # print 'Humidity  = {0:0.2f} %'.format(humidity)

    # Connect to the server and send the packet

    UDP_IP = statsd_server
    UDP_PORT = statsd_port

    try:
        sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        MESSAGE = "env.temperature:" + degrees_string + "|g"
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        MESSAGE = "env.pressure:" + hectopascals_string + "|g"
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        MESSAGE = "env.humidity:" + humidity_string + "|g"
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    except:
        print("Error sending data")

if __name__ == "__main__":
    try:
        while True:
            main(sys.argv[1:])
            time.sleep(5)
    except:
        print("There was an error ¯\_(ツ)_/¯")
