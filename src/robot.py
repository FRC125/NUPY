#!/usr/bin/env python3

import wpilib


class MultiMotor:
    def __init__(self,*ports):
        self.ports = ports
        self.motors = []
        for port in self.ports:
            self.motors.append(wpilib.Jaguar(port))
    def set(self,power):
        for motor in self.motors:
            motor.set(power)
class DriveTrain(wpilib.command.Subsystem):
    def initDefaultCommand(self):
        self.setDefaultCommand(DriveCmd())
        #self.logger.info("Setting default")
    def driveTWH(self,throttle,wheel,h):
        (left,right,h) = h_drive(throttle,wheel,h)        
        Robot.left_drive.set(-left)
        Robot.right_drive.set(right)
        Robot.h_motor.set(h)
    def driveLRH(self,left,right,h):
        Robot.left_drive.set(-left)
        Robot.right_drive.set(right)
        Robot.h_motor.set(h)
class NutronsRobot:
    def __init__(self):
        pass
Robot = NutronsRobot()
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
class MyRobot(wpilib.IterativeRobot):
    '''Main robot class'''
    
    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        Robot.dt = DriveTrain()
                
        Robot.twstick = wpilib.Joystick(1)
        Robot.hstick = wpilib.Joystick(2)
        Robot.left_drive = MultiMotor(4)
        Robot.right_drive = MultiMotor(3)
        Robot.h_motor = MultiMotor(2)
        self.auto_steps = 0
    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        pass
    def autonomousPeriodic(self):
        '''Called every 20ms in autonomous mode'''
        wpilib.command.Scheduler.getInstance().run()
        self.auto_steps += 1
    def disabledInit(self):
        '''Called only at the beginning of disabled mode'''
        pass
    
    def disabledPeriodic(self):
        '''Called every 20ms in disabled mode'''
        pass

    def teleopInit(self):
        '''Called only at the beginning of teleoperated mode'''
        pass

    def teleopPeriodic(self):
        '''Called every 20ms in teleoperated mode'''
        wpilib.command.Scheduler.getInstance().run()
        #Robot.dt.setCurrentCommand(DriveCmd())
        # Move a motor with a Joystick
        #self.motor.set(self.lstick.getY())
        
def h_drive(throttle,wheel,y):
    ''' Return a left , right, h tripple '''
    left = throttle - wheel
    right = throttle + wheel
    h = y
    return (left,right,h)
if __name__ == '__main__':
    wpilib.run(MyRobot,physics_enabled=True)

