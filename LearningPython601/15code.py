import json

file = open('15csv_file.txt','r')
clubs = file.readlines()
file.close()

json_list = []
clubs_details = [line.strip() for line in clubs]

for clubrow in clubs_details:
    club_name, club_city, club_country = clubrow.split(',')
    data ={
        'club' : club_name,
        'city' : club_city,
        'country' : club_country
    }
    json_list.append(data)


json_file1 = open('json_file1.txt', 'w')
json.dump(json_list, json_file1)
json_file1.close()
