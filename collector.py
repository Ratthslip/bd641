#!/usr/bin/python

import sys
import os
import decimal
import dht11
import datetime
from time import gmtime, strftime
import RPi.GPIO as GPIO

class SmartHome:

    def __init__(self):
        self.humidity = None
        self.temperature = None
        self.light = None


    def get_DHT11(self):
        instance = dht11.DHT11(pin=12)
        try:
            result = instance.read()
            if result.humidity is not None:
                self.humidity = "{0:0.1f}".format(result.humidity)
            if result.temperature is not None:
                self.temperature = "{0:0.1f}".format(result.temperature)
        except:
            pass
        return self.humidity, self.temperature

    def get_Light(self):
        try:
            self.light  = On
        except:
            pass

        return self.light

if __name__ == "__main__":
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    myhome = SmartHome()
    h, t = myhome.get_DHT11()
    l = myhome.get_Light()


    print("{0},{1},{2},{3}".format(strftime('%Y-%m-%d %H:%M:%S', gmtime()), h, t, l))

    GPIO.cleanup()
