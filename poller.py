import paho.mqtt.client as paho
import time
import datetime
import os
import json
from requests import get




url_homeassistant = os.environ['HA_URL']
url_homegear = os.environ['HOMEGEAR_URL']


homeassistant_token = os.environ['HA_TOKEN']
homeassistant_target_temperatures = {}
target_update_frequency = os.environ['RADIATOR_UPDATE_FREQUENCY']

_homeassistant_last_query_time = time.time()
_homegear_last_query_time = time.time()
_homeassistant_last_query = ""
_homegear_last_query = ""



ha_headers = {
    'Authorization':'Bearer ' + homeassistant_token,
    'content-type': 'application/json'}

headers_homegear = {
    'content-type': 'application/json'}



def get_climate_devices_from_home_assistant():

    id_list_from_home_assistant = {}
    x = get_json_from_home_assistant(url_homeassistant, ha_headers)
    for i in range(len(x)):
        entity_id = x[i]["entity_id"]
        if entity_id.startswith("climate"):
            print(entity_id + "(" + str(x[i]["attributes"]["id"]) + ")" )
            id_list_from_home_assistant[entity_id] = (x[i]["attributes"]["id"])
    return id_list_from_home_assistant


def get_target_temps_from_home_assistant():
    target_temperatures = {}
    x = get_json_from_home_assistant(url_homeassistant, ha_headers)
    for i in range(len(x)):
        entity_id = x[i]["entity_id"]
        if entity_id.startswith("climate"):
            #print(entity_id + "(" + str(x[i]["attributes"]["id"]) + ")" )
            target_temperatures[entity_id] = (x[i]["attributes"]["temperature"])
    return target_temperatures



def get_homegear_id_from_ha_id(ha_id):
    homegear_json = get_json_from_homegear(url_homegear, headers_homegear)
    for i in range(len(homegear_json["value"])):
        if homegear_json["value"][i]["ADDRESS"] == ha_id:
            print ("HA : " + ha_id + " HG : " + str(homegear_json["value"][i]["ID"]))
            return homegear_json["value"][i]["ID"]


def get_ha_id_from_ha_name(ha_name):
    x = get_json_from_home_assistant(url_homeassistant, ha_headers)
    for i in range(len(x)):
        entity_id = x[i]["entity_id"]
        if x[i]["entity_id"] == ha_name:
            print(entity_id + "(" + str(x[i]["attributes"]["id"]) + ")" )
            return (x[i]["attributes"]["id"])
    else:
        return "Not Found"

def get_homegear_id_from_ha_name(ha_name):
    return get_homegear_id_from_ha_id(get_ha_id_from_ha_name(ha_name))

def get_list_of_ids_to_poll_from_homegear():
    homegear_climate_devices = []
    homeassistant_climate_devices = get_climate_devices_from_home_assistant()
    print ("Getting list of ids to poll from homegear: ")

    for climate_device in homeassistant_climate_devices:
       # print ("homeassistant_climate_devices answered: "+ homeassistant_climate_devices[climate_device])
        #print ("get_homegear_id_from_ha_id()) answered: "+ str(get_homegear_id_from_ha_id(homeassistant_climate_devices[climate_device])))
        #print (homeassistant_climate_devices[climate_device])
        homegear_climate_devices.append(get_homegear_id_from_ha_id(homeassistant_climate_devices[climate_device]))
        #print ("appending: "+ str(get_homegear_id_from_ha_id(homeassistant_climate_devices[climate_device])))
    return homegear_climate_devices


def get_temperature_to_set(ha_id):
    print ("get temp to set is called")
    print (ha_id)
    ha_target_temps = get_target_temps_from_home_assistant()
    for key in ha_target_temps:
        if key == ha_id:
            return ha_target_temps[key]


def get_json_from_homegear(url, headers):
    # print ("Discovering devices from Homegear\n\n")
    global _homegear_last_query
    global _homegear_last_query_time

    response_homegear = get(url_homegear, headers=headers_homegear)
    homegear_json = json.loads(response_homegear.text)
    return homegear_json


def get_json_from_home_assistant(url, headers):

    global _homeassistant_last_query
    global _homeassistant_last_query_time
    if ((time.time() - _homeassistant_last_query_time) > 60) or _homeassistant_last_query == "":
        print("Fetching data from HA")
        print("_homeassistant_last_query_time = " + str(_homeassistant_last_query_time))
        response = get(url, headers=headers)
        x = json.loads(response.text)
        _homeassistant_last_query = x
        _homegear_last_query_time = time.time()
        return x
    else:
        print("Using cached data from HA")
        print("time.time - _homeassistant_last_query_time = " + str((time.time() - _homeassistant_last_query_time)) )
        print("_homeassistant_last_query_time = " + str(_homeassistant_last_query_time))

    return _homeassistant_last_query









