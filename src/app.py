#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bme280 as thermometer
import smbus2
from flask import Flask, jsonify

port = 0
address = 0x77
bus = smbus2.SMBus(port)

app = Flask(__name__)


@app.route("/")
def home():
    calibration_params = thermometer.load_calibration_params(bus, address)
    data = thermometer.sample(bus, address, calibration_params)
    return jsonify({'time': data.timestamp,
                    'humidity': data.humidity,
                    'temperature': data.temperature,
                    'pressure': data.pressure})


app.run(host= '192.168.88.122', port=9000, debug=False)
