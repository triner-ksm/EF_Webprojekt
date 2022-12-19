#Import der notwendigen Module
import requests, json

#Basisangaben
api_key = ""
latitude = "47.178200"
longitude = "8.590790"
#https://www.latlong.net/

#API-URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&lat=" + latitude + "&lon=" + longitude + "&units=metric"

#Anfragen an das API
response = requests.get(complete_url)

#Ausgabe
print(response)
x = response.json()
print(x)