import wpilib
import wpilib.drive
from wpilib import DoubleSolenoid

class Drivetrain:

	def __init__(self, front_left, rear_left, front_right, rear_right)

		self.front_left_motor = front_left
		self.rear_left_motor = rear_left
		self.front_right_motor = front_right
		self.rear_right_motor = rear_right


		self.drive = MecanumDrive(
			self.front_left_motor, 
			self.rear_left_motor, 
			self.front_right_motor, 
			self.rear_right_motor,
			)

		
		#what does this do?
		self.drive.setExpiration(0.1)

		self.driver = wpilib.XboxController(0)
		#self.operator = wpilib.XboxController(1)

		#what does this do?
		self.auto_exec = iter([])

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
		self.robot_drive.stopMotor()
		
