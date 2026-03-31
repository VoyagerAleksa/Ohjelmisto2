import requests

url = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(url)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(data["value"])
    else:
        print("Virhe: palvelin palautti tilakoodin", vastaus.status_code)

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")