import json
import requests

url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

City = input("Enter your city here\n")
querystring = {"city":f"{City}"}

headers = {
	"X-RapidAPI-Key": "1ed29ba148mshbc61f104655aca5p1b038djsn6f24c54432c9",
	"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

if (response.status_code==requests.codes.ok):
    #print(response.text) # it will print all the response coming from API
    Wdic = json.loads(response.text)
    temp=(Wdic["temp"])
    print(f"Current Temperature of {City} is "+str(temp)+"\xb0C")
else:
    print( response.text)





