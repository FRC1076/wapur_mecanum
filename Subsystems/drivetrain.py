import wpilib
import wpilib.drive
from wpilib import DoubleSolenoid

class Drivetrain:

	def __init__(self)
		
		self.front_left_motor = ctre.WPI_TalonSRX(FRONT_LEFT_CHANNEL)
		self.rear_left_motor = ctre.WPI_TalonSRX(REAR_LEFT_CHANNEL)
		#left = wpilib.SpeedControllerGroup(self.left1, self.left2)

		self.front_right_motor = ctre.WPI_TalonSRX(FRONT_RIGHT_CHANNEL)
		self.rear_right_motor = ctre.WPI_TalonSRX(REAR_RIGHT_CHANNEL)
		#right = wpilib.SpeedControllerGroup(self.right1, self.right2)	

		self.front_left_motor.setInverted(True)

		#may need to change this
		self.rear_left_motor.setInverted(True)


		self.drive = MecanumDrive(
			self.front_left_motor, 
			self.rear_left_motor, 
			self.front_right_motor, 
			self.rear_right_motor,
			)

		#what does this do?
		self.drive.setExpiration(0.1)

		self.drivetrain = Drivetrain(left, right, )

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
		
