import requests


api_key = 'f86c4c1ccfcb75393be1672a9cd07943'

while True:
    location = input("location: ")

    result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}')
    if result.json()['cod'] == 404:
        print("Invalid location")
        continue
    break

description = result.json()['weather'][0]['description']
temperature = round(result.json()['main']['temp'])
feels_like = round(result.json()['main']['feels_like'])
high = round(result.json()['main']['temp_max'])
low = round(result.json()['main']['temp_min'])

print(f"the weather in {location} is {temperature}° C with {description}. ")
print(f"It feels like {feels_like}° C.")
print(f"Today's high is {high}° C and today's low is {low}° C.")