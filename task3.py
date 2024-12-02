import json
import requests 

req= requests.get('https://api.open-meteo.com/v1/forecast?latitude=-78.1586&longitude=16.4063&hourly=temperature_2m')
data = req.text
x = json.loads(data)
for i in x:
    print(i)

print(f" here is the weather statistics in antarctica for today! {data}")