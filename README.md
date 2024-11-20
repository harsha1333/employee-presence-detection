# employee-presence-detection
This project involves integrating an ESP32 microcontroller, a PIR (Passive Infrared) motion sensor, the Wokwi simulation platform, and ThingSpeak cloud services to detect a person’s presence and display the data on a webpage. Here's an overview:

Components and Functionality
ESP32 and PIR Sensor Integration:

The PIR sensor detects motion and sends a digital signal to the ESP32.
If motion is detected, an onboard LED connected to GPIO13 is turned on, and the system records the presence of a person.
Wi-Fi and ThingSpeak Cloud:

The ESP32 connects to Wi-Fi using Wokwi's simulated network credentials.
Detected data (person presence) is uploaded to ThingSpeak, a cloud-based platform for IoT data logging and visualization.
The project uses an API key and channel configuration to transmit real-time data to the cloud.
Web Interface:

The data from ThingSpeak is retrieved and displayed on a custom webpage, which reflects whether an employee is present based on the PIR sensor's data.
Workflow
Setup:

Configure the PIR sensor to monitor motion.
Use the Wokwi platform to simulate hardware and test the logic.
Connect the ESP32 to Wi-Fi and initialize ThingSpeak communication.
Data Processing:

The ESP32 checks for motion every 15 seconds.
The status is encoded (1 for present, 0 for absent) and sent to ThingSpeak.
Visualization:

The data uploaded to ThingSpeak is made available through its APIs.
A webpage fetches this data and dynamically updates the employee's presence status.
Applications
This project is a great demonstration of IoT (Internet of Things) in workplace monitoring. It can be scaled to:

Track attendance or presence in offices.
Monitor occupancy for energy-saving automation.
Extend to additional sensors for more detailed analysis.
