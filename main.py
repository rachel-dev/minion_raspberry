from flask import Flask
from flask import Flask, render_template, request
import time
import serial

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
ser.isOpen()

app = Flask(__name__)

@app.route("/")
def index():
#	return "Hello, Rachel"
	return render_template("robot.html")

@app.route('/left_side')
def left_side():
	data_1 = "LEFT"
	ser.write("l")
	response = ser.readline()
	print response
	return 'true'

@app.route('/right_side')
def right_side():
        data_1 = "RIGHT"
        ser.write("r")
        response = ser.readline()
        print response
        return 'true'


@app.route('/up_side')
def up_side():
        data_1 = "UP"
        ser.write("u")
        response = ser.readline()
        print response
        return 'true'


@app.route('/down_side')
def down_side():
        data_1 = "DOWN"
        ser.write("d")
        response = ser.readline()
        print response
        return 'true'

@app.route('/stop')
def stop():
        data_1 = "STOP"
        ser.write("s")
        response = ser.readline()
        print response
        return 'true'

if __name__ == '__main__' :
 	app.run(host='192.168.2.121',port=5000)
