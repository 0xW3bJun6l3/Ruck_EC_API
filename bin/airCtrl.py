#!/usr/bin/env python3
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
        self.pwmCtrl  = None
        self.StartTime = datetime.now()

        self.Pwm_Min:int = 5
        self.Pwm_Max:int = 100

        pass

    def setupPWM(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Pin,GPIO.OUT)
        self.pwmCtrl = GPIO.PWM(self.Pin,self.Hz)
        self.lastState = 'Setup'

    def StartPwm(self):
        if not self.isRunning:
            self.setupPWM()
            print('Abluft-Start mit ' + str(self.dutyCycle) + ' %')
            self.pwmCtrl.start(int(self.dutyCycle))
            self.isRunning = True
            self.lastState = 'Started'

    def StopPwm(self):
        if self.isRunning:
            print("Abluft wird Runtergefahren")
            self.pwmCtrl.stop()
            GPIO.cleanup(self.Pin)
            print("\nPWM gestoppt, GPIO Cleanup durchgeführt.")
            self.lastState = 'Stoped'
            self.isRunning = False

    def hasChanged(self):
        if(self.dutyCycle != self.dutyChangeVal):
            self.ChangePwmDuty(self.dutyChangeVal)

        else:
            pass

    def ChangePwmDuty(self,newDuty:int):
        if self.isRunning:
            # Stelle sicher, dass newDuty nicht unter 5 fällt
            if newDuty < 5:
                newDuty = 5
            # Stelle sicher, dass newDuty nicht über 95 steigt
            elif newDuty > 95:
                newDuty = 95

            self.lastState = 'Duty-Change'
            self.dutyCycle = newDuty
            self.pwmCtrl.ChangeDutyCycle(newDuty)

    def ChangePwmHz(self):
        pass