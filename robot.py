import wpilib
import ctre
from wpilib.drive import MecanumDrive
import autonomous
from subsystems.catcher import Grabber
from wpilib.interfaces import GenericHID
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
		#left = wpilib.SpeedControllerGroup(self.left1, self.left2)

		self.front_right_motor = ctre.WPI_TalonSRX(self.FRONT_RIGHT_CHANNEL)
		self.rear_right_motor = ctre.WPI_TalonSRX(self.REAR_RIGHT_CHANNEL)
		#right = wpilib.SpeedControllerGroup(self.right1, self.right2)

		# may or may not need to invert
		# self.front_left_motor.setInverted(True)
		# #may need to change this
		# self.rear_left_motor.setInverted(True)

		self.drivetrain = Drivetrain(self.front_left_motor, self.rear_left_motor, self.front_right_motor, self.rear_right_motor)


		self.grabber = Grabber(ctre.WPI_TalonSRX(GRABBER_ID))


		elevator1 = ctre.WPI_TalonSRX(ELEVATOR1_ID)
		elevator2 = ctre.WPI_TalonSRX(ELEVATOR2_ID)
		self.elevator = Elevator(
			wpilib.SpeedControllerGroup(elevator1, elevator2))

	def operatorControl(self):
		self.drive.setSafetyEnabled(True)
		while self.isOperatorControl() and self.isEnabled():
			self.drive.driveCartesian(
				self.drivetrain.driver.getX(),
				self.drivetrain.driver.getY(),
				self.drivetrain.driver.getZ(),
				0)

			wpilib.Timer.delay(0.005)


	# def robotPeriodic(self):
	# 	print("Test")

	def teleopInit(self):
		self.left_activated = False
		self.right_activated = False
		print ("TELEOP BEGIN")
		self.forward = 0

	def teleopPeriodic(self):
		deadzone_value = 0.2
		max_acceleration = 0.3
		goal_forward = -self.drivetrain.driver.getY(RIGHT)
		goal_sideways = self.drivetrain.driver.getX(LEFT)

		max_forward = 1.0
		max_sideways = 1.0

		goal_forward = deadzone(goal_forward * max_forward, deadzone_value)
		goal_sideways = deadzone(goal_sideways * max_sideways, deadzone_value)

		alpha = goal_forward - self.forward

		if abs(alpha) < max_acceleration:
			self.forward += alpha
		else:
			self.forward += max_acceleration # * sign(delta)

		if self.drivetrain.driver.getXButton():
			self.drivetrain.stop()
		else:
			self.drivetrain.drive_Cartesian(self.forward, goal_sideways, 0)


	def autonomousInit(self):
		print("AUTONOMOUS BEGIN!")

		self.auton = autonomous.straight_ahead(
			self.drivetrain)

	def autonomousPeriodic(self):
		try:
			next(self.auton)
			print("We are at autonomous periodic")
		except StopIteration:
			self.drivetrain.stop()

def deadzone(val, deadzone):
	if abs(val) < deadzone:
		return 0
	return val


if __name__ == "__main__":
	wpilib.run(Robot, physics_enabled = True)
