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
    
    RIGHT_FINGER_THUMB  = [0]
    RIGHT_FINGER_INDEX  = [1]
    RIGHT_FINGER_MIDDLE = [2]
    RIGHT_FINGER_RING   = [3]
    RIGHT_FINGER_PINKY  = [4]
    RIGHT_WRIST_ROTATION = [5]
   
    RIGHT_FINGERS = RIGHT_FINGER_THUMB + RIGHT_FINGER_INDEX + RIGHT_FINGER_MIDDLE + RIGHT_FINGER_RING + RIGHT_FINGER_PINKY
    
    ALL_SERVOS = RIGHT_FINGERS + RIGHT_WRIST_ROTATION
    
    
    
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def finger_tension(self, fingers, position = 50, callback = None):
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
