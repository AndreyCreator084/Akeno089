"""Создайте новый проект или продолжите работу в текущем проекте.
Напишите код, который форматирует строки для следующих сценариев.
Укажите переменные, которые должны быть вставлены в каждую строку:"""

#Использование %:

team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s!' % team1_num)
print('В команде Волшебники данных участников: %s!' % team2_num)
print('Итого сегодня в командах участниках %s и %s!' % (team1_num, team2_num))

#Использование format():

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
print('Команда Мастера кода решила задач: {}!'.format(score_1))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))

#Использование f-строк:

challenge_result = ''
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_2 > score_1 or score_2 == score_1 and team2_time > team1_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'


tasks_total = score_1 + score_2

time_avg = (team1_time + team2_time) / 2

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
