print('Welcome to the GQuiz!')
Name = input('Please enter your name: ')

question = open('questions.txt','r')
question_list = [line.strip() for line in question.readlines()]
question.close()

score = 0
total = len(question_list)

for question in question_list:
    q, a = question.split('=')
    ans = input('{}='.format(q))
    if a == ans:
        score += 1

result = open('results.txt', 'w')
result.write('Your final score is {}/{}.'.format(score, total))
result.close()

result = open('results.txt','r')
your_result = result.read()
print (your_result)







