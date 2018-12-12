import wpilib 
import ctre
from wpilib.drive import MecanumDrive
import autonomous
from subsystems.grabber import Grabber
from subsystems.elevator import Elevator

LEFT = GenericHID.Hand.kLeft
RIGHT = GenericHID.Hand.kRight

GRABBER_ID = 1
ELEVATOR1_ID = 1
ELEVATOR2_ID = 1

class Robot(wpilib.IterativeRobot):

	#channels on the roborio that the motor controllers are plugged into
	FRONT_LEFT_CHANNEL = 1
	REAR_LEFT_CHANNEL = 2
	FRONT_RIGHT_CHANNEL = 3
	REAR_RIGHT_CHANNEL= 4

	def robotInit(self):

		self.front_left_motor = ctre.WPI_TalonSRX(FRONT_LEFT_CHANNEL)
		self.rear_left_motor = ctre.WPI_TalonSRX(REAR_LEFT_CHANNEL)
		#left = wpilib.SpeedControllerGroup(self.left1, self.left2)

		self.front_right_motor = ctre.WPI_TalonSRX(FRONT_RIGHT_CHANNEL)
		self.rear_right_motor = ctre.WPI_TalonSRX(REAR_RIGHT_CHANNEL)
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
		while self.isOperatorCOntrol() and self.isEnabled():
			self.drive.driveCartesian(
				self.driver.getX(),
				self.driver.getY(),
				self.driver.getZ(), 
				0)

			wpilib.Timer.delay(0.005) 


	def robotPeriodic(self):
		print("Test")

	def teleopInit(self):
		self.left_activated = False
		self.right_activated = False
		print ("TELEOP BEGIN")
		self.forward = 0

	def teleopPeriodic(self):
		deadzone = 0.2
		max_acceleration = 0.3
		goal_forward = -self.driver.getY(RIGHT)
		rotate = self.driver.getX(LEFT)

		max_forward = 1.0
		max_rotate = 1.0

		goal_forward = deadzone(goal_forward * max_forward, deadzone)
		rotate = deadzone(rotate * max_rotate, deadzone)

		alpha = goal_forward - self.forward

		if abs(alpha) < max_acceleration:
			self.forward += alpha
		else: 
			self.forward += max_acceleration * sign(delta)

		if self.driver.getXButton():
			self.drivetrain.stop()
		else:
			self.drivetrain.drive_Cartesian(self.ySpeed, self.xSpeed, self.zRotation, gyroAngle = 0.0)


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


if _name_ == "__main__":
	wpilib.run(Robot, physics_enabled = True)


