# Esp → Discord bot token by PYTHON

การสร้าง Token discord

[Generate Discord Bot Token & Use It](https://www.notion.so/Generate-Discord-Bot-Token-Use-It-10910dc08ab080f2b8e3eaed5fdc579d?pvs=21)

![1.รับสัญญาณ RFID จากบัตรเปิดประตูห้อง (1).png](1._RFID__(1).png)

![1.รับสัญญาณ RFID จากบัตรเปิดประตูห้อง (2).png](1._RFID__(2).png)

## Arduino code

### 1.การกำหนดค่าเบื้องต้น

```c
#include <WiFi.h>
#include <HTTPClient.h>
#include "DHT.h"

#define DHTPIN 2  // กำหนดขาให้กับ DHT
#define DHTTYPE DHT22  // ใช้ DHT22 หรือ DHT11
DHT dht(DHTPIN, DHTTYPE);
```

- **`#define DHTPIN`**: กำหนดพอร์ตที่เชื่อมต่อกับเซ็นเซอร์ DHT (ขา GPIO 2 ในที่นี้)
- **`#include`**: โหลดไลบรารีที่จำเป็นสำหรับการเชื่อมต่อ WiFi, การส่งข้อมูลผ่าน HTTP และการอ่านค่าเซ็นเซอร์ DHT
- **`#define DHTTYPE`**: ระบุประเภทเซ็นเซอร์ DHT ที่ใช้ (DHT22 ในตัวอย่างนี้)

### 2.การกำหนด WiFi และเซิร์ฟเวอร์

```c
const char* ssid = "Saranphat"; // ใส่ชื่อ WiFi ของคุณ
const char* password = "123456789"; // ใส่รหัสผ่าน WiFi ของคุณ\
String serverIP = "172.20.10.7"; // ที่อยู่ local IP ของเซิร์ฟเวอร์ Python
```

- **`ssid` และ `password`**: ชื่อและรหัสผ่านของเครือข่าย WiFi ที่ต้องการเชื่อมต่อ
- **`serverIP`**: ที่อยู่ IP ของเซิร์ฟเวอร์ Python ที่ ESP32 จะส่งข้อมูลไปให้

### 3.การตั้งค่าการเชื่อมต่อ

```cpp
 
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

```

- **`Serial.begin(115200)`**: เปิดการสื่อสารผ่าน Serial Monitor เพื่อดูข้อมูลสถานะการเชื่อมต่อ
- **`WiFi.begin()`**: เชื่อมต่อ WiFi ด้วย SSID และรหัสผ่านที่ระบุ
- **`while (WiFi.status() != WL_CONNECTED)`**: รอจนกว่า WiFi จะเชื่อมต่อสำเร็จ
- **`WiFi.localIP()`**: แสดง IP Address ของ ESP32 ที่ได้รับจากเครือข่าย WiFi

### 4.การอ่านค่า DHT และส่งข้อมูลไปยังเซิร์ฟเวอร์

```cpp

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

```

- **`dht.readTemperature()` และ `dht.readHumidity()`**: อ่านค่าอุณหภูมิและความชื้นจากเซ็นเซอร์ DHT
- **`isnan()`**: ตรวจสอบว่าการอ่านค่าจากเซ็นเซอร์เป็นไปอย่างถูกต้องหรือไม่
- **`Serial.print()`**: แสดงผลค่าอุณหภูมิและความชื้นใน Serial Monitor

### 5.การส่งข้อมูลผ่าน HTTP

```cpp
cpp
Copy code
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
```

- **`WiFi.status() == WL_CONNECTED`**: ตรวจสอบว่า ESP32 ยังคงเชื่อมต่อกับ WiFi อยู่หรือไม่
- **`HTTPClient http`**: สร้าง HTTP Client เพื่อส่งข้อมูล
- **`http.begin()`**: เริ่มต้นเชื่อมต่อกับ URL ของเซิร์ฟเวอร์ Python
- **`http.addHeader("Content-Type", "application/json")`**: กำหนดประเภทข้อมูลที่ส่ง (เป็น JSON)
- **`http.POST(jsonData)`**: ส่งข้อมูลอุณหภูมิและความชื้นในรูปแบบ JSON ไปยังเซิร์ฟเวอร์
- **`delay(10000)`**: หยุดการทำงานของ loop ชั่วคราวเป็นเวลา 10 วินาที

## โค้ดโดยรวม

```c
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
```

## Python Code

### การนำเข้าไลบรารี

```python
import discord
from discord.ext import commands
from flask import Flask, request, jsonify
import threading
//pip install discord.py Flask transformers command install
```

- **`discord`**: ไลบรารีสำหรับสร้าง Discord Bot
- **`commands`**: โมดูลที่ช่วยให้การจัดการคำสั่งในบอทง่ายขึ้น
- **`Flask`**: ไลบรารีสำหรับสร้างเว็บแอปพลิเคชันที่สามารถรับข้อมูล HTTP
- **`threading`**: ใช้สำหรับสร้าง thread ใหม่ เพื่อให้ Flask และ Discord Bot ทำงานพร้อมกัน

### 2. ค่าคอนฟิกสำหรับ Discord

```python
DISCORD_TOKEN = 'YOUR_DISCORD_TOKEN'  # ใส่ Token ของ Discord Bot ของคุณที่นี่
```

- **`DISCORD_TOKEN`**: ตัวแปรที่เก็บ Token สำหรับเข้าถึง Discord Bot ของคุณ (ควรเก็บเป็นความลับ)

### 3. การสร้าง Flask App

```python
 
app = Flask(__name__)

temperature = None
humidity = None

```

- **`app = Flask(__name__)`**: สร้างแอปพลิเคชัน Flask
- **`temperature` และ `humidity`**: ตัวแปรที่ใช้เก็บค่าอุณหภูมิและความชื้นที่รับมาจาก ESP32 โดยเริ่มต้นเป็น `None`

### 4. Route สำหรับรับข้อมูลจาก ESP32

```python
 
@app.route('/update', methods=['POST'])
def update_sensor_data():
    global temperature, humidity
    try:
        data = request.json
        temperature = data.get('temp')
        humidity = data.get('humid')
        print(f"Received temperature: {temperature}")
        print(f"Received humidity: {humidity}")
        if temperature is None or humidity is None:
            return jsonify({'status': 'error', 'message': 'Invalid data format'}), 400
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to process data'}), 500

```

- **`@app.route('/update', methods=['POST'])`**: กำหนด route `/update` สำหรับรับข้อมูลแบบ POST
- **`update_sensor_data`**: ฟังก์ชันที่ทำงานเมื่อมีการส่งข้อมูลมาที่ `/update`
    - **`request.json`**: รับข้อมูล JSON จาก HTTP request
    - **`temperature` และ `humidity`**: เก็บค่าจากข้อมูลที่ได้รับ
    - **`print`**: แสดงค่าที่รับมาทาง console
    - **การตรวจสอบข้อมูล**: หากค่าที่ได้รับเป็น `None` จะส่งกลับข้อความแสดงข้อผิดพลาด

### 5. สร้าง Discord Bot

```python
intents = discord.Intents.default()
intents.message_content = True  # เปิดใช้งาน Intent สำหรับข้อความ
bot = commands.Bot(command_prefix='$', intents=intents)
```

- **`intents`**: กำหนดความสามารถของ Bot เช่น การอ่านข้อความที่ผู้ใช้ส่ง
- **`bot`**: สร้าง Bot โดยกำหนด prefix สำหรับคำสั่ง (ในที่นี้คือ `$`)

### 6. คำสั่งสำหรับ Discord Bot

```python
@bot.command()
async def temp(ctx):
    if temperature is not None:
        try:
            temperature_float = float(temperature)
            temperature_formatted = f"{temperature_float:.1f}"
            await ctx.send(f"Current temperature: {temperature_formatted}°C 🌡️")
        except ValueError:
            await ctx.send("Invalid temperature value.")
    else:
        await ctx.send("No temperature data available.")
@bot.command()
async def humid(ctx):
    if humidity is not None:
        humidity_int = round(humidity)
        await ctx.send(f"Current humidity: {humidity_int}% 💧")
    else:
        await ctx.send("No humidity data available.")
```

- **`@bot.command()`**: กำหนดคำสั่งที่สามารถเรียกใช้ได้ใน Discord
- **`temp(ctx)`**: แสดงค่าอุณหภูมิ
- **`humid(ctx)`**: แสดงค่าความชื้น
- **`ctx.send()`**: ส่งข้อความตอบกลับไปยัง Discord Channel ที่มีการเรียกใช้คำสั่ง

### 7. การรัน Flask และ Discord Bot

```python
if __name__ == '__main__':
    def run_flask():
        app.run(host='0.0.0.0', port=5000)
    threading.Thread(target=run_flask).start()
    bot.run(DISCORD_TOKEN)
```

- **`if __name__ == '__main__':`**: ตรวจสอบว่าโค้ดกำลังถูกเรียกใช้โดยตรง
- **`run_flask()`**: ฟังก์ชันที่ใช้เรียก Flask server โดยเปิดให้เข้าถึงจากทุก IP ที่อยู่ในเครือข่าย
- **`threading.Thread(target=run_flask).start()`**: เริ่ม thread ใหม่เพื่อให้ Flask server ทำงานพร้อมกันกับ Discord Bot
- **`bot.run(DISCORD_TOKEN)`**: เริ่ม Discord Bot โดยใช้ Token ที่กำหนด

## โด้ดโดยรวมทั้งหมด

```python
import discord
from discord.ext import commands
from flask import Flask, request, jsonify
import threading

DISCORD_TOKEN = 'YOUR_DISCORD_TOKEN'  # ใส่ Token ของ Discord Bot ของคุณที่นี่

# สร้าง Flask App สำหรับรับข้อมูลจาก ESP32
app = Flask(__name__)

temperature = None
humidity = None

@app.route('/update', methods=['POST'])
def update_sensor_data():
    global temperature, humidity
    try:
        data = request.json
        temperature = data.get('temp')
        humidity = data.get('humid')
        # ตรวจสอบข้อมูลที่ได้รับ
        print(f"Received temperature: {temperature}")
        print(f"Received humidity: {humidity}")
        if temperature is None or humidity is None:
            return jsonify({'status': 'error', 'message': 'Invalid data format'}), 400
        return jsonify({'status': 'success'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to process data'}), 500

# สร้าง Discord Bot
intents = discord.Intents.default()
intents.message_content = True  # เปิดใช้งาน Intent สำหรับข้อความ
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def temp(ctx):
    if temperature is not None:
        try:
            temperature_float = float(temperature)
            temperature_formatted = f"{temperature_float:.1f}"
            await ctx.send(f"Current temperature: {temperature_formatted}°C 🌡️")
        except ValueError:
            await ctx.send("Invalid temperature value.")
    else:
        await ctx.send("No temperature data available.")

@bot.command()
async def humid(ctx):
    if humidity is not None:
        # แสดงความชื้นด้วยจำนวนเต็ม
        humidity_int = round(humidity)
        await ctx.send(f"Current humidity: {humidity_int}% 💧")
    else:
        await ctx.send("No humidity data available.")

if __name__ == '__main__':
    # เริ่ม Flask server สำหรับรับข้อมูลจาก ESP32
    def run_flask():
        app.run(host='0.0.0.0', port=5000)

    threading.Thread(target=run_flask).start()

    # เริ่ม Discord bot
    bot.run(DISCORD_TOKEN)

```