from inmoov.Humanoid import Humanoid
from inmoov.PwmHatHumanoid import PwmHatHumanoid

h = PwmHatHumanoid()
h.initialize()
for x in range(6):
    h.finger_tension_delta(Humanoid.LEFT_FINGER_THUMB, direction = Humanoid.DIR_TIGHTEN)
h.stop()