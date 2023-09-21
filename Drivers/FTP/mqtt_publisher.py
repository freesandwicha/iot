# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 14/9/2023 10:31 am

import time
from mqtt_client import MQTTClient

# Initialize the MQTTClient instance
mqtt_client = MQTTClient('f5b2a345ee944354b5bf1263284d879e.s1.eu.hivemq.cloud', 'redbackiotclient', 'IoTClient@123')

# Setup the client
mqtt_client.setup_mqtt_client()

try:
    is_running = True
    while is_running:
        topic = input("Please enter the topic you wish to publish to: ")
        mqtt_client.subscribe(topic)
        print("-" * 50)

        while True:
            message = input(f"Please enter the message payload you wish to send to {topic} (type 'changetopic' to switch topic or 'quit' to exit):  ")
            if message.lower() == 'quit':
                print("-" * 50)
                is_running = False
                break
            elif message.lower() == 'changetopic':
                topic = input("\nPlease enter the new topic you wish to publish to: ")
                mqtt_client.subscribe(topic)
                print("-" * 50)
                continue

            mqtt_client.publish(topic, message)
            print(f"\nPublished to {topic}: {message}")
            print("-" * 50)
finally:
    pass
