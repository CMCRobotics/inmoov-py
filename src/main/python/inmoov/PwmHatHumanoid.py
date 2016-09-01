'''
Adafruit PWM Hat Humanoid implementation
Created on Aug 04, 2016

@author: bcopy
@modified: aakafosfor
'''

from inmoov.Humanoid import Humanoid
import Adafruit_PCA9685
import time
import logging


class PwmHatHumanoid(Humanoid):
    # TODO: are these values really right?
    HKING_SERVO = { # TOOD: make a class for that?
        'min': 230, # pulse length out of 4096
        'med': 230+130,
        'max': 540
    }

    BLACK_SERVO = {
        'min': 120,
        'med': 120+265,
        'max': 650
    }

    # servo types (PWM channel: type)
    SERVOS = {
        0: HKING_SERVO,
        1: HKING_SERVO,
        2: HKING_SERVO,
        3: HKING_SERVO,
        4: HKING_SERVO,
        5: BLACK_SERVO
    }

    # finger connections (finger: PWM channel)
    FINGERS = { # TODO: its not just fingers... better name?
        Humanoid.RIGHT_FINGER_THUMB[0]: 0,
        Humanoid.RIGHT_FINGER_INDEX[0]: 1,
        Humanoid.RIGHT_FINGER_MIDDLE[0]: 2,
        Humanoid.RIGHT_FINGER_RING[0]: 3,
        Humanoid.RIGHT_FINGER_PINKY[0]: 4,
        Humanoid.RIGHT_WRIST_ROTATION[0]: 5
    }

   
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        # Initialise the PWM device using the default address
        self.pwm = Adafruit_PCA9685.PCA9685()
        # Alternatively specify a different address and/or bus:
        #self.pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
        
        self.pwm.set_pwm_freq(60)
        # this member array stores the PWM status of all servos.
        self.servoPWM = [0,0,0,0,0,0] # TODO: automatic size
        
        # Set all servos to medium position
        for pwmPosition in self.FINGERS:
            self._apply_pwm(pwmPosition, 50)

        self.initialized = False
        

    def initialize(self):
        super(PwmHatHumanoid,self).initialize()
        self.initialized = True
        
    '''
     Set given fingers to specified absolute position (in %)
    '''
    def finger_tension(self, fingers, position, callback = None):
        for f in fingers:
            self._apply_pwm(self.FINGERS[f], position)

        if callback is not None:
            callback()

    '''
     Apply a delta to given fingers (loosen or tighten)
     delta in %
    '''
    def finger_tension_delta(self, fingers, direction = Humanoid.DIR_LOOSEN, delta = 10, callback = None):
        dir = (1 if direction == Humanoid.DIR_LOOSEN else -1)
        for f in fingers:
            newValue = self.servoPWM[f] + delta * dir
            self._apply_pwm(self.FINGERS[f], newValue)
            
        if callback is not None:
            callback()

    '''
     Stop power to all servos
    '''
    def stop(self, callback = None):
        #  TODO : Stop all servos
        if callback is not None:
            callback()
    
    '''
     Apply a new PWM and store the known value
     position in %
    '''
    def _apply_pwm(self, pwmChannel, position):
        servo = self.SERVOS[pwmChannel]
        position = max(0, min(100, position))
        #print('_apply_pwm: channel = '+str(pwmChannel)+', position = '+str(position))
        off = int(servo['min'] + (servo['max'] - servo['min']) * position/100.0)
        self.pwm.set_pwm(pwmChannel, 0, off)
        self.servoPWM[pwmChannel] = position
 
    def reset_all_servos(self, callback = None):
        for servo in self.FINGERS:
            self._apply_pwm(servo, 50)
        if callback is not None:
            callback()
        
Humanoid.register(PwmHatHumanoid)

if __name__ == '__main__':
    _humanoid = PwmHatHumanoid()
