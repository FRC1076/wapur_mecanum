import wpilib 

class Grabber: 
	""" 
	Grabber catches the ball and has a mechanism to release ball 

	"""
	def __init__(self, motor):
		self.motor = motor


	def setSpeed(self, speed=1.0):
        self.motor.set(speed)


    # def set_left(self, speed=1.0):
    #     self.left_motor.set(-speed)

    # def set_right(self, speed=1.0):
    #     self.right_motor.set(-speed)

  