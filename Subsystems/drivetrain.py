import wpilib
import ctre
from wpilib.command.subsystem import Subsystem
from robotmap import channels

from wpilib.drive import MecanumDrive


class Drivetrain:

	def __init__(self, front_left, rear_left, front_right, rear_right)

		self.drive = wpilib.drive.MecanumDrive(
			front_left, 
			rear_left, 
			front_right, 
			rear_right,
			)

		#what does this do?
		self.drive.setExpiration(0.1)

		self.driver = wpilib.XboxController(0)
		self.operator = wpilib.XboxController(1)

		#what does this do?
		self.auto_exec = iter([])


	def drive_Cartesian(self, ySpeed, xSpeed, zRotation, gyroAngle = 0.0):
		self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)

	def set(self, ySpeed, xSpeed, zRotation, gyroAngle):
		self.drive.driveCartesian(ySpeed, xSpeed, zRotation, gyroAngle)

	def operatorControl(self):
		self.drive.setSafetyEnabled(True)
		while self.isOperatorCOntrol() and self.isEnabled():
			self.drive.driveCartesian(
				self.driver.getX(),
				self.driver.getY(),
				self.driver.getZ(), 
				0)

			wpilib.Timer.delay(0.005) 

	def stop(self):
		self.drive.stopMotor()
		
