from waitress import serve
from flask import Flask
from datetime import datetime

import logging
import os
import re

app = Flask(__name__)

@app.route('/hostname')
def get_hostname():
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    hostname = str(os.environ.get('HOSTNAME'))
    return { "Hostname": hostname }

@app.route('/timestamp')
def get_date():
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return { "Timestamp": date_time_str }

@app.route('/')
def get_both():
    now = datetime.now()
    date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    hostname = str(os.environ.get('HOSTNAME'))
    return { "DateTimestamp": date_time_str, "Hostname": hostname }

if __name__ == "__main__":
    app.run(debug=True)