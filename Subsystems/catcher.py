import wpilib 

class Grabber: 
	""" 
	Grabber catches the ball and has a mechanism to release ball 
	with pneumatics.
	"""
	def __init__(self, motor):
		self.motor = motor

	def eject(self, speed = 1.0):
		self.motor.set(speed)

	def reset(self, speed = -1.0):
		self.motor.set(speed)

	def stop(self):
		self.motor.set(0)