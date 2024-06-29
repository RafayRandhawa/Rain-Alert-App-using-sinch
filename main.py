import requests
import sinch
import os
#SDK
PROJECT_ID = "f251b7ce-6490-497e-b8bc-1bed1be1bd66"
APP_ID = "f106fefb-99ea-427f-a271-7649d4fc4089"
SECRET = "xL98gM2F.wyTEoejCzeh_PflLc"
FROM_NUMBER = "447520651202"
TO_NUMBER = "923477229072"
#REST API-----------------------------------------
SERVICE_PLAN_ID = "2ef7e427a6e748a3b6f8b7c638dde6ab"
API_TOKEN = os.environ.get("AUTH_TOKEN")
payload = {
    "from": FROM_NUMBER,
    "to": [
        TO_NUMBER
    ],
    "body": "Hello how are you"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_TOKEN
}
#REST API-----------------------------------------
API_KEY_OPENWEATHER = "94662b46ddf115fcc031345ff3d275f3"
openweather_3hr_interval_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
openweather_parameters = {
    "lat": 24.857428,
    "lon": 67.068766,
    "appid": API_KEY_OPENWEATHER,
    "units": "metric",
    "cnt": 8
}
openweather_response = requests.get(openweather_3hr_interval_Endpoint, params=openweather_parameters)
openweather_response.raise_for_status()
weather_data = openweather_response.json()
print(weather_data)
for data in weather_data["list"]:
    for weather in data["weather"]:
        if weather["main"] == "Rain":
            weather_description = weather["description"].title()
            time = data["dt_txt"].split(" ")[1]
            date = data["dt_txt"].split(" ")[0]
            message_string = f"We predict {weather_description} at {time} on {date}"
            client = sinch.SinchClient(project_id=PROJECT_ID, key_id=APP_ID, key_secret=SECRET)
            payload["body"] = message_string  #REST API
            batch_response = client.sms.batches.send(body=message_string, to=[TO_NUMBER], from_=FROM_NUMBER,
                                                     delivery_report="none")
            print(batch_response)
