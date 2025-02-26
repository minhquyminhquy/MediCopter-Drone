"""
This script instructs the drone to take off, fly to target position, and land. 
Meanwhile recording the journey with the camera infront.
Demo day: 07 Aug 2023
"""
 
from dronekit import connect, VehicleMode , LocationGlobal , LocationGlobalRelative
import time  
import dronekit_sitl  
from pymavlink import mavutil 
import cv2

# INITIALIZE VIDEO CAPTURE
video_capture = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output2.avi', fourcc, 20.0, (640, 480))

# INITIALIZE DRONE VEHICLE
connecting_string = "/dev/ttyACM0" 
baud = 57600 
vehicle = connect(connecting_string,baud,wait_ready=True) 

# FLYING STATES
IS_ARMING_AND_TAKING_OFF = False
HAS_FINISHED_ARMING_AND_TAKEOFF = False
HAS_LANDED = False

# FLYING PARAMS
THRESHOLD_DISTANCE = 2  

def arm_and_takeoff(target_alt):
    """This script instruct the drone to arm and takeoff"""
    global IS_ARMING_AND_TAKING_OFF, HAS_FINISHED_ARMING_AND_TAKEOFF, output_file, video_capture

    # Check whether arming is possible, if not, waiting drone to initialize
    while not vehicle.is_armable:
        print("Waiting for vehicle to initialize...")
        time.sleep(1)

    # Arm the drone
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Trying to arm...")
        time.sleep(1)
        vehicle.armed = True

    print("Motors already armed")

    IS_ARMING_AND_TAKING_OFF = True

    print("Vehicle taking off")

    vehicle.simple_takeoff(h)  

    while True:
        print(f"Altitude: {vehicle.location.global_relative_frame.alt:3f}m")

        # Write the frame into the video
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.flip(frame, 0)
            output_file.write(frame)

        # If reach desired altitude, stop ascending
        if vehicle.location.global_relative_frame.alt >= target_alt * 0.95:
            print("Reached target altitude")
            HAS_FINISHED_ARMING_AND_TAKEOFF = True
            break      
        
    return None 

def is_at_target_location(target_pos):
    """Check if the drone has reached the target position or not"""
    target_latitutude = target_pos[0]
    target_longitude = target_pos[1]
    distance_to_target = vehicle.location.global_frame.distance_to_location_global(target_latitutude
                                                                                   ,target_longitude)
    return distance_to_target <= THRESHOLD_DISTANCE

def fly_to_mission_point(target_point, air_speed, ground_speed): 
    """Guide the drone to fly to a target point."""
    global HAS_LANDED, output_file, video_capture

    # setup the speed
    vehicle.airspeed = 0.5
    vehicle.groundspeed = 0.5 # account for wind speed
    
    vehicle.simple_goto(target_point) 
    while True:
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.flip(frame, 0)
            output_file.write(frame)
        ##LAND
        if is_at_target_location():
            
            print("Reach target location")
            vehicle.mode = VehicleMode("LAND") 
            while True:
                ret, frame = video_capture.read()
                if ret:
                    frame = cv2.flip(frame, 0)
                    output_file.write(frame)
                if vehicle.location.global_relative_frame.alt <= 0.05:
                    Landed = True
                    break
            
                else:
                    print("Have not reached target location yet")
            break
   



def get_parameter():
    """Print vehicle parameters"""
    print(f"Version: {vehicle.version}")
    print(f"Global Location: {vehicle.location.global_frame}")
    print(f"Battery: {vehicle.battery}")
    print(f"Mode: {vehicle.mode.name}")
    print(f"Armed State: {vehicle.armed}")

def main():
    # Fly params

    # Start position: Brush #1
    point1 = LocationGlobalRelative(10.80491722128159, 106.71654397535926)
    # Target position: Bush #2
    point2 = LocationGlobalRelative(10.804956868705531, 106.7167913159932) 

    # Retrieve the preflight info
    get_parameter()
    time.sleep(2)

    while True:

        ret, frame = video_capture.read()
        if ret:
            frame = cv2.flip(frame, 0)
            output_file.write(frame)
        
        if IS_ARMING_AND_TAKING_OFF == False:
            arm_and_takeoff(2)

        if HAS_FINISHED_ARMING_AND_TAKEOFF == True :
            fly_to_mission_point(array_point, air_speed=0.5, ground_speed=0.5)

        if HAS_LANDED:
            break

    video_capture.release()
    output_file.release()

if __name__ == "__main__":
    main()



