# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o8Qnh8vKV9a0T3DtUIKjIYDfEKOOxbn6
"""

#!/usr/bin/env python
 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

print GPIO.input(18)

print GPIO.input(23)

print GPIO.input(24)

print GPIO.input(25)