import wpilib


class Elevator(wpilib.command.Subsystem):
    def initDefaultCommand(self):
        pass

    def at_bottom(self):
        return Robot.bottom_limitswitch.get()

    def at_top(self):
        return Robot.top_limitswitch.get()

    def elevator_up(self):
        if self.at_top():
            Robot.elevator_motor.set(0)
        else:
            Robot.elevator_motor.set(-1)

    def elevator_down(self):
        if self.at_bottom:
            Robot.elevator_motor.set(0)
        else:
            Robot.elevator_motor.set(1)
