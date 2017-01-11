from inmoov.Humanoid import Humanoid
from inmoov.PwmHatHumanoid import PwmHatHumanoid

h = PwmHatHumanoid()
h.initialize()
h.reset_all_servos()

while True:
    h.finger_tension(Humanoid.RIGHT_FINGERS, position = 95)

    key = raw_input("Give me a cup, please (and press Enter)")
    if key == 'q':
        break

    h.finger_tension(Humanoid.RIGHT_FINGER_THUMB, position = 85)
    h.finger_tension(Humanoid.RIGHT_FINGER_INDEX, position = 55)
    h.finger_tension(Humanoid.RIGHT_FINGER_MIDDLE, position = 45)
    h.finger_tension(Humanoid.RIGHT_FINGER_RING, position = 55)
    h.finger_tension(Humanoid.RIGHT_FINGER_PINKY, position = 55)

    key = raw_input("Take the cup, please (and press Enter)")
    if key == 'q':
        break

    h.finger_tension(Humanoid.RIGHT_FINGERS, position = 95)

h.stop()
h.initialize()
h.reset_all_servos()



