import wpilib


class Intake(wpilib.command.Subsystem):

    def initDefaultCommand(self):
        pass

    def open_intake_wheels(self):
        Robot.solenoid.set(True)

    def close_intake_wheels(self):
        Robot.solenoid.set(False)

    def spin_intake_wheels(self):
        Robot.intake_motor.set(-1)

    def spit_intake_wheels(self):
        Robot.intake_motor.set(1)

    def stop_intake_wheels(self):
        Robot.intake_motor.set(0)
