import wpilib

from nutrons import Robot


class Elevator_cmd(wpilib.command.Command):

    def __init__(self):
        wpilib.command.Command.__init__(self)
        self.requires(Robot.elevator)

    def initialize(self):
        pass

    def execute(self):
        if Robot.twstick.getRawButton(2):
            Robot.elevator.elevator_up()
        if Robot.twstick.getRawButton(3):
            Robot.elevator.elevator_down()

    def isFinished(self):
        return False
