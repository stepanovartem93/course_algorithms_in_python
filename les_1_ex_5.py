'''5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.'''

print("Программа по вводимому номеру вычисляет букву")

alph = 'abcdefghijklmnopqrstuvwxyz'

index = int(input("Введите номер буквы: "))

letter = alph[index - 1].title()

print(f'За указанным номером {index} числится буква: {letter}.')