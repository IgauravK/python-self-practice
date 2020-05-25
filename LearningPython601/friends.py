friends = input('Enter three friends name, seprated by comma (no spaces please): ').split(',')

people1 = open('people1', 'r')
people_nearby = [line.strip() for line in people1.readlines()]

people1.close()

friends_s = set(friends)
people_nearby_s = set(people_nearby)

friends_nearby_set = friends_s.intersection(people_nearby_s)

nearby_friends_file = open('nearbyfriends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby!, Avoid them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
