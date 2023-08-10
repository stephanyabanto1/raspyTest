import RPi.GPIO as gpio
import time
import socketio


sio = socketio.Client()

gpio.setmode(gpio.BCM)

ENA = 27
IN1 = 17
IN2 = 4
ENB = 5
IN3 = 6
IN4 = 13


#ENA Right
gpio.setup(ENA, gpio.OUT) #enable input
gpio.setup(IN1, gpio.OUT)
gpio.setup(IN2, gpio.OUT)
#End of ENA 

#ENB
gpio.setup(ENB, gpio.OUT) #enable input
gpio.setup(IN3, gpio.OUT)
gpio.setup(IN4, gpio.OUT) #backward
#end of ENB





def forward():
    gpio.output(IN1,True )
    gpio.output(IN2, True)
    gpio.output(IN3,True)
    gpio.output(IN4,False)

def backward():
    gpio.output(IN1, False)
    gpio.output(IN2, True)


#wrong it is not turning on because of this
def turnOn():
    gpio.output(ENA,True)
    gpio.output(ENB, True)

def turnOff():
    gpio.output(ENA, False)
    gpio.output(ENB, False)

def turnRight():
    gpio.output(IN3, False)
    gpio.output(IN4, True)
    gpio.output(IN1, False) #back
    gpio.output(IN2, True) #forward

def turnLeft():
    gpio.output(IN3, True)
    gpio.output(IN4, False)
    gpio.output(IN1, True)
    gpio.output(IN2, False)


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