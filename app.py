# app.py

from flask import Flask, request
import csv
import time

app = Flask(__name__)

server_version = 1.0

@app.post("/")
def log_traffic():
	ip = request.remote_addr
	time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	with open('log_file.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow([time_stamp, ip, server_version])
	return "Logged traffic", 200

if __name__ == '__main__':
	app.run()
