"""
This script instructs the drone to take off, fly to target position, and land. 
Meanwhile recording the journey with the camera infront. In this phase,
we connected to the drone via PyMAVLink and controled it by telemetry.
This code is executed on my laptop, no on the Raspberry Pi.

Recreate day: 26 Feb 2025
Demo day: 02 Jul 2023
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect
import time

# FLYING STATES
IS_ARMING_AND_TAKING_OFF = False
HAS_FINISHED_ARMING_AND_TAKEOFF = False
HAS_LANDED = False

# FLYING PARAMS
THRESHOLD_DISTANCE = 2  

def arm_vehicle():
    """Arms the drone and sets the mode to GUIDED"""
    # Arm the drone
    master.mav.command_long_send(
        master.target_system, master.target_component,
        dialect.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0
    )
    print("Arming the drone...")
    
    # Change mode to GUIDED
    master.set_mode(dialect.MAV_MODE_GUIDED_ARMED)

def takeoff(target_altitude):
    """Sends takeoff command to the drone"""
    master.mav.command_long_send(
        master.target_system, master.target_component,
        dialect.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, target_altitude, 0
    )
    print(f"Taking off to {target_altitude} meters")

def wait_for_takeoff(target_altitude):
    """Wait until the drone reaches the target altitude"""
    while True:
        msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        altitude = msg.relative_alt / 1000.0  # Altitude in meters
        print(f"Altitude: {altitude} meters")
        
        if altitude >= target_altitude:
            print("Target altitude reached")
            break
        time.sleep(1)   

def fly_to_target(target_latitude, target_longitude):
    """Sends the drone to a target position"""
    master.mav.mission_item_send(
        master.target_system, master.target_component,
        0,  # Mission index
        dialect.MAV_FRAME_GLOBAL_RELATIVE_ALT,
        dialect.MAV_CMD_NAV_WAYPOINT, 0, 1, 0,
        0, 0, 0, 0, target_latitude, target_longitude, 0
    )

    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    print(f"Latitude: {msg.lat}, Longitude: {msg.lon}, Altitude: {msg.relative_alt / 1000.0}m")

    print(f"Flying to target location: {target_latitude}, {target_longitude}")

def is_at_target_location(target_latitude, target_longitude):
    """Check if the drone has reached the target location"""
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
    drone_latitude = msg.lat / 1E7
    drone_longitude = msg.lon / 1E7
    distance_to_target = ((drone_latitude - target_latitude) ** 2 + (drone_longitude - target_longitude) ** 2) ** 0.5
    return distance_to_target <= THRESHOLD_DISTANCE

def land_vehicle():
    """Land the drone"""
    master.mav.command_long_send(
        master.target_system, master.target_component,
        dialect.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0, 0
    )
    print("Landing the drone")

def main():
    target_latitude = 10.80491722128159
    target_longitude = 106.71654397535926
    target_altitude = 6  

    # Arming and taking off sequence
    arm_vehicle()
    time.sleep(2)  # Wait a bit before takeoff
    takeoff(target_altitude)
    wait_for_takeoff(target_altitude)

    # Fly to the target location
    fly_to_target(target_latitude, target_longitude)
    
    while True:
        if is_at_target_location(target_latitude, target_longitude):
            print("Reached target location!")
            land_vehicle()
            break
        
        time.sleep(1)

    # Wait for the drone to land
    while True:
        msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        altitude = msg.relative_alt / 1000.0
        if altitude <= 0.05:
            print("Drone has landed")
            break
        time.sleep(1)

if __name__ == "__main__":

    connection_string = 'udp:127.0.0.1:14550'  
    master = utility.MAVLink(connection_string)

    main()
