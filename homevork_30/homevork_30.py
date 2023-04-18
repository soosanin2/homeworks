import json
import random
import requests


# 1_________

a = ['https://google.com/', 'https://facebook.com/', 'https://twitter.com/', 'https://amazon.com/', 'https://apple.com/']
select_site = random.choice(list(a))
res = requests.get(select_site)

print(res.status_code)
print(select_site)
print(len(res.content))


# 2_______

city = input("your city ").lower()
country = input("your country").lower()
get_city = 'https://geocoding-api.open-meteo.com/v1/search?name=' + city
get_location = requests.get(get_city)
list_location = get_location.json()

try:
    dict_location = list_location['results']

    for i in dict_location:
        latitude = i['latitude']
        longitude = i['longitude']

        if i['country'].lower() == country:
            for itm in dict_location:
                if itm['country_code'] != 'UA':
                    pass
                else:
                    latitude = itm['latitude']
                    longitude = itm['longitude']

            get_meteo = 'https://api.open-meteo.com/v1/forecast?latitude=' \
                        + str(latitude) + '&longitude=' + str(longitude) \
                        + '&hourly=temperature_2m&current_weather=true&forecast_days=1&timezone=auto'
            get_meteo_1 = requests.get(get_meteo)
            print(get_meteo_1.json())
            break
    else:
        print('sorry, an error occurred, you may have entered the wrong country name')

except:
    print('sorry, an error occurred, you may have entered the wrong city or country name')
