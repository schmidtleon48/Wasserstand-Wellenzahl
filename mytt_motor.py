#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

def on_message (client, userdata, msg):
        msg = client.subscribe('steuerung')
        print(msg.payload)
        if (str(msg.payload) == "b'links'") or (str(msg.payload) == "links"):
            motor1.links()
            print("Klick durch Steuerung")
            t = threading.Timer(3.0, motor1.stop())
            t.start()
            
        elif (str(msg.payload) == "b'rechts'") or (str(msg.payload) == "rechts"):
            motor1.rechts()
            print("Klick durch Steuerung")
            t = threading.Timer(3.0, motor1.stop())
            t.start()

        elif (str(msg.payload) == "b'stop'") or (str(msg.payload) == "stop"): 
            motor1.stop()
            print("Klick durch Steuerung")

class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(27,GPIO.OUT)
        GPIO.setup(17,GPIO.OUT)
        
    def links(self):
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(17,GPIO.LOW)
        print("Pumpen")
   
    def rechts(self):
        GPIO.output(27,GPIO.LOW)
        GPIO.output(17,GPIO.HIGH)
        print("Pumpen")
   
    def stop(self):
        GPIO.output(27,GPIO.LOW)
        GPIO.output(17,GPIO.LOW)
        print("Nicht Pumpen")

if __name__ == "__main__":
    client=mqtt.Client()
    client.connect("10.0.27.209", 1883, 60)
    motor1=Motor()
    motor1.stop()
    client.on_message = on_message
    client.loop_forever()