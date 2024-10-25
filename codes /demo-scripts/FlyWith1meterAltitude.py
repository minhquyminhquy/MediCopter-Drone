# High flying drone
 
from dronekit import connect, VehicleMode , LocationGlobal , LocationGlobalRelative
import time  
import dronekit_sitl  
from pymavlink import mavutil 

connecting_string = "/dev/ttyACM0" 
baud = 57600 
vehicle = connect(connecting_string,baud,wait_ready=True) 

def arm_and_takeoff(h):

    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)
    print("Arming motors")

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Takeoff")
    vehicle.simple_takeoff(h)  

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= h * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

    return None 

def fly_to_mission_point(e): 
    vehicle.airspeed = 1 
    vehicle.simple_goto(e) 
    time.sleep(1)
    vehicle.mode = VehicleMode("LAND")
    


def get_parameter(): 
    print("version", vehicle.version )
    print("Global location", vehicle.location.global_frame) 
    print("battery", vehicle.battery) 
    print("Mode", vehicle.mode.name)   
    print("armed ", vehicle.armed)
    

# get to run in raspberry pi 

#array_point = [] 
#a = int(input(" How many points do you want ? : ")) 
#for k in range(a) : 
#         dlat = float(input(" Input dlat : ")) 
#         dlon = float(input(" Input dlon : "))
#         location_input = LocationGlobalRelative(dlat,dlon) 
#         array_point.append(location_input)  
epoint = LocationGlobalRelative(10.804897966546946, 106.71652619465362,1)
get_parameter() 
time.sleep(2)
arm_and_takeoff(1)
fly_to_mission_point(epoint) 

