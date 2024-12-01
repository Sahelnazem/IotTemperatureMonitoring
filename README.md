# IotTemperatureMonitoring

DHT11 Temperature Monitoring and Data Logging

This project demonstrates how to use an Arduino Uno with a DHT11 sensor to measure temperature and send the data to a web server via WiFi.

Features

Real-time temperature monitoring using the DHT11 sensor.
Sending the temperature data to a remote server in JSON format.
Simple and efficient communication using WiFi.
Hardware Requirements

Arduino Uno
DHT11 Temperature and Humidity Sensor
10kΩ Resistor (for pull-up on the data pin)
Jumper wires
Hardware Setup

Circuit Diagram

Use the above diagram to connect the DHT11 sensor to the Arduino Uno as follows:

DHT11 Pin	Arduino Pin
VCC	5V
DATA	Digital Pin 2
GND	GND
Software Requirements

Arduino IDE (v1.8 or newer).
Required libraries:
DHT sensor library by Adafruit.
Built-in WiFi and HTTPClient libraries (for ESP boards or similar).
How to Use

1. Clone this repository
git clone https://github.com/yourusername/arduino-dht11-temperature-logger.git
2. Install Libraries
Make sure you have the following libraries installed in your Arduino IDE:

DHT sensor library: Install from the Library Manager (Tools > Manage Libraries).
WiFi and HTTPClient: Already included with ESP32/ESP8266 boards.
3. Update the Code
Open the Arduino sketch file and update the following:

Replace Your_Network_Name and Your_Password with your WiFi credentials.
Update serverName with the URL of your server.
4. Upload the Code
Connect the Arduino Uno to your computer.
Open the Arduino IDE, select the correct board and port (Tools > Board and Tools > Port).
Upload the sketch.
5. Monitor the Output
Open the Serial Monitor (Tools > Serial Monitor) in the Arduino IDE to see the temperature data and server responses.

Sample JSON Payload

The temperature is sent to the server in the following format:

{
  "temperature": 25.6
}
Code Overview

Setup
The DHT11 sensor is initialized, and the board connects to WiFi.
dht.begin();
WiFi.begin(ssid, password);
Main Loop
Reads temperature data:
float temperature = dht.readTemperature();
Sends the data to a server if WiFi is connected:
HTTPClient http;
http.addHeader("Content-Type", "application/json");
http.POST(jsonData);
Enhancements

Consider adding the following features:

Humidity monitoring (supported by DHT11).
Failover mechanism for unstable WiFi connections.
Support for other sensors like DHT22.
Acknowledgments

Adafruit for the DHT library.
Arduino for its versatile microcontroller ecosystem.
License

This project is open-source and licensed under the MIT License. Feel free to use, modify, and share it.
