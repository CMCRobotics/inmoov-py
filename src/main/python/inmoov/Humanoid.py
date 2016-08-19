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
    
    LEFT_FINGER_THUMB  = [0]
    LEFT_FINGER_INDEX  = [1]
    LEFT_FINGER_MIDDLE = [2]
    LEFT_FINGER_RING   = [3]
    LEFT_FINGER_PINKY  = [4]
    LEFT_WRIST_ROTATION = [5]
   
    LEFT_FINGERS = LEFT_FINGER_THUMB + LEFT_FINGER_INDEX + LEFT_FINGER_MIDDLE + LEFT_FINGER_RING + LEFT_FINGER_PINKY
    
    ALL_SERVOS = LEFT_FINGERS + LEFT_WRIST_ROTATION
    
    
    
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def finger_tension_delta(self, fingers, direction = DIR_LOOSEN, delta = 10, callback = None):
        pass

    @abstractmethod
    def stop(self, callback = None):
        pass

    @abstractmethod
    def reset_all_servos(self, callback = None):
        pass