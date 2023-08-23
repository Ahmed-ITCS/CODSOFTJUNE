import requests
apikey= "&appid=bf70a8684296ffe792d05e49617f8bff"
cityapi = "https://api.openweathermap.org/data/2.5/weather?q="
zipapi = "https://api.openweathermap.org/data/2.5/weather?zip="
user_choice = input("1 to find wheather by city\n2 to find wheather by zip code : ")
if(user_choice =="1"):
    name = input("enter name of city : ")
    cityname = name.capitalize()
    url = cityapi+cityname+apikey
    data = requests.get(url)
    data=data.json()
    print("\ntemperature : ",data['main']['temp'])
    print("humidity : ",data['main']['humidity'])
    print("wind speed : ",data['wind']['speed'])
    print("description : ",data['weather'][0]['description'])
elif(user_choice =="2"):
    zip = input("enter zip code : ")
    countrycode = input("enter country code : ")
    url = zipapi+zip+","+countrycode+apikey
    #print(url)
    data = requests.get(url)
    data=data.json()
    print("\ntemperature : ",data['main']['temp'])
    print("humidity : ",data['main']['humidity'])
    print("wind speed : ",data['wind']['speed'])
    print("description : ",data['weather'][0]['description'])
