import json
import random
import requests

# 1_________

google = 'https://google.com/'
facebook = 'https://facebook.com/'
twitter = 'https://twitter.com/'
amazon = 'https://amazon.com/'
apple = 'https://apple.com/'

a = [google, facebook, twitter, amazon, apple]
select_site = random.choice(list(a))
res = requests.get(select_site)

print(res.status_code)
print(select_site)
print(len(res.content))

# 2_______

city = input("your city ")
get_city = 'https://geocoding-api.open-meteo.com/v1/search?name=' + city
get_location = requests.get(get_city)
list_location = get_location.json()

dict_location = list_location['results']
for i in dict_location:
    if i['country_code'] != 'UA':
        pass
    else:
        latitude = i['latitude']
        longitude = i['longitude']
        print(i['name'])

get_meteo = 'https://api.open-meteo.com/v1/forecast?latitude='\
            + str(latitude) +  '&longitude='+ str(longitude) \
            + '&hourly=temperature_2m&forecast_days=1&timezone=auto'
get_meteo_1 = requests.get(get_meteo)
print(get_meteo_1.json())








