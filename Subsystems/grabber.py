import wpilib 

class Grabber:

    def __init__(self, motor):
        self.motor = motor


    def set_motor(self, speed = 1.0):
        self.motor.set(-speed)