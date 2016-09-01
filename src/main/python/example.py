# uncomment one part at a time to try

import time
from inmoov.Humanoid import Humanoid
from inmoov.PwmHatHumanoid import PwmHatHumanoid

h = PwmHatHumanoid()
h.initialize()
h.reset_all_servos()


# bad stuff, don't run this ;)
#h.finger_tension(Humanoid.RIGHT_FINGER_MIDDLE, position = 100)

# thumb tremor
#h.finger_tension(Humanoid.RIGHT_FINGER_THUMB, position = 100)
#for x in range(7):
#    h.finger_tension_delta(Humanoid.RIGHT_FINGER_THUMB, direction = Humanoid.DIR_TIGHTEN, delta = 10)
#    time.sleep(1)

# binary counting
while True:
    for number in range(32):
        print('Actual number: '+str(number))
        for i in range(5):
            if (number/(2**i))&1 == 1:
                h.finger_tension([i], 100)
            else:
                h.finger_tension([i], 10)
        time.sleep(1)

h.stop()
