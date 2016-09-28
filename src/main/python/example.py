# uncomment one part at a time to try

import time
import datetime
from inmoov.Humanoid import Humanoid
from inmoov.PwmHatHumanoid import PwmHatHumanoid

h = PwmHatHumanoid()
h.initialize()
h.reset_all_servos()

def DecToFingerBin(number):
    for i in range(5):
        if (number/(2**i))&1 == 1:
            h.finger_tension([i], 85)
        else:
            h.finger_tension([i], 15)

# bad stuff, don't run this ;)
#h.finger_tension(Humanoid.RIGHT_FINGER_MIDDLE, position = 100)

# thumb tremor
#h.finger_tension(Humanoid.RIGHT_FINGER_THUMB, position = 100)
#for x in range(7):
#    h.finger_tension_delta(Humanoid.RIGHT_FINGER_THUMB, direction = Humanoid.DIR_TIGHTEN, delta = 10)
#    time.sleep(1)

# binary counting
h.finger_tension(Humanoid.RIGHT_WRIST_ROTATION, 50)
for number in range(32):
    print('Actual number: '+str(number))
    DecToFingerBin(number)
    time.sleep(1)

# wrist moves
#for x in range(3):
#    h.finger_tension(Humanoid.RIGHT_WRIST_ROTATION, 40)
#    time.sleep(1)
#    h.finger_tension(Humanoid.RIGHT_WRIST_ROTATION, 60)
#    time.sleep(1)

# clock
#minute = datetime.datetime.now().minute
#print("actual time (minutes): " + str(minute))
#DecToFingerBin(minute)

#h.stop()
#h.initialize()
#h.reset_all_servos()



