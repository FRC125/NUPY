import wpilib


class MultiMotor:

    def __init__(self,*ports):
        self.ports = ports
        self.motors = []
        for port in self.ports:
            self.motors.append(wpilib.Talon(port))

    def set(self,power):
        for motor in self.motors:
            motor.set(power)
