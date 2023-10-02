#!/usr/bin/env python
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
# MQTT_USERNAME  = "MQTT_USERNAME"
# MQTT_PASSWORD  = "MQTT_PASSWORD"
# MQTT_CLIENT_ID = "MQTT_CLIENT_ID"

MQTT_USERNAME  = "49720c20-a3c1-11ed-b193-d9789b2af62b"
MQTT_PASSWORD  = "b7efd7c914d5a6dcb57336b30855e7236f0b7918"
MQTT_CLIENT_ID = "18acb550-a3c5-11ed-8d53-d7cd1025126a"


client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port loglevel=logging.INFO)
# For a secure connection use port 8883 when calling client.begin:
# client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883, loglevel=logging.INFO)

i=0
timestamp = 0

while True:
    client.loop()
    
    if (time.time() > timestamp + 10):
        client.celsiusWrite(1, i)
        client.luxWrite(2, i*10)
        client.hectoPascalWrite(3, i+800)
        timestamp = time.time()
        i = i+1
