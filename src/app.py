from flask import Flask
import smbus2
import bme280 as thermometer

port = 0
address = 0x77
bus = smbus2.SMBus(port)

calibration_params = thermometer.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object

app = Flask(__name__)


@app.route("/")
def home():
    data = thermometer.sample(bus, address, calibration_params)
    return data


app.run()