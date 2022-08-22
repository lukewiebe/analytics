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
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    client_version = request.get_json()["client_version"]
    source_page = request.get_json()["source_page"]

    # write log entry to log.csv
    with open('log.csv', 'a') as f:
        writer = csv.writer(f)

        # if log file does not exist, create it and write column names
        if not os.path.exists(log_path):
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
            server_version,
            client_version
        ])
    return "Logged traffic", 200

if __name__ == '__main__':
    app.run()
