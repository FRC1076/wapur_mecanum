import wpilib
import wpilib.drive
from wpilib import DoubleSolenoid

class Drivetrain:

	def __init__(self, left, right)
		self.robot_drive = wpilib.drive.DifferentialDrive(left, right)

		self.right = right
		self.left = left

	def arcade_drive(self, foward, rotate):
		self.robot_drive.arcadeDrive(forward, rotate)

	def stop(self):
		self.robot_drive.stopMotor()
		
