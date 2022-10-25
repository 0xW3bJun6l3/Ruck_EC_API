#!/usr/bin/env python3
from hashlib import new
import time
from datetime import datetime

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

class PWMCtrl:

    def __init__(self,Hz,Pin,dutyCycle):
        self.isRunning = False
        self.lastState = ''

        self.Hz:int = Hz
        self.Pin:int = Pin
        self.dutyCycle:int = dutyCycle

        self.HasChanged:bool = False
        self.dutyChangeVal:int = 0
        
        # pwmCtrl WILL HOLD THE PWM OBJECT FROM GPIO CLASS
        self.pwmCtrl  = ''
        self.StartTime = datetime.now()

        self.Pwm_Min:int = 0
        self.Pwm_Max:int = 100
        
        pass

    def setupPWM(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Pin,GPIO.OUT)
        self.pwmCtrl = GPIO.PWM(self.Pin,self.Hz)
        self.lastState = 'Setup'

    def StartPwm(self):
        self.setupPWM()
        print('Abluft-Start mit ' + str(self.dutyCycle) + ' %')
        self.pwmCtrl.start(int(self.dutyCycle))
        self.isRunning = True
        self.lastState = 'Started'

    def StopPwm(self):
        print("Abluft wird Runtergefahren")
        self.pwmCtrl.stop()
        GPIO.cleanup()
        print("\nPWM gestoppt, GPIO Cleanup durchgeführt.")
        self.lastState = 'Stoped'
        self.isRunning = False

    def hasChanged(self):
        if(self.dutyCycle != self.dutyChangeVal):
            self.ChangePwmDuty(self.dutyChangeVal)

        else:
            pass

    def ChangePwmDuty(self,newDuty:int):
        if newDuty>99:
            newDuty=99
        if newDuty<0:
            newDuty=0
        if newDuty<3:
            # TEST MIN VALUE THAT WORKS FINE
            newDuty=4
        self.lastState = 'Duty-Change'
        self.dutyCycle = newDuty
        self.pwmCtrl.ChangeDutyCycle(int(newDuty))
        
