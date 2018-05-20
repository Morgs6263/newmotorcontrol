# -*- coding: utf-8 -*-
"""
Created on Sun May 20 12:01:23 2018

@author: morga
"""

import time
import RPi.GPIO as GPIO
import sys, tty,  termios, time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# import each pin that the motors and the driver
# is connected to
# Motor 1
Motor1A = 16
Motor1B = 18
Motor1E = 22

# Motor 2
Motor2A = 11
Motor2B = 13
Motor2E = 15

# Initialise the GPIO Pins
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

print('w forward')
print('s reverse')
print('a left')
print('d right ')
print('q stop')
print('e exit program')

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN, old_settings)
    return ch

# get the brobot to move forward
def forward():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)

# get the brobot to move backwards
def reverse():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
 
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    
# so for left and right I currently have
# 1 motor going forward and the other going 
# backward, however this can be changed 
def left():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def right():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def stop():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)


while True:
    char = getch()
    if(char == "w"):
        forward()
    if(char == "s"):
        reverse()
    if(char == "a"):
        left()
    if(char == "d"):
        right()
    if(char == "q"):
        stop()
    if(char == "e"):
        quit()
    
    
    
    
    
    
    
    
    