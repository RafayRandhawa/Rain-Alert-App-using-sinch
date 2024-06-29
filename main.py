import requests
import sinch
#SDK
PROJECT_ID = "your project id"
APP_ID = "your app id"
SECRET = "your secret key"
FROM_NUMBER = "your sinch number here"
TO_NUMBER = "your number here"
API_KEY_OPENWEATHER = "your open weather api key"
openweather_3hr_interval_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
openweather_parameters = {
    "lat": "integer value of your latitude here",
    "lon": "integer value of your longitude here,
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
            batch_response = client.sms.batches.send(body=message_string, to=[TO_NUMBER], from_=FROM_NUMBER,
                                                     delivery_report="none")
            print(batch_response)
