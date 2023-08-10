import RPi.GPIO as gpio
import time
import socketio


sio = socketio.Client()

gpio.setmode(gpio.BCM)

#ENA Right
gpio.setup(27, gpio.OUT) #enable input
gpio.setup(17, gpio.OUT)
gpio.setup(4, gpio.OUT)
#End of ENA 

#ENB
gpio.setup(5, gpio.OUT) #enable input
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT) #backward
#end of ENB



def forward():
    gpio.output(17,True )
    gpio.output(4, False)
    gpio.output(6,True)
    gpio.output(13,False)

def backward():
    gpio.output(17, False)
    gpio.output(4, True)

def turnOn():
    gpio.output(27,False)
    gpio.output(5, True)

def turnOff():
    gpio.output(27, False)
    gpio.output(5, False)

def turnRight():
    gpio.output(6, True)
    gpio.output(13, False)
    gpio.output(17, False) #back
    gpio.output(4, True) #forward

def turnLeft():
    gpio.output(6, False)
    gpio.output(13, True)
    gpio.output(17, True)
    gpio.output(4, False)


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
def piTurnedRight():
    print("Turned Right")
    turnRight()

@sio.event
def piTurnedLeft():
    print("Turned left")
    turnLeft()

@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://192.168.2.15:3000')
sio.wait()