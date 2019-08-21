import paho.mqtt.client as paho
import time
import datetime
import os


broker = "192.168.178.20"
port = 1883
mqtt_username = os.environ['MQTT_USER']
mqtt_password = os.environ['MQTT_PASS']


topic = "homegear/1234-5678-9abc"
addresses_to_poll = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

target_temperature = os.environ['RADIATOR_TARGET']
target_update_frequency = os.environ['RADIATOR_UPDATE_FREQUENCY']

delay_between_polls = target_update_frequency / len(addresses_to_poll)


def on_publish(client, userdata, result):             #create function for callback

    print("Successfully polled \n")
    pass


while 1:

    for radiator in addresses_to_poll:
        client1 = paho.Client("control1")                           #create client object
        client1.username_pw_set(username=mqtt_username, password=mqtt_password)
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker, port)                                 #establish connection
        now = datetime.datetime.now()
        temperature_to_set = target_temperature + ((now.hour % 2)*0.5)
        ret = client1.publish(topic+"/set/" + str(radiator) + "/1/SET_TEMPERATURE", temperature_to_set)                   #publish
        print("Polling radiator" + topic+"/set/" + str(radiator) + "/1/SET_TEMPERATURE polled")
        print(len(addresses_to_poll))
        time.sleep(delay_between_polls)



