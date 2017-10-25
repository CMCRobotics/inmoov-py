import time
import datetime
from inmoov.Humanoid import Humanoid
from inmoov.PwmHatHumanoid import PwmHatHumanoid

h = PwmHatHumanoid()
def DecToFingerBin(number):
    for i in range(5):
        if (number/(2**i))&1 == 1:
            h.finger_tension([i], 85)
        else:
            h.finger_tension([i], 15)

#while True:
#    h.pwm.set_pwm(8, 0, 4000)
#    print("aa")
#    time.sleep(1)
#    h.pwm.set_pwm(8, 0, 0)
#    print("bb")
#    time.sleep(1)

while True:
    h.initialize()
    h.reset_all_servos()

    # binary counting
    for number in range(32):
        # print('Actual number: '+str(number))
        DecToFingerBin(number)
        time.sleep(1)

    h.stop()

    time.sleep(60*5)