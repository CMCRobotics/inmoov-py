from inmoov.Humanoid import Humanoid
from inmoov.PwmHatHumanoid import PwmHatHumanoid

h = PwmHatHumanoid()
h.initialize()
h.reset_all_servos()

print 'Preparing...'
# TODO: flush output
h.finger_tension(Humanoid.RIGHT_FINGERS, position = 50)

end = False
step = 10
print 'Commands:'
print 'q   e  r  t  y  u    ---> tighter            -  ---> smaller step'
print '^    d  f  g  h  j   ---> middle position    +  ---> bigger step'
print '|     c  v  b  n  m  ---> looser'
print '|     ^  ^  ^  ^  ^'
print 'exit  |  |  |  |  |'
print '      |  |  |  |  +--> pinky'
print '      |  |  |  +-----> ring'
print '      |  |  +--------> middle'
print '      |  +-----------> index'
print '      +--------------> thumb'
while not end:
    print "Step = %d, Fingers' positions: %d, %d, %d, %d, %d" % (step, h.servoPWM[0], h.servoPWM[1], h.servoPWM[2], h.servoPWM[3], h.servoPWM[4])
    key = raw_input('> Command, master?')
    if key == 'q':
        end = True
    elif key == 'e':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_THUMB, delta = -step)
    elif key == 'c':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_THUMB, delta = step)
    elif key == 'd':
        h.finger_tension(Humanoid.RIGHT_FINGER_THUMB, position = 50)
    elif key == 'r':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_INDEX, delta = -step)
    elif key == 'v':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_INDEX, delta = step)
    elif key == 'f':
        h.finger_tension(Humanoid.RIGHT_FINGER_INDEX, position = 50)
    elif key == 't':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_MIDDLE, delta = -step)
    elif key == 'b':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_MIDDLE, delta = step)
    elif key == 'g':
        h.finger_tension(Humanoid.RIGHT_FINGER_MIDDLE, position = 50)
    elif key == 'y':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_RING, delta = -step)
    elif key == 'n':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_RING, delta = step)
    elif key == 'h':
        h.finger_tension(Humanoid.RIGHT_FINGER_RING, position = 50)
    elif key == 'u':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_PINKY, delta = -step)
    elif key == 'm':
        h.finger_tension_delta(Humanoid.RIGHT_FINGER_PINKY, delta = step)
    elif key == 'j':
        h.finger_tension(Humanoid.RIGHT_FINGER_PINKY, position = 50)
    elif key == '-':
        step = step - 1
    elif key == '+':
        step = step + 1

h.stop()
h.initialize()
h.reset_all_servos()



