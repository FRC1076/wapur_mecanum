import sys 
sys.path.append("C:/Users/biaoh/Desktop/1076 Software/wapur_mecanum/wapur_mecanum")

import wpilib
from subsystems.drivetrain import Drivetrain 


#def drive_Cartesian(self, ySpeed, xSpeed, zRotation, gyroAngle = 0.0):

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

	drivetrain.Cartesian_Drive(1.0, 0, 90, gyroAngle = 0.0)
	assert ySpeed == 1
	assert xSpeed
