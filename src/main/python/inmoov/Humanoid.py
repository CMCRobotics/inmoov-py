'''
Created on Aug 04, 2016

@author: bcopy
'''
from abc import ABCMeta,abstractmethod
import time



class Humanoid(object):
    __metaclass__ = ABCMeta

    DIR_FORWARD = 0x01
    DIR_BACKWARD = 0x02
    DIR_TIGHTEN = 0x01
    DIR_LOOSEN = 0x02
    
    LEFT_FINGER_THUMB  = 0x01
    LEFT_FINGER_INDEX  = 0x02
    LEFT_FINGER_MIDDLE = 0x03
    LEFT_FINGER_RING   = 0x04
    LEFT_FINGER_PINKY  = 0x05
    
    LEFT_FINGERS = [ LEFT_FINGER_THUMB, LEFT_FINGER_INDEX, LEFT_FINGER_MIDDLE, LEFT_FINGER_RING, LEFT_FINGER_PINKY ]
    
    
    
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def fingerTensionDelta(self, fingers, direction = DIR_LOOSEN, delta = 10, callback = None):
        pass

    @abstractmethod
    def stop(self, callback = None):
        pass
 


