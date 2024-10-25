#  TEST FILEBASE  

from dronekit import connect, VehicleMode , LocationGlobal , LocationGlobalRelative
import time  
import dronekit_sitl    
from pymavlink import mavutil 
from gpiozero import Servo
import cv2  
import pyrebase 
import subprocess
servo_pin1 = 17
servo_pin2 = 18
servo1 = Servo(servo_pin1) 
servo2 = Servo(servo_pin2)
connecting_string = "/dev/ttyACM0" 
baud = 57600 
subprocess.Popen(["python","connectcamera.py"])
vehicle = connect(connecting_string,baud,wait_ready=True) 



config = {
  "apiKey": "AIzaSyBi24u8OlLlesdg_g_w4XfZuwttWCwHnSw",
  "authDomain": "droneai-c394f.firebaseapp.com",
  "databaseURL": "https://droneai-c394f-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId" : "droneai-c394f",
  "storageBucket" : "droneai-c394f.appspot.com",
  "messagingSenderId" : "1043958961590",
  "appId" : "1:1043958961590:web:318bf9d30904beeee3dd17",
  "measurementId" : "G-JFZ5YSZSVE"
} 

firebase = pyrebase.initialize_app(config)
db = firebase.database()
def set_position_servo(): 
     '''servo_pin1 = 17
     servo_pin2 = 18
     servo1 = Servo(servo_pin1)
     servo2 = Servo(servo_pin2)'''
     pos = (180/180) * 2 - 1
     back_pos = (10/180) * 2 -1 
     servo1.value = back_pos 
     servo2.value = pos
     time.sleep(0.5) 
     servo1.value = pos
     servo2.value = back_pos
     time.sleep(0.5)

def filebase_data():
    Lat = vehicle.location.global_frame.lat 
    Lon = vehicle.location.global_frame.lon
    Data = {"LAT": Lat, "LNG": Lon}
    db.update(Data)

def camera(): 
    global video_capture , output_file
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.flip(frame, 0)
        output_file.write(frame)


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
        #camera()
        filebase_data() 
        if vehicle.location.global_relative_frame.alt >= h * 0.95:
            print("Reached target altitude")
            set_position_servo()
            time.sleep(2)
            break
            
        time.sleep(1)

    return None 

arm_and_takeoff(2)
vehicle.mode = VehicleMode("LAND")
