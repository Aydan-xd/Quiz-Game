intro = input('Welcome to my Quiz do you want to play: ')

if intro == 'no':
    quit()
else:
    print('Alright lets start!\n')

score = 0

questions = ['Who played aunt may in The amazing Spider-man?: ', 'Who played Jorden Belfort in wolf of wall street?: ',
 'Who played megatron in dark side of the moon?: ', 'Who played r2-d2 in Revenge of the sith?: ',
 'Who played short round in the temple of doom?: ',]

awnsers = ['Rosemary Harris', 'Leonardo DiCaprio', 'Hugo Weaving', 'Kennedy Baker', 'Ke Huy Quan']

question_1 = input(questions[0])

if question_1.lower() == awnsers[0].lower():
    print('Correct')
    score += 1
    print('Score is: ', score)
else:
    print(awnsers[0], '\n')
    print('wrong')
    print(score)

question_2 = input(questions[1])

if question_2.lower() == awnsers[1].lower():
    print('Good job')
    score += 1
    print('Score is: ', score)
else:
    print(awnsers[1], '\n')
    print('You suck')
    score -= 1
    print(score)

question_3 = input(questions[2])

if question_3.lower() == awnsers[2].lower():
    print('Your on a roll!')
    score += 1
    print('Score is: ', score)
else:
    print(awnsers[2], '\n')
    print('Terible')
    score -= 1
    print(score)

question_4 = input(questions[3])
 
if question_4.lower() == awnsers[3].lower():
    print('Outstanding')
    score += 1
    print('Score is: ', score)
else:
    print(awnsers[3], '\n')
    print('Alt f4 please')
    score -= 1
    print(score)

question_5 = input(questions[4])

if question_5.lower() == awnsers[4].lower():
    print('Amazing!')
    score += 1
    print('Your score is: ', score)
else:
    print(awnsers[4], '\n')
    print('Uninstall')
    score -= 1
    print(score)

over = input('Quiz is over did you like it?: ')

k = input(quit())


