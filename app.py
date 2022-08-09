# app.py

from flask import Flask, request, jsonify
import csv
import time
import os.path

app = Flask(__name__)

server_version = 1.0
log_path = 'log.csv'

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
			]
		writer = csv.writer(f)

		# if log file does not exist, create it
		if not os.path.exists(log_path):
			writer.writerow([
				'datetime',
				'ip',
				'source_page',
				'server_version',
				'client_version'
				])
		writer.writerow([
			time_stamp,
			ip,
			source_page,
			server_version,
			client_version
			])
	return "Logged traffic", 200

if __name__ == '__main__':
	app.run()
