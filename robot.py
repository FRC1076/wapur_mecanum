import wpilib
import ctre
import robotpy_ext.common_drivers.navx as navx
from wpilib.drive import MecanumDrive
import autonomous
from wpilib.interfaces import GenericHID
from subsystems.grabber import Grabber
from subsystems.elevator import Elevator
from subsystems.drivetrain import Drivetrain

LEFT = GenericHID.Hand.kLeft
RIGHT = GenericHID.Hand.kRight

GRABBER_ID = 1

ELEVATOR1_ID = 1
ELEVATOR2_ID = 1

class Robot(wpilib.IterativeRobot):

	def robotInit(self):

		self.FRONT_LEFT_CHANNEL = 4
		self.REAR_LEFT_CHANNEL = 5
		self.FRONT_RIGHT_CHANNEL = 6
		self.REAR_RIGHT_CHANNEL = 7

		self.front_left_motor = ctre.WPI_TalonSRX(self.FRONT_LEFT_CHANNEL)
		self.rear_left_motor = ctre.WPI_TalonSRX(self.REAR_LEFT_CHANNEL)

		self.front_right_motor = ctre.WPI_TalonSRX(self.FRONT_RIGHT_CHANNEL)
		self.rear_right_motor = ctre.WPI_TalonSRX(self.REAR_RIGHT_CHANNEL)

		# may or may not need to invert
		# self.front_left_motor.setInverted(True)
		# #may need to change this
		# self.rear_left_motor.setInverted(True)
		self.gyro = navx.ahrs.AHRS.create_spi()

		self.drivetrain = Drivetrain(self.front_left_motor, self.rear_left_motor, self.front_right_motor, self.rear_right_motor)

		self.driver = wpilib.XboxController(0)
		self.operator = wpilib.XboxController(1)

		self.grabber = Grabber(ctre.WPI_TalonSRX(GRABBER_ID))

		elevator1 = ctre.WPI_TalonSRX(ELEVATOR1_ID)
		elevator2 = ctre.WPI_TalonSRX(ELEVATOR2_ID)
		self.elevator = Elevator(wpilib.SpeedControllerGroup(elevator1, elevator2))

		grabber = ctre.WPI_TalonSRX(GRABBER_ID)
		self.grabber = Grabber(wpilib.SpeedControllerGroup(grabber))

	def operatorControl(self):
		self.drive.setSafetyEnabled(True)
		while self.isOperatorControl() and self.isEnabled():
			self.drive.driveCartesian(
				self.driver.getX(),
				self.driver.getY(),
				self.driver.getZ(),
				0)

			wpilib.Timer.delay(0.005)


	def robotPeriodic(self):
		return

	def teleopInit(self):
		self.left_activated = False
		self.right_activated = False
		print ("TELEOP BEGIN")
		self.yDist = 0

	def teleopPeriodic(self):
		deadzone_value = 0.2
		max_acceleration = 0.3
		# driver controls
		ySpeed = self.driver.getY(RIGHT)
		xSpeed = self.driver.getX(RIGHT)

		zRotation = self.driver.getX(LEFT)

		max_ySpeed = 1.0
		max_xSpeed = 1.0
		max_rotSpeed = 1.0

		ySpeed = deadzone(ySpeed * max_ySpeed, deadzone_value)
		xSpeed = deadzone(xSpeed * max_xSpeed, deadzone_value)
		zRotation = deadzone(zRotation * max_rotSpeed, deadzone_value)

		# delta = yForward - self.yDist

		# if abs(delta) < max_acceleration:
		# 	self.yDist += delta
		# else:
		# 	self.yDist += max_acceleration * sign(delta)

		# operator controls
		elevatorUp = self.operator.getTriggerAxis(RIGHT)
		elevatorDn = self.operator.getTriggerAxis(LEFT)

		TRIGGER_LEVEL = 0.35

		if abs(elevatorUp) > TRIGGER_LEVEL:
			self.elevator.go_up(elevatorUp)
		elif abs(elevatorDn) > TRIGGER_LEVEL:
			self.elevator.go_down(elevatorDn)
		else:
			self.elevator.stop()

		#intake, negative is reversing direction

		intake_stick = -deadzone(self.operator.getY(RIGHT), deadzone_value)

		self.grabber.setSpeed(intake_stick * 0.5)

		if self.driver.getXButton():
			self.drivetrain.stop()
		else:
			self.drivetrain.drive_Cartesian(ySpeed, xSpeed, zRotation)


	def autonomousInit(self):
		print("AUTONOMOUS BEGIN!")

		self.auton = autonomous.straight_ahead(self.drivetrain)

	def autonomousPeriodic(self):
		try:
			next(self.auton)
			# print("We are at autonomous periodic")
		except StopIteration:
			self.drivetrain.stop()

def deadzone(val, deadzone):
	if abs(val) < deadzone:
		return 0
	return val


if __name__ == "__main__":
	wpilib.run(Robot, physics_enabled = True)
