import RPi.GPIO as gpio
import time
import socketio


sio = socketio.Client()

gpio.setmode(gpio.BCM)

#First label 

LED1 = 18
LED2 = 23
LED3 = 24
LED4 = 25
LED5 = 8
LED6 = 7

#set up

gpio.setup(LED1, gpio.OUT)
gpio.setup(LED2, gpio.OUT)
gpio.setup(LED3, gpio.OUT)
gpio.setup(LED4, gpio.OUT)
gpio.setup(LED5, gpio.OUT)
gpio.setup(LED6, gpio.OUT)


def FirstLed():
    gpio.output(LED1, True)









#wrong it is not turning on because of this



@sio.event
def connect():
    sio.emit("ID", 'steph-pi')
    print('connection established')
    

@sio.event
def movePi(direction):
    print('recieved direction:  ', direction)
    

@sio.event
def goForward():
    FirstLed()
    print("Go Forward")
    
    

@sio.event 
def piTurnedOff():
    print("Turned Off")
   

@sio.event
def piTurnedOn():
    print("Turned on")
    

@sio.event
def piTurnedRight():
    print("Turned Right")
   

@sio.event
def piTurnedLeft():
    print("Turned left")
   

@sio.event
def goBackward():
    print("Went Backward")
   




@sio.event
def disconnect():
    print('disconnected from server')





sio.connect('http://192.168.2.18:3000')
sio.wait()