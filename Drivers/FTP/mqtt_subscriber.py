# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 14/9/2023 10:31 am
import threading
from mqtt_client import MQTTClient

def user_commands(mqtt_client):
    global topic_to_subscribe
    while True:
        command = input("\nType 'changetopic' to switch subscription topic or 'quit' to exit: ")

        if command.lower() == 'quit':
            mqtt_client.get_client().loop_stop()  # Stop the background loop
            mqtt_client.get_client().disconnect()
            exit()
        elif command.lower() == 'changetopic':
            new_topic = input("\nPlease enter the new topic you wish to subscribe to: ")
            mqtt_client.unsubscribe(topic_to_subscribe)
            mqtt_client.subscribe(new_topic)
            topic_to_subscribe = new_topic

# Initialize the MQTTClient instance
mqtt_client = MQTTClient('f5b2a345ee944354b5bf1263284d879e.s1.eu.hivemq.cloud', 'redbackiotclient', 'IoTClient@123')

# Setup the client
mqtt_client.setup_mqtt_client()

topic_to_subscribe = input("Enter the topic you wish to subscribe to: ")
mqtt_client.subscribe(topic_to_subscribe)
print("-" * 50)

# Start a separate thread to handle user commands
threading.Thread(target=user_commands, args=(mqtt_client,)).start()

try:
    mqtt_client.loop_forever()
except KeyboardInterrupt:
    print("\nSubscriber terminated.")
finally:
    mqtt_client.get_client().disconnect()
