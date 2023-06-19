from datetime import datetime
import json


class MQTTMessage:
    @staticmethod
    def from_json(json_message):
        d = json.loads(json_message)
        m = MQTTMessage(d["data"], d["counter"], d["timestamp"])
        return m

    def __init__(self, data, counter=0, timestamp=None):
        if timestamp is not None:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.now()
        self.counter = counter
        self.data = data

    def __str__(self):
        return f"{self.timestamp} <{self.counter:04d}>: {self.data}"

    def to_json(self):
        return json.dumps(self.__dict__, default=str)
