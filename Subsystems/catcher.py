import wpilib 

class Grabber: 
	""" 
	Grabber catches the ball and has a mechanism to release ball 

	"""
	def __init__(self, left, right):
		self.left_motor = left
		self.right_motor = right

	def set(self, speed=1.0):
        self.set_left(speed)
        self.set_right(speed)

    def set_left(self, speed=1.0):
        self.left_motor.set(-speed)

    def set_right(self, speed=1.0):
        self.right_motor.set(-speed)

  