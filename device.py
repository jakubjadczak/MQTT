from utils import get_topics, get_config
import paho.mqtt.client as mqtt
from datetime import datetime
import random
import time
import sys

class Device:
    def __init__(self, component: str):
        self.counters = {}
        self.component = component
        self.topics = get_topics(self.component)
        self.frequency = float(get_config(component, 'frequency'))
        self.port = int(get_config(component, 'port'))
        self.ip = get_config(component, 'ip')

        self.client = mqtt.Client()
        if self.client.connect('127.0.0.1', 1883, 60) != 0:
            raise Exception("Could not connect to MQTT broker")
        
        self.set_counters()
        self.publish()
        
    def __del__(self):
        self.client.disconnect()

    def set_counters(self):
        topics = list(self.topics.keys())
        for t in topics:
            self.counters[t] = 0

    def publish(self):
        while True:
            for topic, value in self.topics.items():
                self.client.publish(topic, f'{self.generate_data(value)}, {self.counters[topic]}, {datetime.now()}')
                self.counters[topic] += 1
            time.sleep(self.frequency)

    @staticmethod
    def generate_data(data_type: str):
        if data_type.startswith('int'):
            if data_type.endswith(']'):
                random_range = data_type.split('[')[1].split(']')[0]
                random_range = random_range.split(':')
                return random.randint(int(random_range[0]), int(random_range[1]))
            else:
                return random.randint(0, 100)
        elif data_type.startswith('float'):
            if data_type.endswith(']'):
                random_range = data_type.split('[')[1].split(']')[0]
                random_range = random_range.split(':')
                return random.uniform(int(random_range[0]), int(random_range[1]))
            else:
                return random.uniform(0, 100)


if __name__ == '__main__':
    argv = sys.argv
    d = Device(argv[1])