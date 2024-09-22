#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 2  // กำหนดขาให้กับ DHT
#define DHTTYPE DHT22  // ใช้ DHT22 หรือ DHT11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Saranphat"; // ใส่ชื่อ WiFi ของคุณ
const char* password = "123456789"; // ใส่รหัสผ่าน WiFi ของคุณ

String serverIP = "172.20.10.7"; // ที่อยู่ local IP ของเซิร์ฟเวอร์ Python

void setup() {
  Serial.begin(115200);
  dht.begin();
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  Serial.println("WiFi connected.");
  Serial.print("ESP32 IP address: ");
  Serial.println(WiFi.localIP());  // แสดง IP Address ของ ESP32 ที่เชื่อมต่อ
}

void loop() {
  float temp = dht.readTemperature();
  float humid = dht.readHumidity();
  
  if (isnan(temp) || isnan(humid)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  // แสดงค่าอุณหภูมิและความชื้น
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println("°C");
  Serial.print("Humidity: ");
  Serial.print(humid);
  Serial.println("%");
  
  // ส่งค่าไปยังเซิร์ฟเวอร์ที่ใช้ Python สำหรับ Discord Bot
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    
    String serverURL = "http://" + serverIP + ":5000/update"; 
    http.begin(serverURL);
    
    http.addHeader("Content-Type", "application/json");
    String jsonData = "{\"temp\": " + String(temp) + ", \"humid\": " + String(humid) + "}";
    
    int httpResponseCode = http.POST(jsonData);
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    http.end();
  }
  
  delay(10000); // อัปเดตทุกๆ 10 วินาที (ปรับเปลี่ยนตามที่คุณต้องการ)
}