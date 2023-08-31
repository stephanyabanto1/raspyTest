import RPi.GPIO as gpio
import time
import socketio
import atexit

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


def LED1On():
    gpio.output(LED1, True)


def LED1OFF():
    gpio.output(LED1, False)

def TurnOnAll():
    gpio.output(LED1, True)
    gpio.output(LED2, True)
    gpio.output(LED3, True)
    gpio.output(LED4, True)
    gpio.output(LED5, True)
    gpio.output(LED6, True)


def TurnOfAll():
    gpio.output(LED1, False)
    gpio.output(LED2, False)
    gpio.output(LED3, False)
    gpio.output(LED4, False)
    gpio.output(LED5, False)
    gpio.output(LED6, False)


    #button to turn them all on 
    #button to turn each of four on 



#wrong it is not turning on because of this


state = {
    'up': False,
    'down': False,
    'left': False,
    'right': False
}


@sio.event
def connect():
    sio.emit("ID", 'steph-pi')
    print('connection established')
    

@sio.event
def robot_instructions(instructions):
    # state['up'] = instructions['up']
    print(instructions)
    

@sio.event
def disconnect():
    print('disconnected from server')


def exit_handler():
    gpio.cleanup()
    print('cleaned pins')

atexit.register(exit_handler)

sio.connect('http://192.168.2.11:3000')

sio.wait()
