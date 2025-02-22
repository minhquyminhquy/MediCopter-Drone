# MediCopter: DIY Autonomous Drone for Medical Supply Delivery

Welcome to our project! We are Quy, Vinh, and Khoa from Gia Dinh High School, Vietnam. **MediCopter** is an automated drone designed to deliver medical supplies to rural areas. In this documentation, you will find details about our journey in building the drone from scratch, including the code and media. At the end of this document, you can also listen to our presentation.

<div align="center">
  <img src="media/medicopter_landscape.jpg" alt="MediCopter Poster" width="600"/>
</div>

## Introduction

MediCopter is built around a multicopter frame, various sensors, and a power management system. To achieve autonomous flight, it uses a **Raspberry Pi 4** running Python scripts to maneuver the drone to the desired destination, send GPS data back to the server, and detect obstacles. The flight stability is maintained by the **Pixhawk 2.4.8** flight controller, which uses PID tuning.

### Motivation
In the Mekong Delta, a rural region in southern Vietnam, **44%** of hospitals lack sufficient medical supplies, creating a critical need for on-demand medical delivery. Traditional vehicles like ambulances struggle to reach these areas on time due to poor infrastructure and traffic.

MediCopter addresses this issue by speeding up medical supply transportation with drones. Capable of carrying up to 2kg and reaching a peak speed of 100 km/h, MediCopter can deliver most supplies needed in emergencies.

### Key Features
- **Max Load**: Carries up to 2kg with 3D-printed arms and servos.
- **Autonomous Flight**: Uses GPS for automatic navigation and real-time updates to the server.
- **Obstacle Detection**: Detects obstacles like birds, kites, and buildings using object detection.

![Poster - MediCopter](media/poster.jpg)

---

## Materials

### Hardware Components

| Part                    | Components                                     | Description                             |
|-------------------------|------------------------------------------------|-----------------------------------------|
| **Multicopter Frame**    | Frame with Power Distribution Board            | Main structure of the drone             |
|                         | 4 x 11x4.5 Propellers                         | Provides lift                           |
|                         | 4 Arms                                        | Supports the propellers                 |
|                         | 5000mAh LiPo Battery                          | Power source                            |
|                         | 4 x 40A ESCs                                   | Controls motor speed                    |
|                         | 980 kV Brushless Motors                       | Drives propellers                       |
| **Flight Controller**    | Raspberry Pi 4                                | Onboard processing                      |
|                         | Pixhawk 2.4.8                                 | Flight control system                   |
|                         | GPS                                            | Navigation                               |
| **Add-ons**              | Raspberry Pi Camera                           | Captures images and video               |
|                         | Microphone & Speaker                          | Audio input and output                  |
|                         | SIM Module                                    | Cellular connectivity                   |
|                         | USB Camera (for landing detection)            | Assists with landing detection          |

### Software & Online Services

| Software/Service         | Purpose                                           |
|--------------------------|---------------------------------------------------|
| **ArduPilot**            | Provides tools for PID tuning and calibration of the drone’s flight controller. |
| **Python Libraries**     | Libraries used for development:                   |
|                         | - **DroneKit**: Communicates with the drone and controls flight operations. |
|                         | - **OpenCV**: Image processing and computer vision (object detection). |
| **Firebase**             | Real-time location tracking and telemetry data storage. |
| **TensorFlow Lite**      | Deploys the MobileNet-SSD object detection model for real-time object recognition. |
| **SolidWorks**           | 3D modeling and design optimization of drone components. |

### Hand Tools & Fabrication Tools

| Tool                     | Purpose                                           |
|--------------------------|---------------------------------------------------|
| **3D Printer**           | Rapid prototyping of custom drone parts. |
| **Electric Soldering Iron** | For soldering electronic components and custom wiring. |

---

## Workflow

The workflow involves 3 main components: **Computer**, **Raspberry Pi**, and **Pixhawk** (Flight Controller).

### Pre-flight
1. **Connection**: Raspberry Pi connects to the computer via Dynamic DNS and SSH.
2. **Command Execution**: Python scripts are executed on the Raspberry Pi through the computer.
3. **Preflight Setup**: Sensor calibration and battery checks are performed.

### Mid-flight
4. **Takeoff**: Raspberry Pi commands the flight controller to spin the propellers.
5. **Flight**: The flight controller adjusts motor speeds to maintain stability.
6. **Navigation**: GPS guides the drone to its destination based on waypoints or manual inputs.
7. **Video Streaming**: Video is streamed from the onboard camera.
8. **Obstacle Detection**: Objects like birds and buildings are detected during flight.

### Landing
9. **Landing**: The flight controller gradually descends and lands the drone safely.

<div align="center">
  <img src="media/Rasp-Pi-Combination.png" alt="Raspberry Pi - Pixhawk Combination" width="600"/>
</div>

Example code:

