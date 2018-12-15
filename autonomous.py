import math
import time
import wpilib


def straight_ahead(drivetrain):
    yield from Timed(MecanumAutonomous(drivetrain), duration = 5).run()

class BaseAutonomous:
    def init(self):
        return self

    def execute(self):
        pass

    def end(self):
        pass

    def run(self):
        def _execute():
            yield from self.execute()
            self.end()
            self.init()
        return _execute()

class Timed(BaseAutonomous):
    def __init__(self, auto, duration):
        self.auto = auto
        self.duration = duration
        self.auto.init()
        self.end_time = time.time() + self.duration

    def execute(self):
        for _ in self.auto.execute():
            if time.time() > self.end_time:
                print("TIMED OUT!")
                break
            yield

    def end(self):
        self.auto.end()


class MecanumAutonomous(BaseAutonomous):
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain

    def execute(self):
        while True:
            self.drivetrain.drive_Cartesian(1, 0, 0)
            yield

    def end(self):
        self.drivetrain.stop()
