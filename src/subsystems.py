import wpilib
from utils import MultiMotor
from nutrons import Robot
from commands import DriveCmd
from math import sin, cos, radians
import imu
class DriveTrain(wpilib.command.Subsystem):
    
    def initDefaultCommand(self):
        self.setDefaultCommand(DriveCmd())
        self.gyro = imu.ImuGyro()
        #self.logger.info("Setting default")
    def driveTWH(self,throttle,wheel,h):
        '''Takes a speed, a turn-ratio, and an h-wheel and sets each motor'''
        (left,right,h) = self.h_drive(throttle,wheel,h)        
        Robot.left_drive.set(-left)
        Robot.right_drive.set(right)
        Robot.h_motor.set(h)
    def driveLRH(self,left,right,h):
        '''Takes a left motor, right motor, and h-wheel, and sets each motor'''
        Robot.left_drive.set(-left)
        Robot.right_drive.set(right)
        Robot.h_motor.set(h)
    def h_drive(self,throttle,wheel,y):
        '''Return a left , right, h tripple '''
        left = throttle - wheel
        right = throttle + wheel
        h = y
        return (left,right,h)
    def get_field_centric(self, theta, forward, right):
        '''Takes field centric values and returns and sets the values'''
        theta = radians(theta)
        temp = forward*cos(theta) + right*sin(theta)
        right = -forward*sin(theta) + right*cos(theta)
        forward = temp
        forward_1 = forward
        right_1 = right
        return (forward_1, right_1)
    def drive_field_centric(self, forward, right):
        '''Takes a speed forward and a speed for the h drive and sets the motors accordingly'''
        theta = self.gyro.getAngle()
        forward, right = self.get_field_centric(theta, forward, right)
        self.driveTWH(forward, 0, right)

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





