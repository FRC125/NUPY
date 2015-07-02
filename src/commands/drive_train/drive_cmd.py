import wpilib

from nutrons import Robot


class Drive_cmd(wpilib.command.Command):

    def __init__(self):
        wpilib.command.Command.__init__(self)
        self.requires(Robot.dt)

    def initialize(self):
        print("Initializing.")

    def execute(self):
        T = Robot.twstick.getRawAxis(1)
        W = Robot.twstick.getRawAxis(5)
        H = Robot.twstick.getRawAxis(0)
        if Robot.twstick.getRawButton(1):
            Robot.dt.drive_field_centric(T, H)
        Robot.dt.drive_TWH(T, W, H)

    def isFinished(self):
        return False
