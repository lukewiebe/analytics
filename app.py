# app.py

from flask import Flask, request
import time

app = Flask(__name__)

# establish variables here

@app.post("/")
def log_traffic():
	print(request.remote_addr)
	time_stamp = time.strftime("%H:%M:%S", time.localtime())
	print(time_stamp)
	return "Logged traffic", 200

if __name__ == '__main__':
	app.run()
