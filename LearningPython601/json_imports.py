import json

file = open('friends_json.txt', 'r')
file_contents = json.load(file)  # reads file and turns it to dictionary

file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])


movies = [
    {'name':'Ugly','director':'Anurag'},
    {'name':'Udaan','director':'Vikram'}
]

json_list = []
for movie in movies:
    json_list.append(movie)

json_file22 = open('movies_json','w')
json.dump(json_list, json_file22)
json_file22.close()

N = open('movies_json', 'r')
N_content = json.load(N)
N.close()

print(N_content)