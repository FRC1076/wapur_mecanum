from helper import GetSet
from subsystems.catcher import Catcher

def test_make_grabber():
	left_motor = GetSet(0)
	right_motor = GetSet(0)

	catcher = Catcher(left_motor, right_motor)
	catcher.set()
	assert left_motor.state == -1
	assert right_motor.state == -1
	catcher.set(speed=-0.5)
	assert left_motor.state == -0.5
	assert right_motor.state == -0.5
	catcher.set(speed = -1.0)
	assert left_motor.state == -1
    assert right_motor.state == -1
    catcher.set(speed = -0.5)
    assert left_motor.state == -0.5
    assert right_motor.state == -0.5
