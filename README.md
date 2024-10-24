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
|                        | 5000mA LiPo Battery                         | Power source                       |
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


# Results & Achievement

On Aug 2023, our prototype are capable of flying automatically reach. We also successfully develop the add-on feature for communication between the human and human

# Further development

Our drone is still limit

There are two types of synchronization and they can complement each other:
