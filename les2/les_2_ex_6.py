'''6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться,
больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.'''
import random

print("Игра 'Угадай число'")
attempt = 0
n = random.randint(0, 100)

while attempt < 10:
    number = int(input("Введите предполагаемое число: "))
    if number < n:
        print("Слишком мало")
        attempt += 1
    elif number > n:
        print("Слишком много")
        attempt += 1
    else:
        print(f'Поздравляю, вы отгадали число {n} с {attempt} попытки')
        break
else:
    print(f'Вы не угадали за 10 попыток, было загадано число {n}')
