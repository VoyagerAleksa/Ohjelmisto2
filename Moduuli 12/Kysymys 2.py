import requests

api_key = "409196c4c54853c6dde12cb6095e5508"

municipality = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

description = data["weather"][0]["description"]
temperature = data["main"]["temp"]

print(f"Weather: {description}")
print(f"Temperature: {temperature} Celsius")