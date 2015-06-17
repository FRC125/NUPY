import os.path
class ImuGyro:
    def __init__(self):
        if os.path.isfile('/dev/ttyACM0'):
            self.port = open('/dev/ttyACM0')
        else:
            self.port = None
    def get_yaw(self):
        if self.port:
            line = self.port.readline()
            return float(line[3:9])
        return -1
        ## '!y-yaw.00 etc'
    def getAngle(self):
        return self.get_yaw()
