import json
import requests 

req= requests.get('https://api.open-meteo.com/v1/forecast?latitude=49.2497&longitude=-123.1193&daily=weather_code,temperature_2m_max,temperature_2m_min')
data = req.text
x = json.loads(data)
for i in x:
    print(i)

print("\n")
lat = x['latitude']
long = x['longitude']
time = x['timezone']
daily = x['daily']
temp = x['daily']['temperature_2m_max']
temp.sort()
print(f" here is the weather statistics in Vancouver for today!\n")
print(f"latitude: {lat}\nlongitude: {long}\ntimezone: {time}\ntemperatures today from lowest to highest:\n{temp} ")


