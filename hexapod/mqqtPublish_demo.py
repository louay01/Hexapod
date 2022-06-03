import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
from trial import *
import time
import threading
from ultrasonicFile import distance

delay = 0.4

TOPIC = "GraduationProject/Implementation/Louay&Doreid"


message = ""

dist = distance()

def do_something():
    while message == "b'forward'":
        print("f")
        dist = distance()
        if dist < 10:
            break    
        forward_walk()
        time.sleep(delay)

    while message == "b'back'":
        print("b")
        backward_walk()
        time.sleep(delay)

    while message == "b'right'":
        print("r")
        rotate(20, right=True, left=False)
        time.sleep(delay)

    while message == "b'left'":
        print("l")
        rotate_left()
        time.sleep(delay)

    while message == "b'pitch_down'":
        print("pD")
        pitch_down() 
        time.sleep(delay)

    while message == "b'pitch_up'":
        print("pU")
        pitch_up()
        time.sleep(delay)

    while message == "b'yaw_right'":
        print("yR")
        yaw_right()
        time.sleep(delay)

    while message == "b'yaw_left'":
        print("yL")
        yaw_left()
        time.sleep(delay)

    time.sleep(delay)
    standard_stance(Z)


#t = threading.Thread(target=do_something)
#t.start()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)


 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global message
    message = str(msg.payload)
    t = threading.Thread(target=do_something)
    t.start()
    print(msg.topic+" "+str(msg.payload))
    if str(msg.payload) == "b'Marhaba'":
        print(55)
        publish.single(TOPIC, "Marhaba_Back", hostname="test.mosquitto.org")

        
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org")
     

client.loop_forever()

checkMsg(message)