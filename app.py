# app.py

from flask import Flask, request, jsonify
import csv
import time

app = Flask(__name__)

server_version = 1.0

@app.post("/")
def log_traffic():
	ip = request.remote_addr
	time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	client_version = request.get_json()["client_version"]
	with open('log.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([time_stamp, ip, server_version, client_version])
	return "Logged traffic", 200

if __name__ == '__main__':
	app.run()
