import wpilib
from wpilib.command import Command
from nutrons import Robot



class ElevatorCmd(wpilib.command.Command):
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

class IntakeCmd(wpilib.command.Command):
    def __init__(self):
        wpilib.command.Command.__init__(self)
        self.requires(Robot.intake)
    def initialize(self):
        pass

    def execute(self):
        if Robot.twstick.getRawButton(4):
            Robot.intake.open_intake_wheels(self)
        if Robot.twstick.getRawButton(5):
            Robot.intake.close_intake_wheels(self)
        if Robot.twstick.getRawButton(6):
            Robot.intake.spin_intake_wheels(self)
        if Robot.twstick.getRawButton(7):
            Robot.intake.spit_intake_wheels(self)
        if Robot.twstick.getRawButton(7):
            Robot.intake.stop_intake_wheels(self)
