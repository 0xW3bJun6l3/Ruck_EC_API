from flask import Flask, jsonify, request
from datetime import datetime
from airCtrl import PWMCtrl


app = Flask(__name__)
AirController = PWMCtrl(1000,18,10)
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

@app.route("/air/start", methods=['GET'])
def PwmStarter():
    if(AirController.isRunning == False):
        AirController.StartPwm()
        data_set={
            'Message' : 'Fan is Started',
            'Time' : datetime.now(),
            'Hz' : AirController.Hz,
            'DutyCycle':AirController.dutyCycle,
        }
        return jsonify({'data':data_set})

    else:
        data_set={
            'Message' : 'Fan is still Running'
        }
        return jsonify({'Error':data_set})

        
@app.route("/air/stop", methods=['GET'])
def PwmStoper():
    if(AirController.isRunning == False):
        data_set={
            'Message' : 'Fan not Running, can´t Stop'
        }
        return jsonify({'Error':data_set})
    else:
        AirController.StopPwm()
        data_set={
            'Message' : 'Fan is Stopped',
            'Time' : datetime.now(),
        }
        return jsonify({'data':data_set})

@app.route("/air/ctrl", methods=['POST'])
def PwmChange():
    NewDuty = request.json['newDuty']
    print(NewDuty)
    AirController.ChangePwmDuty(int(NewDuty))
    return jsonify({'Result':'Success','NewDutyCycle':int(NewDuty)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5533,debug=True)
