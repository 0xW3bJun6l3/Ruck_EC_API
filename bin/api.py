from email import message
from ipaddress import ip_address
from flask import Flask, jsonify, request
from datetime import datetime
from airCtrl import PWMCtrl


app = Flask(__name__)
AirController = PWMCtrl(1000,18,5)
#Setup and Run AirController
AirController.StartPwm()

@app.route("/", methods=['GET'])
def InfoPage():
   data_set = {
    'isRunning':AirController.isRunning,
    'lastState': AirController.lastState,
    'Time' : datetime.now(),
    'Hz' : AirController.Hz,
    'DutyCycle':AirController.dutyCycle,
   }
   return jsonify({"data":data_set})

@app.route("/air/start", methods=['POST'])
def PwmStarter():
    if not AirController.isRunning:
        AirController.start_pwm()
        data_set = {
            'Message': 'Fan is started',
            'Time': datetime.now(),
            'Hz': AirController.Hz,
            'DutyCycle': AirController.dutyCycle,
        }
        return jsonify({'data': data_set}), 200
    else:
        data_set = {
            'Message': 'Fan is still running'
        }
        return jsonify({'Error': data_set}), 409


@app.route("/air/stop", methods=['POST'])
def PwmStoper():
    if AirController.isRunning:
        AirController.stop_pwm()
        data_set = {
            'Message': 'Fan is stopped',
            'Time': datetime.now(),
        }
        return jsonify({'data': data_set}), 200
    else:
        data_set = {
            'Message': 'Fan not running, cannot stop'
        }
        return jsonify({'Error': data_set}), 409

@app.route("/air/ctrl", methods=['POST'])
def PwmChange():
    if AirController.isRunning:
        NewDuty = request.json['newDuty']
        print(NewDuty)
        AirController.ChangePwmDuty(int(NewDuty))
        return jsonify({'Result':'Success','NewDutyCycle':int(NewDuty)})
    return jsonify({'Result':'Error Not Running','NewDutyCycle':int(NewDuty)})
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5533,debug=True)