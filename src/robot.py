import wpilib

from nutrons import Robot
from wpilib import DigitalInput
from wpilib import Encoder
from utils.multi_motor import Multi_motor
from networktables import NetworkTable
from subsystems.drive_train import Drive_train
from subsystems.elevator import Elevator
from subsystems.intake import Intake
from autonomous.test_auton import AutonDrive


class MyRobot(wpilib.IterativeRobot):
    '''Main robot class'''

    def robotInit(self):
        '''Robot-wide initialization code should go here'''
        self.sd = NetworkTable.getTable('SmartDashboard')
        self.i = 0
        Robot.dt = Drive_train()
        Robot.elevator = Elevator()
        Robot.intake = Intake()
        Robot.twstick = wpilib.Joystick(1)
        Robot.hstick = wpilib.Joystick(2)
        Robot.left_drive = Multi_motor(4)
        Robot.right_drive = Multi_motor(3)
        Robot.h_motor = Multi_motor(2)
        Robot.elevator_motor = Multi_motor(5)
        Robot.top_limitswitch = DigitalInput(2)
        Robot.bottom_limitswitch = DigitalInput(1)
        Robot.solenoid = wpilib.DoubleSolenoid(7, 0)
        Robot.intake_motor = Multi_motor(0)
        Robot.encoder = Encoder(3,4)


        self.autonomous_command = AutonDrive()
        self.auto_steps = 0

    def autonomousInit(self):
        '''Called only at the beginning of autonomous mode'''
        self.autonomous_command.start()

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

        if self.i%100 ==0:
            self.sd.putDouble('Gypro', Robot.dt.get_gyro_angle())
        self.i+= 1
        # Move a motor with a Joystick
        #self.motor.set(self.lstick.getY())

if __name__ == '__main__':
    wpilib.run(MyRobot,physics_enabled=True)
