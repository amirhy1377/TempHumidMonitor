import time
import board
import adafruit_dht
import requests

# تنظیمات سنسور
dhtDevice = adafruit_dht.DHT22(board.D4)  # استفاده از GPIO4

# تنظیمات سرور
SERVER_URL = 'http://your-server.com/api/data'

def read_and_send_data():
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        if humidity is not None and temperature is not None:
            print(f"Temp={temperature:.1f}C  Humidity={humidity:.1f}%")
            data = {
                'temperature': temperature,
                'humidity': humidity
            }
            response = requests.post(SERVER_URL, json=data)
            print(f"Data sent to server: {response.status_code}")
        else:
            print("Failed to retrieve data from humidity sensor")
    except RuntimeError as error:
        # خطاهای خواندن سنسور را نادیده بگیرید
        print(error.args[0])

if __name__ == "__main__":
    while True:
        read_and_send_data()
        time.sleep(60)  # ارسال داده‌ها هر 60 ثانیه

