import wpilib 
from wpilib.drive import MecanumDrive
import autonomous

LEFT = GenericHID.Hand.kLeft
RIGHT = GenericHID.Hand.kRight



class Robot(wpilib.IterativeRobot):

	#channels on the roborio that the motor controllers are plugged into
	FRONT_LEFT_CHANNEL = 1
	REAR_LEFT_CHANNEL = 2
	FRONT_RIGHT_CHANNEL = 3
	REAR_RIGHT_CHANNEL= 4

	def robotInit(self):
		
		subsystems.init()

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


		# if self.driver.getXButton():
		# 	self.drivetrain.stop()
		# else
		# 	self.drivetrain.

	def autonomousInit(self):
		print("AUTONOMOUS BEGIN")

		self.auton = autonomous.straight(
			self.drivetrain)

	def autonomousPeriodic(self):
		try:
			next(self.auton)
		except StopIteration:
			self.drivetrain.stop()

def deadzone(val, deadzone):
	if abs(val) < deadzone:
		return 0
	return val



if _name_ == "__main__":
	wpilib.run(Robot, physics_enabled = True)


