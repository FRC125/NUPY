import wpilib
from wpilib.command import Command
from nutrons import Robot

class DriveCmd(wpilib.command.Command):
    def __init__(self):
        wpilib.command.Command.__init__(self)
        self.requires(Robot.dt)
    def initialize(self):
        print("Initializing.")
        
    def execute(self):
        T = Robot.twstick.getRawAxis(1)
        W = Robot.twstick.getRawAxis(5)
        H = Robot.hstick.getRawAxis(0)
        Robot.dt.driveTWH(T,W,H)
        #print("in execute()")
    def isFinished(self):
        return False