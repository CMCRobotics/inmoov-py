from gpiozero import Button
from inmoov.Humanoid import Humanoid
from inmoov.PwmHatHumanoid import PwmHatHumanoid

h = PwmHatHumanoid()
h.initialize()
h.reset_all_servos()

button = Button(4)

print "Press the stick central button to grab a cup. Press it again to release it."
while True:
    h.finger_tension(Humanoid.RIGHT_FINGERS, position = 95)
    button.wait_for_press()
    h.finger_tension(Humanoid.RIGHT_FINGER_THUMB, position = 85)
    h.finger_tension(Humanoid.RIGHT_FINGER_INDEX, position = 55)
    h.finger_tension(Humanoid.RIGHT_FINGER_MIDDLE, position = 45)
    h.finger_tension(Humanoid.RIGHT_FINGER_RING, position = 55)
    h.finger_tension(Humanoid.RIGHT_FINGER_PINKY, position = 55)
    button.wait_for_press()

h.stop()
h.initialize()
h.reset_all_servos()



