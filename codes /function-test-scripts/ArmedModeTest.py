from dronekit import connect, VehicleMode , LocationGlobal , LocationGlobalRelative
import time  
import dronekit_sitl  
from pymavlink import mavutil 

connecting_string = "/dev/ttyACM0" 
baud = 57600 
vehicle = connect(connecting_string,baud=baud,wait_ready=True, timeout=500) 

def arm():
    print("Mode is", vehicle.mode.name) 
    vehicle.mode = VehicleMode("GUIDED")
    print("Mode is", vehicle.mode.name)
    while vehicle.is_armable != True: 
        print(" waiting to armable ") 
        time.sleep(1) 
    print(" vehicle is armable ") 

    vehicle.mode = VehicleMode("GUIDED") 
    while vehicle.mode != "GUIDED" : 
        print("waiting for vehiclemode") 
        time.sleep(1) 
    print("Ok vehicel mode ") 

    vehicle.arm = True 
    while vehicle.armed == False : 
        print(" Not connect arm") 
        time.sleep(1) 
    print(" Gud Gud Arm") 
    time.sleep(3) 

    return None 

def get_parameter(): 
    print("version", vehicle.version )
    print("Global location", vehicle.location.global_frame) 
    print("battery", vehicle.battery) 
    print("atitude", vehicle.atitude) 
    print("Mode", vehicle.mode.name)
    print("GPS", vehicle.GPS_0) 


# def takeoff(h) : 
  #  vehicle.simple_takeoff(h) 
     # while True : 
       # atitude_real = vehicle.location.global_relative_frame.alt 
        # print("atitude", str(atitude_real))  



# get to run in raspberry pi 

arm()
time.sleep(3)
get_parameter() 
