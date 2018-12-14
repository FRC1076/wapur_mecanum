import wpilib 
import ctre
import robotpy_ext.common_drivers.navx as navx
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
		self.gyro = navx.ahrs.AHRS.create_spi()

		self.drivetrain = Drivetrain(self.front_left_motor, self.rear_left_motor, self.front_right_motor, self.rear_right_motor)
		
		self.driver = wpilib.XboxController(0)
        self.operator = wpilib.XboxController(1)

		self.grabber = Grabber(ctre.WPI_TalonSRX(GRABBER_ID)) 

		elevator1 = ctre.WPI_TalonSRX(ELEVATOR1_ID)
		elevator2 = ctre.WPI_TalonSRX(ELEVATOR2_ID)
		self.elevator = Elevator(wpilib.SpeedControllerGroup(elevator1, elevator2))

		
		elevator1 = ctre.WPI_TalonSRX(ELEVATOR1_ID)
		elevator2 = ctre.WPI_TalonSRX(ELEVATOR2_ID)
		self.elevator = Elevator(
			wpilib.SpeedControllerGroup(elevator1, elevator2))
		
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
		print("Test")

	def teleopInit(self):
		self.left_activated = False
		self.right_activated = False
		print ("TELEOP BEGIN")
		self.yDist = 0

	def teleopPeriodic(self):
		deadzone = 0.2
		max_acceleration = 0.3
		# driver controls
		ySpeed = self.driver.getY(RIGHT)
		xSpeed = self.driver.getX(RIGHT)

		zRotation = self.driver.getX(LEFT)

		max_ySpeed = 1.0
		max_xSpeed = 1.0

		yForward = deadzone(yForward * max_ySpeed, deadzone)
		xDistance = deadzone(xDistance * max_xSpeed, deadzone)

		delta = yForward - self.yDist

		if abs(delta) < max_acceleration:
			self.yDist += delta
		else: 
			self.yDist += max_acceleration * sign(delta)

		# operator controls
		elevatorZ = self.operator.getTriggerAxis(RIGHT)
		spit = self.operator.getTriggerAxis(LEFT)

		TRIGGER_LEVEL = 0.35

		if abs(elevatorZ) > TRIGGER_LEVEL:
			self.elevator.go_up(elevatorZ)
		elif abs(spit) > TRIGGER_LEVEL:
			self.elevator.go_down(spit)
		else: 
			self.elevator.stop()

		#intake
		left_stick = -deadzone(self.operator.getY(LEFT), INTAKE_DEADZONE)
        right_stick = -deadzone(self.operator.getY(RIGHT), INTAKE_DEADZONE)
        self.grabber.set_left(left_stick * 0.5)
        self.grabber.set_right(right_stick * 0.5)

	
		if self.driver.getXButton():
			self.drivetrain.stop()
		else:
			self.drivetrain.drive_Cartesian(ySpeed, xSpeed, zRotation, gyroAngle = 0.0)


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


