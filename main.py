import RPi.GPIO as gpio
import time
import socketio


sio = socketio.Client()

gpio.setmode(gpio.BCM)
gpio.setup(27, gpio.OUT)
gpio.setup(17, gpio.OUT)
gpio.setup(4, gpio.OUT)

def forward():
    gpio.output(17,True )
    gpio.output(4, False)

def backward():
    gpio.output(17, False)
    gpio.output(4, True)

def turnOn():
    gpio.output(27,True)

def turnOff():
    gpio.output(27, False)

@sio.event
def connect():
    turnOn()
    sio.emit("ID", 'steph-pi')
    print('connection established')

@sio.event
def movePi(direction):
    print('recieved direction:  ', direction)
    if(direction == 'forward'):
        forward()
    else:
        backward()

@sio.event 
def piTurnedOff():
    print("Turned Off")
    turnOff()

@sio.event
def piTurnedOn():
    print("Turned on")
    turnOn()

@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://192.168.2.15:3000')
sio.wait()