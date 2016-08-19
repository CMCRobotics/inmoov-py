'''
Adafruit PWM Hat Humanoid implementation
Created on Aug 04, 2016

@author: bcopy
'''

from inmoov.Humanoid import Humanoid
import Adafruit_PCA9685
import time
import logging


class PwmHatHumanoid(Humanoid):
    global HKING_SERVO_MIN  # Min pulse length out of 4096
    HKING_SERVO_MIN = 230
    global HKING_SERVO_MAX  # Max pulse length out of 4096
    HKING_SERVO_MAX = 540
    global HKING_SERVO_MED  # Med pulse length out of 4096
    HKING_SERVO_MED = 230+130

    BLACK_SERVO_MIN = 120  # Min pulse length out of 4096
    BLACK_SERVO_MAX = 650  # Max pulse length out of 4096
    BLACK_SERVO_MED = 120+265  # Max pulse length out of 4096
   
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # Initialise the PWM device using the default address
        self.pwm = Adafruit_PCA9685.PCA9685()
        # Alternatively specify a different address and/or bus:
        #self.pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
        
        self.pwm.set_pwm_freq(60)
        # this member array stores the PWM status of all servos.
        self.servoPWM = []
        
        # Set all servos to medium position
        for x in LEFT_FINGERS:
            self._apply_pwm(x,0, HKING_SERVO_MED)

        self.initialized = False
        

    def initialize(self):
        super(PwmHatHumanoid,self).initialize()
        self.initialized = True
        

    '''
      apply a delta to the given finger (loosen or tighten)
    '''
    def finger_tension_delta(self, fingers, direction = Humanoid.DIR_LOOSEN, delta = 10, callback = None):
        dir = (-1 if direction == Humanoid.DIR_LOOSEN else 1)
        for f in fingers:
            dlt = delta * dir
            # control we have not gone over a maximum or minimum
            if( direction == Humanoid.DIR_LOOSEN) :
                newVal = max(HKING_SERVO_MIN, self.servoPWM[f] + dlt)
            else:
                newVal = min(HKING_SERVO_MAX, self.servoPWM[f] + dit)
            self._apply_pwm(f, 0, newVal)
            
        if callback is not None:
            callback()

    def stop(self, callback = None):
        #  TODO : Stop all servos
        if callback is not None:
            callback()
    
    '''
     Apply a new PWM and store the known value
    '''
    def _apply_pwm(self, servo, on=0, off=HKING_SERVO_MED):
        self.pwm.set_pwm(servo, on, off)
        self.servoPWM[servo] = off
 
    def reset_all_servos(self, callback = None):
        for srvo in Humanoid.ALL_SERVOS:
            self._apply_pwm(srvo,0,0)
        if callbox is not None:
            callback()
        
Humanoid.register(PwmHatHumanoid)

if __name__ == '__main__':
    _humanoid = PwmHatHumanoid()
