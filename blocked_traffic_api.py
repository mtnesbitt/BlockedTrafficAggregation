import requests
import ast

class BlockedTrafficAPI:
    def get_addresses(self, num_ips):
            r = requests.get('http://10.230.1.59:5000/aggregate?num_ips=' + num_ips)
            list = ast.literal_eval(str(r.text))

            for a in list:
                print(a)

if __name__ == "__main__":
    bta = BlockedTrafficAPI()
    bta.get_addresses(10)