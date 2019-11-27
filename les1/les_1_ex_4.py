'''4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.'''
print("Введите две буквы алфавита")

alph = 'abcdefghijklmnopqrstuvwxyz'

first = input("\tвведите первую букву: ")
second = input("\tвведите вторую букву: ")

first_index = alph.index(first) + 1
second_index = alph.index(second) + 1
diff = abs((first_index - second_index) + 1)

print(f'первая буква имеет индекс: {first_index}; \n вторая буква имеет индекс: {second_index};'
      f'\n количество букв между этими двумя буквами равно {diff}.')
