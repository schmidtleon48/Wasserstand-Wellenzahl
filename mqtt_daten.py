#!/usr/bin/python3

'''
Dies ist nur ein Prototyp. Dieses Skript soll die Füllhöhe berechnen und dann in Prozent an "datenl" und "datenr" die jeweilige Füllhöhe 
in Prozent publishen.
'''

import paho.mqtt.client as mqtt
import wellenzahl

class Node:
    def __init__(self):
        client=mqtt.Client()
        client.connect(10.0.27.209, 1883, 60)
    
    def publishl(daten):
        client.publish('datenl', daten, qos=0, retain=False)

    def publishr(daten):
        client.publish('datenr', daten, qos=0, retain=False)

if __name__ == "__main__":
    node1=Node()
    node1.publishl(wellenzahl.Füllhöhe)