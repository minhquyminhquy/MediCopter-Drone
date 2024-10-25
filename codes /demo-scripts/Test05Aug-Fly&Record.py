# CODE FLY DRONE BASIC 
from dronekit import connect, VehicleMode , LocationGlobal , LocationGlobalRelative
import time  
import dronekit_sitl  
from pymavlink import mavutil  
from gpiozero import Servo
import cv2


servo_pin1 = 17
servo_pin2 = 18
servo1 = Servo(servo_pin1) 
servo2 = Servo(servo_pin2)


connecting_string = "/dev/ttyACM0" 
baud = 57600 
vehicle = connect(connecting_string,baud,wait_ready=True) 

def arm_and_takeoff(h):
    #RECORD VIDEO
    video_capture = cv2.VideoCapture(0)  # Use 0 for the default camera

    # Define the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_file = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640, 480))
    #--------------------------------


    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
    print("Arming motors")
    
    
    vehicle.mode = VehicleMode("GUIDED") 
    while vehicle.mode != "GUIDED":
        print("Fail mode ")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Takeoff")
    vehicle.simple_takeoff(h)  



    while True:
        #record
        ret, frame = video_capture.read()

        # If the frame was read successfully
        if ret:
            # Display the frame
            #cv2.imshow('Video', frame)
            frame = cv2.flip(frame, 0)
            # Write the frame to the output file
            output_file.write(frame)

        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= h * 0.95:
            print("Reached target altitude")
            break
        #time.sleep(1) 

    video_capture.release()
    output_file.release()
    

    return None 
def set_position_servo(): 
     pos = (45/180) * 2 - 1
     servo1.value = pos  
     servo2.value = pos
     time.sleep(1) 
     back_pos = (150/180) * 2 - 1
     servo1.value = back_pos
     servo2.value = back_pos  
     time.sleep(0.5)


def get_parameter(): 
    print("version", vehicle.version )
    print("Global location", vehicle.location.global_frame) 
    print("battery", vehicle.battery) 
    print("Mode", vehicle.mode.name)
    print("armed ", vehicle.armed)
def land():
    vehicle.mode = VehicleMode("LAND")   

# get to run in raspberry pi 
get_parameter() 
time.sleep(2)
arm_and_takeoff(2)
set_position_servo()
land()






