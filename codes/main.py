import json
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time  
import cv2 
import pyrebase
from geopy.distance import geodesic 
import random  # Used for simulating obstacle detection

# Load configuration from JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

# Constants from config
CONNECTING_STRING = config['connection']['connecting_string']
BAUD_RATE = config['connection']['baud_rate']

# Firebase Configuration
FIREBASE_CONFIG = config['firebase']

# Initialize Vehicle
vehicle = connect(CONNECTING_STRING, BAUD_RATE, wait_ready=True)  
firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()

def update_firebase_location():
    """Update the drone's current latitude and longitude to Firebase."""
    lat = vehicle.location.global_frame.lat 
    lon = vehicle.location.global_frame.lon
    data = {"LAT": lat, "LNG": lon}
    db.update(data)

def capture_camera_frame(video_capture, output_file): 
    """Capture a frame from the camera and write it to the output file."""
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.flip(frame, 0)
        output_file.write(frame)

def arm_and_takeoff(target_altitude):
    """Arm the drone and take off to the specified altitude."""
    while not vehicle.is_armable:
        print("Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Taking off...")
    vehicle.simple_takeoff(target_altitude)  

    while True:
        print("Altitude: ", vehicle.location.global_relative_frame.alt)
        update_firebase_location()
        if vehicle.location.global_relative_frame.alt >= target_altitude * 0.95:
            print("Reached target altitude")
            break

def fly_to_target(latitude, longitude):         
    """Fly the drone to the specified latitude and longitude."""
    vehicle.airspeed = 10  # Set the speed during the flight
    altitude = 30  # Set the desired altitude during the flight
    target_point = LocationGlobalRelative(latitude, longitude, altitude) 
    vehicle.simple_goto(target_point) 

    while True:
        # Get the current location
        current_location = vehicle.location.global_relative_frame
        current_latitude = current_location.lat
        current_longitude = current_location.lon
        current_point = (current_latitude, current_longitude)

        # Calculate the remaining distance to the target point
        remaining_distance = geodesic(current_point, target_point).meters

        update_firebase_location()  # Update Firebase with current location

        if remaining_distance < 0.25:
            print("Drone reached target location")
            break

        time.sleep(1)  # Sleep to prevent rapid looping

def land(): 
    """Land the drone safely."""
    vehicle.mode = VehicleMode("LAND")
    while True: 
        update_firebase_location() 
        altitude = vehicle.location.global_frame.alt
        if altitude < 0.2:
            print("Drone is on the ground")
            break 

def return_to_launch(): 
    """Return the drone to its launch point."""
    vehicle.mode = VehicleMode('RTL') 
    while True: 
        update_firebase_location() 
        altitude = vehicle.location.global_frame.alt
        if altitude < 0.2:
            print("Drone landed safely")
            break 

def print_drone_parameters():      
    """Print the current parameters of the drone."""
    print("DRONE STATUS:")
    print("1. Firmware Version:", vehicle.version)
    print("2. Global location:", vehicle.location.global_frame) 
    print("3. Battery:", vehicle.battery)  
    print("4. Mode:", vehicle.mode.name) 
    print("5. Armed Status:", vehicle.armed)

def monitor_battery():
    """Monitor the drone's battery status."""
    battery = vehicle.battery
    print("Battery Voltage: {}V".format(battery.voltage))
    print("Battery Level: {}%".format(battery.level))

    if battery.level < 20:
        print("Warning: Low battery! Returning to launch.")
        return_to_launch()

def check_for_obstacles():
    """Simulate obstacle detection. In a real scenario, replace this with actual sensor data."""
    obstacle_detected = random.choice([True, False])
    if obstacle_detected:
        print("Obstacle detected! Taking evasive action.")
        # Simple evasive maneuver: fly up and then return to original path
        vehicle.simple_takeoff(10)  # Ascend to 10 meters
        time.sleep(5)
        return_to_launch()

def create_waypoints():
    """Create a list of waypoints for the drone to fly to."""
    return [
        (10.80477, 106.71871),
        (10.80480, 106.71900),
        (10.80490, 106.71920),
        (10.80500, 106.71850)
    ]

def execute_mission(waypoints):
    """Execute the flight mission based on provided waypoints."""
    for waypoint in waypoints:
        latitude, longitude = waypoint
        fly_to_target(latitude, longitude)
        monitor_battery()
        check_for_obstacles()

if __name__ == "__main__":
    video_capture = cv2.VideoCapture(0)  # Initialize camera capture
    output_file = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

    target_altitude = 6
    print_drone_parameters() 
    arm_and_takeoff(target_altitude)

    waypoints = create_waypoints()
    execute_mission(waypoints)

    land()
    output_file.release()  # Release video output file
