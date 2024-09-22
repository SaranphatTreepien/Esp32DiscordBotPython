import discord
import requests
import openai

# Discord bot token
DISCORD_TOKEN = 'TOKEN_BOT_DISCORD'

# OpenAI API key
OPENAI_API_KEY = 'GPT-4_API_KEY'

openai.api_key = OPENAI_API_KEY

# สร้าง Discord bot client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def get_esp32_data():
    try:
        response = requests.get(ESP32_URL)
        response.raise_for_status()  # Check the response status
        data = response.text.strip().split("\n")
        temp_line = next((line for line in data if "temperature:" in line), None)
        humid_line = next((line for line in data if "humidity:" in line), None)

        if temp_line and humid_line:
            temperature = temp_line.split(":")[1]
            humidity = humid_line.split(":")[1]
            return float(temperature), float(humidity)
        else:
            print("Invalid data format received.")
            return None, None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None

async def get_weather_commentary(temperature, humidity):
    prompt = f"The temperature is {temperature}°C and the humidity is {humidity}%. How is the weather today?"
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$temp':
        temperature, humidity = await get_esp32_data()
        if temperature is not None:
            await message.channel.send(f"Current Temperature: {temperature}°C")
        else:
            await message.channel.send("Failed to get data from ESP32.")

    elif message.content == '$humid':
        temperature, humidity = await get_esp32_data()
        if humidity is not None:
            await message.channel.send(f"Current Humidity: {humidity}%")
        else:
            await message.channel.send("Failed to get data from ESP32.")

    elif message.content == '$weather':
        temperature, humidity = await get_esp32_data()
        if temperature is not None and humidity is not None:
            weather_commentary = await get_weather_commentary(temperature, humidity)
            await message.channel.send(f"Weather analysis: {weather_commentary}")
        else:
            await message.channel.send("Failed to get data from ESP32.")

# เริ่ม bot
client.run(DISCORD_TOKEN)
