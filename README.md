# MediCopter: DIY Automated Drone for Medical Supply Delivery!

Welcome to our space! We are Quy, Vinh, and Khoa from Gia Dinh High School, Vietnam. Our project is MediCopter, an automated drone to deliver medical supply to rurals areas. In this github documentation, you can find our journey to build it from stratch, codes, and medias. You can also listen to our presentation at the end of this document.
# Introduction
Our drone primarily consist of multicopter frame, various sensors, and a power manangement system. In order to run automatically, there is an **Raspberry Pi 4** that run Python script to maneuver the drone to the desired duration, meanwhile sending GPS location back to the computer and detecting obstacles. To ensure smooth flight, there is a **Pixhawk 2.4.8** fly controller that control the balance of the flight using PID, which we had tune for better balance.
## Motivation:
In the Mekong Delta, which is an rural area located in the southern Vietnam, there is **44%** of hospitals that are not equipped with sufficient medical supplies, leading to the emergence of ___ . In the emergency need of a certain medical supply, the traditional vehicles, like ambulance, are not capable of reaching these hospitals on-time, leading to bad situations.

That is why we developed MediCopter, a solution that can significantly speed up the transportation times of medical supplies by using drones, one of the most modern means of transportation. With the capabilities of holding up to 2kg, and peak speed of 100 km/h [1], MediCopter can deliver most of the supplies needed for an emergency.

Our drone consists of hardwares components and Python script for the maneuver, and also for the

## Key features

* Capable of holding maximum of 2kg by the 3D printed arm and servor
* Automatically fly to the destination by using GPS and automatically update on the server
 * Using Object Detection to detect obstacles like bird, kites, building during maneuver

# Materials

## Hardware component


| Part                   | Components                                 | Description                         |
|------------------------|--------------------------------------------|-------------------------------------|
| **Multicopter Frame**  | Frame with Power Distribution Board        | Main structure for the drone       |
|                        | 4 x 11x4.5 Propellers                       | Provides lift                       |
|                        | 4 Arms                                     | Supports propellers                 |
|                        | 5000mAh LiPo Battery                         | Power source                       |
|                        | 4 x 40A Electronic Speed Controllers (ESC) | Controls motor speed                |
|                        | 980 kV Brushless Motor                      | Drives propellers                   |
| **Flight Controller**  | Raspberry Pi 4                              | Onboard processing                  |
|                        | Pixhawk 2.4.8                              | Flight control system               |
|                        | GPS                                         | Navigation                          |
| **Add-ons**            | Raspberry Pi Camera                         | Captures images and video           |
|                        | Microphone & Speaker                        | Audio input and output              |
|                        | SIM Module                                  | Cellular connectivity                |
|                        | USB Camera (for detecting landing area)    | Assists in landing detection        |

## Software Apps and Online Services

| Software/Service         | Purpose                                           |
|--------------------------|---------------------------------------------------|
| **ArduPilot**            | Provides tools for PID tuning and calibration of the drone's flight controller. Allows fine-tuning of performance and stability. |
| **Python Libraries**     | Essential libraries used for development:   |
|                          | - **DroneKit**: Enables communication with the drone and control of flight operations.  |
|                          | - **OpenCV**: Used for image processing and computer vision tasks, such as object detection and tracking. |
| **Firebase**             | Facilitates real-time location monitoring and data storage for the drone, allowing remote access to telemetry data. |
| **TensorFlow Lite**      | Enables deployment of the MobileNet-SSD object detection model on the Raspberry Pi, allowing real-time object detection capabilities. |
| **SolidWorks**           | Provides tools for 3D modeling and rendering of drone components, enabling visualization and design optimization. |


## Hand Tools and Fabrication Tools

| Tool                     | Purpose                                           |
|--------------------------|---------------------------------------------------|
| **3D Printer**           | Used for creating custom parts and components for the drone, allowing for rapid prototyping and design iterations. Supports various materials to enhance structural integrity. |
| **Electric Soldering Iron** | Essential for soldering electronic components onto the drone's circuit boards, ensuring reliable connections for optimal performance. Ideal for custom wiring and repairs. |

# Workflow
The workflow consists of 3 objects: Computer, Raspberry Pi, Pixhawk (Flight Controller)
## Pre-flight
1. **Connection**: The Raspberry Pi connects to the ThinkPad via Dynamic DNS and SSH. 
2. **Command Execution**: Commands are sent from the computer to execute Python scripts on the Raspberry Pi. 
3. **Preflight Setup**: Sensor calibration and battery checks are performed. 
## Mid-air
4. **Takeoff**: The Raspberry Pi commands the flight controller to spin the propellers. 
5. **Flight**: The flight controller adjusts motor speeds based on sensor data for stability. 
6. **Navigation**: The drone uses GPS for positioning and follows waypoints or manual inputs. 
7. **Video Streaming**: Video streaming is initiated. 
8. **Obstacle detection**: Detect obstacles (bird, building, etc)
## Landing
9. **Landing**: The flight controller commands the drone to gradually descend and land.
# Results & Achievement
On the demo of Aug 2023, our prototype are capable of flying automatically fly from point A to point B, and land safely. 

https://github.com/user-attachments/assets/ffb7f6d2-7564-45cc-9413-335dbed1bee8

This is a big win for us for the whole summer. Then, we validate our drone by bringing it into an innovation competition and won a Gold Medal. You can find the video of our presentation below:

  [![Demo Video](https://i.ytimg.com/an_webp/0ZWgyOTTF1M/mqdefault_6s.webp?du=3000&sqp=CMuj6rgG&rs=AOn4CLBX9lz_WXm-ejFd_2T9RwqOcMvjVg)](https://www.youtube.com/watch?v=0ZWgyOTTF1M&t)

# Further development

Although we have succesfully develop other add-on like object detection, our drone are not capable of dodging the obstacle in real-time. This is one of the main development that we can improve in the future. For further distance and more payload, we can upgrade our battery and motors.
