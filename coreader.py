# -*- coding: utf-8 -*-
"""COReader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wY0RqOEV1dqnujDPTwfWhQ0yUtJ5-uKX
"""

import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS

from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0)

print(chan.value, chan.voltage)