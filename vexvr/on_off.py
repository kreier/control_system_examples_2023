#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vr import *

# Brain should be defined by default
brain = Brain()

drivetrain = Drivetrain("drivetrain", 0)
pen = Pen("pen", 8)
pen.set_pen_width(THIN)
left_bumper = Bumper("leftBumper", 2)
right_bumper = Bumper("rightBumper", 3)
front_eye = EyeSensor("frontEye", 4)
down_eye = EyeSensor("downEye", 5)
front_distance = Distance("frontdistance", 6)
distance = front_distance
magnet = Electromagnet("magnet", 7)
location = Location("location", 9)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:      2023/02/22
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

def driveControlOnOff(duration):
    setpoint = 0
    speed = 100
    # reset the timer
    brain.timer_reset()
    # begin algorithm to drive straight to the position of y = 0

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        if( currentYLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)


# Add project code in "main"
def main():
    driveControlOnOff(5)
    drivetrain.turn_to_heading(90, DEGREES)


# VR threads — Do not delete
vr_thread(main())
