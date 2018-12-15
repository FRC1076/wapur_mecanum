import sys 
sys.path.append("C:/Users/biaoh/Desktop/1076 Software/wapur_mecanum/wapur_mecanum")

from helper import GetSet
from subsystems import elevator as Elevator
def test_elevator():
    motor = GetSet(0)
    elevator = Elevator(motor)

    elevator.go_up()
    assert motor.state == 1
    elevator.go_up(speed=0.5)
    assert motor.state == 0.5

    elevator.go_down()
    assert motor.state == -1
    elevator.go_down(speed=0.5)
    assert motor.state == -0.5
