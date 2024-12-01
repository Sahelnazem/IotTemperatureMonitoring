#include <DHT.h>
#include <WiFi.h>
#include <HTTPClient.h>

// DHT Sensor settings
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// WiFi credentials
const char* ssid = "Your_Network_Name";
const char* password = "Your_Password";

// Server URL
const char* serverName = "http://your-server.com/temperature";

void setup() {
  Serial.begin(115200);
  dht.begin();

  // Connecting to WiFi
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // Reading temperature
  float temperature = dht.readTemperature();
  
  if (isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Sending data to server
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);

    // Sending data
    http.addHeader("Content-Type", "application/json");
    String jsonData = "{\"temperature\": " + String(temperature) + "}";
    int httpResponseCode = http.POST(jsonData);

    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);

    http.end();
  } else {
    Serial.println("WiFi Disconnected");
  }

  delay(10000); // Send data every 10 seconds
}
