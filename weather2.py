#for making get requests
import requests
import json

print("Welcome to the Weather Data program") 
#Country codes when pulling names
country_code = 'US'
#Main function loop
while True:
        input1 = input('Please enter zip code or City name: ')
  
        if input1.isdigit():
                key = f"zip={input1},{country_code}"

                request_url = 'https://api.openweathermap.org/data/2.5/weather?'+key+'&APPID=13fbbcc945b3e6c3b8822d546c124a9d&units=imperial'
                print(request_url)
  
                print('Requesting...')
                request = requests.get(request_url)
                if request.status_code == 200:
                        print('Sucessfull data retrieval')
                        #request.text contains data in json format
                        #using json.loads() that converts data to python dict.
                        data = json.loads(request.text)
  
                        print('Results:')
  
                        print('Name: ',data['name'])
                        print('temperature: ', data['main']['temp'],'in fahrenheit')
                        print('wind: ',data['wind']['speed'],'deg',data['wind']['deg'])
                        print('pressure: ',data['main']['pressure'])
                        print('humidity: ',data['main']['humidity'])
                        print('cordinates: ',data['coord'])
                        print('clouds: ',data['clouds'])
                        print('weather:',data['weather'][0]['main'])
                        print('weather description: ',data['weather'][0]['description'])
                else:
                        print(request.status_code)
                        print(request.text)

        elif input1.isalpha():
                key = f'q={input1},{country_code}'

                request_url = 'https://api.openweathermap.org/data/2.5/weather?'+key+'&APPID=13fbbcc945b3e6c3b8822d546c124a9d&units=imperial'
                print(request_url)
  
                print('Requesting...')
                request = requests.get(request_url)
                if request.status_code == 200:
                        print('Sucessfull data retrieval')
                        data = json.loads(request.text)
  
                        print('Results:')
  
                        print('Name: ',data['name'])
                        print('temperature: ', data['main']['temp'],'in fahrenheit')
                        print('wind: ',data['wind']['speed'],'deg',data['wind']['deg'])
                        print('pressure: ',data['main']['pressure'])
                        print('humidity: ',data['main']['humidity'])
                        print('cordinates: ',data['coord'])
                        print('clouds: ',data['clouds'])
                        print('weather:',data['weather'][0]['main'])
                        print('weather description: ',data['weather'][0]['description'])
                else:
                        print(request.status_code)
                        print(request.text)
