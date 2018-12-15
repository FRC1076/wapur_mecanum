import wpilib

class Grabber:
	"""
	Grabber catches the ball and has a mechanism to release ball

	"""
	def __init__(self, motor):
		self.motor = motor

	def set(self, speed=1.0):
		self.motor.set(-speed)
