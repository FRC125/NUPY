#!/usr/bin/env python3

import wpilib


from utils import MultiMotor
from subsystems import DriveTrain
from commands import DriveCmd
from nutrons import Robot


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

        # Move a motor with a Joystick
        #self.motor.set(self.lstick.getY())

if __name__ == '__main__':
    wpilib.run(MyRobot,physics_enabled=True)
