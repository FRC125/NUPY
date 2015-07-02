import wpilib
from wpilib import buttons


class OI:
    """
        This class is the glue that binds the controls on the
        physical operatorinterface to the commands and command
        groups that allow control of the robot.
    """

    def __init__(self, robot):
        self.robot = robot
