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

def driveXDistance(setpoint,duration):
  
    maxSpeed = 100
    k = 1
    # reset the timer
    brain.timer_reset()
    # begin algorithm to drive straight to the setpoint position in X

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        output = k*error
        # Ensure the output is not more than the maximum speed
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)
        # Set the direction of movement
        
        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

# Add project code in "main"
def main():
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,4)   

# VR threads — Do not delete
vr_thread(main())
