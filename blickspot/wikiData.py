import requests 
import re

searchTitle = 'List_of_data_breaches' 
# 'List_of_security_hacking_incidents'
r = requests.get(f'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=links&redirects=1&titles={searchTitle}')

# We found the request url that returns a json 

req_json = r.json()

parseD = req_json['query']['pages']['49282028']['links']
size =  len(parseD)
hack_li = []
hack_dict = {}

for hacks in range(-1,9):
    # print(parseD[hacks]['title'])
    hack_li.append(parseD[hacks]['title'])

# print(hack_li , "\n")

hack_year = []
hack_name = []


pattern = r'\d+'
size = len(hack_li)
for datasec in range(size):
    data = str(hack_li[datasec])
    final_data = data.split(" ", 1)
    H_years = final_data[0]
    H_names = final_data[-1]
    hack_name.append(H_names)

    if H_years.isdigit():
        hack_year.append(H_years)
    else:
        H_years.replace(H_years,'0000')


# print(hack_year)
# print(hack_name)


for h_y, h_n in zip(hack_year, hack_name):
    data_str = {h_y : f"{h_n}"}
    hack_dict.update(data_str)


# print(hack_dict)



