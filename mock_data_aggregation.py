import socket
from flask import Flask, request
from threading import Thread

app = Flask(__name__)
ip_addresses = {}
call_made = False


def aggregate_data():
    for i in range(10):
        ip_addresses[str(i) + "." + str(i) + "." + str(i) + "." + str(i)] = str(i)

@app.route('/aggregate')
def send_data():
    num_ips = int(request.args.get('num_ips'))
    sorted_ips = sorted(ip_addresses, key=ip_addresses.__getitem__, reverse=True)
    ips_to_be_sent = []
    for i in range(num_ips):
        ips_to_be_sent.append(sorted_ips[i])
    return str(ips_to_be_sent)

if __name__ == "__main__":
    data_aggregation_thread = Thread(target = aggregate_data)
    data_aggregation_thread.start()
    app.run(host="0.0.0.0", port=5000)