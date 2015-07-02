import wpilib

from wpilib.command import Command
from nutrons import Robot


class Auto_drive(wpilib.command.Command):

    def __init__(self):
        wpilib.command.Command.__init__(self)
        self.requires(Robot.dt)

    def initialize(self):
        print("Initializing.")

    def execute(self):
        Robot.dt.drive_TWH(0.5, 0.0, 0.0)
        if Robot.encoder.get() > 10:
            Robot.dt.drive_TWH(0.0, 0.0, 0.0)

    def isFinished(self):
        return Robot.encoder.get() > 10
