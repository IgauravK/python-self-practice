'''movies = [
    {'name':'Ugly','director':'Anurag'},
    {'name':'Udaan','director':'Vikram'}
]

def write_to_file(output):
    with open('file.csv','w') as f:
        f.write("name,director\n")
        for line in output:
            f.write(f"{line['name']}, {line['director']}\n")

write_to_file(movies)

def read_to_file(output):
    with open('file.csv','r') as f:
        content = f.readlines()
        for line in content[1:]:
            columns = line.strip().split(",")
            print (f"Name: {columns[0]}\tDirector: {columns[1]}")

read_to_file(movies)'''


import csv

movies = [
    {'name':'Ugly','director':'Anurag'},
    {'name':'Udaan','director':'Vikram'}
]

def write_to_file (output):
    with open('file.csv','w') as f:
        writer = csv.DictWriter(f, fieldnames=['name','director'])
        writer.writeheader()
        writer.writerows(output)

write_to_file(movies)

def read_to_file (output):
    with open('file.csv','r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']}\tDirector: {line['director']}")

read_to_file(movies)

def read_to_file1 (output):
    with open('file.csv','r') as f:
        reader = csv.DictReader(f)
        print (list(reader))

read_to_file1(movies)

'''import csv

movies = [
    {'name':'Ugly','director':'Anurag'},
    {'name':'Udaan','director':'Vikram'}
]

def write_to_file (output):
    with open('file.csv','w') as f:
        writer = csv.writer(f)
        f.write('name,director\n')
        writer.writerows([elem.values() for elem in output])

write_to_file(movies)

def read_to_file (output):
    with open('file.csv','r') as f:
        reader = csv.reader(f)
        for line in reader:
            print(f"Name: {line[0]}\tDirector: {line[1]}")

read_to_file(movies)'''
