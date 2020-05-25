import json

json_list = []
csv_file = open('15csv_file.txt','r')

for line in csv_file.readlines():
    club, city, country = line.strip().split(',')
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)

csv_file.close()

json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)  # write json data to a file
json_file.close()
