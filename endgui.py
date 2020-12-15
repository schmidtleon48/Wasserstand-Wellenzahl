#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
import paho.mqtt.client as  mqtt
import paho.mqtt.subscribe as subscribe

'''
Momentan publisht es nur Befehle. Für die Anzeige des Fülstandes machen Sie die Comments raus und geben Sie die richtige IP in den
früheren Comments ein
'''

client=mqtt.Client()
client.connect("10.0.27.209",1883,60)

def publ():
    client.publish('steuerung', "links", qos=0, retain=False)
    print("Client publisht!")

def pubs():
    client.publish('steuerung', "stop", qos=0, retain=False)
    print("Client publisht!")

def pubr():
    client.publish('steuerung', "rechts", qos=0, retain=False)
    print("Client publisht!")

#msgl = subscribe.simple("datenl", hostname="10.0.27.119:1883")
#msgr = subscribe.simple("datenr", hostname="10.0.27.119:1883")

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)

root.title("Wellenzahl")

label= Label(frame1,text="Wellenzahl - Füllstandsmessung",justify=LEFT)
label.pack(side=LEFT)

hi_there = Button(frame2,text="nach links",command=publ)
hi_there.pack(side=LEFT)

hi_there1 = Button(frame2,text="stop",command=pubs)
hi_there1.pack(side=RIGHT)

hi_there2 = Button(frame2,text="nach rechts",command=pubr)
hi_there2.pack()

'''
bar1 = Progressbar(frame3, length=400)
bar1['value'] = 70 #msgl.payload
bar1.pack()

bar2 = Progressbar(frame3, length=400)
bar2['value'] = 20 #msgr.payload
bar2.pack()
'''

frame1.pack(padx=1,pady=1)
frame2.pack(padx=10,pady=10)
frame3.pack(padx=20,pady=20)

root.mainloop()