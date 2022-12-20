# app.py

import os.path
import time
import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

SERVER_VERSION = 1.0
LOG_PATH = 'log.csv'

@app.post("/")
def log_traffic():
    # define contents of log entry
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    client_version = request.get_json()["client_version"]
    source_page = request.get_json()["source_page"]

    # write log entry to log.csv
    with open(LOG_PATH, 'a') as f:
        writer = csv.writer(f)

        # if log file does not exist, create it and write column names
        if not os.path.exists(LOG_PATH):
            writer.writerow([
                'datetime',
                'source_page',
                'server_version',
                'client_version'
            ])

        # write data to log.csv
        writer.writerow([
            time_stamp,
            source_page,
            SERVER_VERSION,
            client_version
        ])
    return "Logged traffic", 200

if __name__ == '__main__':
    app.run()
