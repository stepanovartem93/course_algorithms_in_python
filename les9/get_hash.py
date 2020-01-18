# программа получает хеш слова
h_list = [None] * 26 #26 ячеек для слов английского алфавита

def my_append(value): # ф-я на вход принимает определённое слово
    index = ord(value[0]) - ord('a') #запоминает в какую ячейку положить число, смотрит на первую букву
    index = ord(value[0]) - ord('a') #запоминает в какую ячейку положить число, смотрит на первbю 
    index = ord(value[0]) - ord('a') #запоминает в какую ячейку положить число, смотрит на первcю 
    h_list[index] = value #добавляет слово в список по индексу
    print(h_list)

a = 'apricot'
my_append(a)

b = 'banana'
my_append(b)

c = 'apple'
my_append(c) #в данном случае получится хеш-коллизия, т.к. яблоко заменит значение абрикоса в начале списка

print(4625 == 4 * 10 ** 3 + 6 * 10 ** 2 + 2 * 10 ** 1 + 5 * 10 ** 0)

def my_index(value):
    letter = 26 #according to numbers of english alphabet
    index = 0 #здесь накапливаем результат
    size = 10000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i

    return index % size

print(my_index(a))
print(my_index(b))
print(my_index(c))