<div align="center">
  <img src="media/example-code.png" alt="Example Code" width="600"/>
</div>

---

## Building Process

The project consists of two main phases: **Manual Control** (Pixhawk) and **Autonomous Control** (Pixhawk + Raspberry Pi). You can find our assembly process in this [YouTube playlist](https://youtube.com/playlist?list=PL21Xkm88JcA4obuWS0P6m1VQUeOZoDrcb&si=dXZTIC1rQ1kXRq51).

[![MediCopter Assembling Playlist](https://i.ytimg.com/vi/Av5gm4qZClE/hqdefault.jpg)](https://youtube.com/playlist?list=PL21Xkm88JcA4obuWS0P6m1VQUeOZoDrcb&si=dXZTIC1rQ1kXRq51)

### Phase 1: Manual Control with Pixhawk

#### Building the Frame
1. **Connect ESCs to Power Distribution Board (PDB)**
   <div align="center">
     <img src="media/assembling/Connect-ESC-to-PDB.png" alt="Connect ESC to PDB" width="200"/>
   </div>

2. **Connect Brushless Motors to Arms**
   <div align="center">
     <img src="media/assembling/Connect-motors-to-arms.png" alt="Connect Motors to Arms" width="200"/>
   </div>

3. **Connect Arms to PDB**
   <div align="center">
     <img src="media/assembling/Connect-motors-to-arms.png" alt="Connect Arms to PDB" width="200"/>
   </div>

4. **Connect Battery to PDB**
   <div align="center">
     <img src="media/assembling/Connect-Battery-PDB.png" alt="Connect Battery to PDB" width="200"/>
   </div>

5. **Connect Pixhawk to PDB**
   <div align="center">
     <img src="media/assembling/Connect-Pixhawk-PDB.png" alt="Connect Pixhawk to PDB" width="200"/>
   </div>

6. **3D Print the Legs**: You can find the `.stl` files in the `3D_components` folder.

[Download the .STL files here](https://github.com/user-attachments/assets/169ed1b9-fe8f-40f5-9008-af87535a27e2)

#### Pixhawk Setup
7. **Calibration and PID Tuning with ArduPilot**
   <div align="center">
     <img src="media/assembling/Calibration-PID-Tuning.png" alt="Calibration and PID Tuning" width="200"/>
   </div>

8. **Spinning Test #1**: ESCs burned out, so we upgraded to new ESCs.

9. **Connect New ESCs**
   <div align="center">
     <img src="media/assembling/New-ESC.png" alt="Connect New ESCs" width="200"/>
   </div>

10. **Field Test #1 with Controller**: First test with manual control.

[Watch the test video](https://github.com/user-attachments/assets/e171f9fb-7b1c-440d-8f37-c7a3fa3b547b)

---

### Phase 2: Autonomous Control

#### Raspberry Pi Setup
1. **Connect Raspberry Pi**
   [View image of the Raspberry Pi connection](https://github.com/user-attachments/assets/7c1b4f54-8426-4d72-b6c0-2fdf0d123a5a)

2. **Connect Servo for Box Grabber**: Download the 3D print files at `3D_components/BoxGrabberPart1.stl` and `3D_components/BoxGrabberPart2.stl`.
   
   [View servo connection image](https://github.com/user-attachments/assets/4f15eef7-565c-4d65-8523-65f59fb4e886)

3. **Field Test #2**: Automatic flight and delivery.

---

#### Developing MobileNet-SSD Model
1. **Image Collection**: Gather images for training the object detection model (buildings, birds, kites).
2. **Train the Model**
   [Training progress image](https://github.com/user-attachments/assets/8a863976-2954-48e5-a756-10348f319502)
3. **Deploy on Raspberry Pi**: Model deployed on the drone for real-time object detection.

[Deployment image](https://github.com/user-attachments/assets/92360678-1291-4f0b-8a1d-1a17bf62b5d6)

#### Camera Module Setup
[Camera module setup](https://github.com/user-attachments/assets/2ed117ee-a2e5-4d44-a882-4a480ddee704)

---

## Results & Achievements

In our August 2023 demo, our prototype successfully flew autonomously from point A to point B and landed safely.

[Watch the demo video](https://github.com/user-attachments/assets/ffb7f6d2-7564-45cc-9413-335dbed1bee8)

This success led us to participate in an innovation competition where we won a Gold Medal. Below is a video of our presentation:

<div align="center">
  [![AI-JAM Presentation Video](https://i.ytimg.com/an_webp/0ZWgyOTTF1M/mqdefault_6s.webp)](https://www.youtube.com/watch?v=0ZWgyOTTF1M&t)
  *AI-JAM Presentation Video*
</div>

---

## Further Development

While we successfully implemented object detection, real-time obstacle avoidance remains a key area for improvement. Additionally, we plan to enhance the drone’s range and payload capacity by upgrading its battery and motors.

