Using EQ3 Max radiator thermostats with Home Assistant, one issue is that the actual temperatures only get updated when the valve moves or when you set a value. 

This is a short hacky attempt to force the radiators to update semi regularly. To note, there is a budget/duty cycle of communications allowed for communications to these thermostats, so a high update frequency won't be successful. I am using the script to poll hourly.

You'll need to have a number of environmental variables set to make this work:

HA_TOKEN=<integration token from Home Assistant>

HA_URL=<URL of your Home Assistant instance>

RADIATOR_UPDATE_FREQUENCY=<update frequency in seconds>
  
HOMEGEAR_URL=<homegear URL>

MQTT_SERVER=<MQTT server hostname / IP>
MQTT_PORT=<MQTT Port>
MQTT_PASS=<MQTT Password>

MQTT_USER=<MQTT Username>
MQTT_TOPIC=<homegear topic eg homegear/1234-5678-9abc>

Run the script using 'python loop.py'

