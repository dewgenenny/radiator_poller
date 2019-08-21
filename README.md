Using EQ3 Max radiator thermostats with Home Assistant, one issue is that the actual temperatures only get updated when the valve moves or when you set a value. 

This is a short hacky attempt to force the radiators to update semi regularly. To note, there is a budget/duty cycle of communications allowed for communications to these thermostats, so a high update frequency won't be successful. I am using the script to poll hourly.
