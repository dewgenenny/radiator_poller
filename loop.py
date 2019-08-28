import poller
import paho.mqtt.client as paho
import time
import datetime
import os



broker = os.environ['MQTT_SERVER']
port = os.environ['MQTT_PORT']
mqtt_username = os.environ['MQTT_USER']
mqtt_password = os.environ['MQTT_PASS']
mqtt_topic = "something/something"
# mqtt_topic = os.environ['MQTT_TOPIC']
target_update_frequency = os.environ['RADIATOR_UPDATE_FREQUENCY']


def on_publish(client, userdata, result):             #create function for callback

    print("Successfully polled:")
    pass

delay_between_polls = int(target_update_frequency) / len(poller.get_list_of_ids_to_poll_from_homegear())


while 1:
    devices_to_poll = poller.get_climate_devices_from_home_assistant()
    print ("polling: ")
    print (devices_to_poll)

    for radiator in devices_to_poll:

        print ("temp to set is: "+str(poller.get_temperature_to_set(radiator)))
        client1 = paho.Client("Radiator Poller")                           #create client object
        client1.username_pw_set(username=mqtt_username, password=mqtt_password)
        client1.on_publish = on_publish                          #assign function to callback
        client1.connect(broker, int(port))                                 #establish connection
        now = datetime.datetime.now()
        temperature_to_set = int(20) + ((now.hour % 2)*0.5)
        ret = client1.publish(mqtt_topic + "/set/" + str(poller.get_homegear_id_from_ha_name(radiator)) + "/1/SET_TEMPERATURE", temperature_to_set)                   #publish
        print(" radiator " + mqtt_topic + "/set/" + str(poller.get_homegear_id_from_ha_name(radiator)) + "/1/SET_TEMPERATURE with temperature set at: "+str(temperature_to_set))
        time.sleep(delay_between_polls)

