'''
Adafruit PWM Hat Humanoid implementation
Created on Aug 04, 2016

@author: bcopy
'''

from inmmov.Humanoid import Humanoid
from Adafruit_PWM_Servo_Driver import PWM
import time

class PwmHatHumanoid(Humanoid):
    HKING_SERVO_MIN = 230  # Min pulse length out of 4096
    HKING_SERVO_MAX = 540  # Max pulse length out of 4096
    HKING_SERVO_MED = 230+130  # Max pulse length out of 4096

    BLACK_SERVO_MIN = 120  # Min pulse length out of 4096
    BLACK_SERVO_MAX = 650  # Max pulse length out of 4096
    BLACK_SERVO_MED = 120+265  # Max pulse length out of 4096
   
    def __init__(self):
        # Initialise the PWM device using the default address
        self.pwm = PWM(0x40)
        self.pwm.setPWMFreq(60)
        # this member array stores the PWM status of all servos.
        self.servoPWM = []
        
        # Set all servos to medium position
        for x in LEFT_FINGERS:
            self._applyPWM(x,0, HKING_SERVO_MED)

        self.initialized = False
        

    def initialize(self):
        super(PwmHatHumanoid,self).initialize()
        self.initialized = True
        

    '''
      apply a delta to the given finger (loosen or tighten)
    '''
    def fingerTensionDelta(self, fingers, direction = Humanoid.DIR_LOOSEN, delta = 10, callback = None):
        dir = (-1 if direction == Humanoid.DIR_LOOSEN else 1)
        for f in fingers:
            dlt = delta * dir
            # control we have not gone over a maximum or minimum
            if( direction == Humanoid.DIR_LOOSEN) :
                newVal = max(HKING_SERVO_MIN, self.servoPWM[f] + dlt)
            else:
                newVal = min(HKING_SERVO_MAX, self.servoPWM[f] + dit)
            self._applyPWM(f, 0, newVal)
            
        if callback is not None:
            callback()

    def stop(self, callback = None):
        #  TODO : Stop all servos
        if callback is not None:
            callback()
    
    '''
     Apply a new PWM and store the known value
    '''
    def _applyPWM(self, servo, on=0, off=HKING_SERVO_MED):
        self.pwm.setPWM(servo, on, off)
        self.servoPWM[servo] = off
 
Humanoid.register(PwmHatHumanoid)

if __name__ == '__main__':
    _humanoid = PwmHatHumanoid()
