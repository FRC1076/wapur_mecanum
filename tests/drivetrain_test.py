import wpilib
from subsystems.drivetrain import Drivetrain 

def test_forward():
	front_left_motor = GetSet(0)
	rear_left_motor = GetSet(0)
	front_right_motor = GetSet(0)
	rear_right_motor = GetSet(0)

	drivetrain = Drivetrain(
		front_left_motor, 
		rear_left_motor, 
		front_right_motor, 
		rear_right_motor
		)

	drivetrain.Cartesian_Drive(
		front_left_motor, 
		rear_left_motor, 
		front_right_motor,
		rear_right_motor
		)
