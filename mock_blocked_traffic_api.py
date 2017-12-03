import requests
import ast
import sys

class MockBlockedTrafficAPI:
    def __init__(self, num_ips):
        self.num_ips = num_ips

    def get_addresses(self):
            r = requests.get('http://localhost:5000/aggregate?num_ips=' + str(self.num_ips))
            list = ast.literal_eval(str(r.text))
            return list
