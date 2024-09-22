import discord
from discord.ext import commands
from flask import Flask, request, jsonify
import threading

# ค่าคอนฟิกสำหรับ Discord
DISCORD_TOKEN = 'TOKEN'  # ใส่ Token ของ Discord Bot ของคุณที่นี่

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
