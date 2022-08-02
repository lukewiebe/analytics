# app.py

from flask import Flask, request, jsonify
import csv
import time

app = Flask(__name__)

server_version = 1.0

@app.post("/")
def log_traffic():
	# define contents of log entry
	ip = request.remote_addr
	time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	client_version = request.get_json()["client_version"]
	source_page = request.get_json()["source_page"]
	# write log entry to log.csv
	with open('log.csv', 'a') as f:
		fieldnames = [
			'datetime',
			'ip',
			'source_page',
			'server_version',
			'client_version'
			]
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writerow({
			'datetime': time_stamp,
			'ip': ip,
			'source_page': source_page,
			'server_version': server_version,
			'client_version': client_version
			})
	return "Logged traffic", 200

if __name__ == '__main__':
	app.run()
