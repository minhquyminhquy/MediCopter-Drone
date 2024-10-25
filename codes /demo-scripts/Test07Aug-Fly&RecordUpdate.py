# High flying drone
 
from dronekit import connect, VehicleMode , LocationGlobal , LocationGlobalRelative
import time  
import dronekit_sitl  
from pymavlink import mavutil 
import cv2
#INITIALIZE VIDEO
video_capture = cv2.VideoCapture(0) 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output2.avi', fourcc, 20.0, (640, 480))
#INITIALIZE DRONE
connecting_string = "/dev/ttyACM0" 
baud = 57600 
vehicle = connect(connecting_string,baud,wait_ready=True) 
#FLYING STATES
Landing = False
arm_and_takeoff_state = False
Finish_arm_and_takeoff = False
Landed = False
Landing = False



def arm_and_takeoff(h):
    global arm_and_takeoff_state, Finish_arm_and_takeoff, output_file, video_capture
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
    print("Arming motors")

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    arm_and_takeoff_state = True

    print("TAKEOFF")

    vehicle.simple_takeoff(h)  


    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        ret, frame = video_capture.read()
        if ret:
            frame = cv2.flip(frame, 0)
            output_file.write(frame)
        if vehicle.location.global_relative_frame.alt >= h * 0.95:
            print("Reached target altitude")
            Finish_arm_and_takeoff = True
            break      
        

    return None 

def is_at_target_location():
    global current_latitude, current_longitude
    current_latitude = vehicle.location.global_frame.lat
    current_longitude = vehicle.location.global_frame.lon
    distance_to_target = vehicle.location.global_frame.distance_to_location_global(target_latitude, target_longitude)

    return distance_to_target <= threshold_distance

def fly_to_mission_point(array_point): 
    global Landed, output_file, video_capture
    vehicle.airspeed = 0.5
    vehicle.groundspeed = 0.5
    
    for point in array_point :  
        vehicle.simple_goto(point) 
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
    print("version", vehicle.version )
    print("Global location", vehicle.location.global_frame) 
    print("battery", vehicle.battery)  
    print("Mode", vehicle.mode.name) 
    print("armed ", vehicle.armed)
    

# get to run in raspberry pi 
array_point = []
point1 = LocationGlobalRelative(10.80491722128159, 106.71654397535926)
point2 = LocationGlobalRelative(10.804956868705531, 106.7167913159932,2) 
array_point.append(point2)

target_latitude = 10.804956868705531  # Target latitude in degrees
target_longitude = 106.7167913159932  # Target longitude in degrees
threshold_distance = 2  # Threshold distance in meters

get_parameter() 
time.sleep(2)





while True:
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.flip(frame, 0)
        output_file.write(frame)
    
    if arm_and_takeoff_state == False:
        arm_and_takeoff(2)

    if Finish_arm_and_takeoff == True :
        fly_to_mission_point(array_point)

    if Landed:
        break

video_capture.release()
output_file.release()





