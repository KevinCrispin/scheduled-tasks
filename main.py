import requests
import os
from twilio.rest import Client

sid = os.environ.get("sid")
auth = os.environ.get("auth")
fn = "whatsapp:+916360530768"

client = Client(sid,auth)
 
endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_params = {
    "lat":46.947975,
    "lon": 7.447447,
    "cnt" : 4,
    "appid": "360c4f5b8e9c2bc2c41e5496ac12106a"
}

response = requests.get(endpoint,api_params)
output = response.json()
print(output)

gonna_Rain = False
for time in output["list"]:
    if int(time["weather"][0]["id"])>700:
        print(time["dt_txt"])

for i in range(0,20):
    if(not gonna_Rain):
        client.messages.create(
                from_= "whatsapp:+14155238886",
                to= fn,
                body="It is not going to rain"
                )
    else:
        client.messages.create(
                from_= "whatsapp:+14155238886",
                to= fn,
                body="It is going to rain, carry an umbrella"
                )
    
