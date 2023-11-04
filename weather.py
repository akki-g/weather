import time
from twilio.rest import Client
import requests
import schedule


def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data

def c_to_f(c):
    return (c * 9/5)+32
def send_weather_update():
    latitude=28.568953
    longitude= -81.192588

    weather_data = get_weather(latitude, longitude)
    temperature_c = weather_data["hourly"]["temperature_2m"][0]
    humidity = weather_data["hourly"]["relativehumidity_2m"][0]
    temperature_f = c_to_f(temperature_c)

    weather_info = (
        f"Good Morning Akshat!\n"
        f"Current Weather in Orlando Florida: {temperature_f:.2f}\n"
        f"Relative Humidity: {humidity}"
    )

def send_text_message(body):
    account_sid= 'ACa8e92d896588e894e1703b6d691d645e'
    auth_token= '21d8b204414d157035aab0e035ec8335'
    from_phone_number= 18775114864
    to_phone_number= 18134038236

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("Text message sent!")

def main():
    schedule.every().day.at("16:18").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
