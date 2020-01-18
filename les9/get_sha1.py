import hashlib

print(hashlib.sha1(b'Hello World!').hexdigest())
# буква "b" означает байт-строка
# ф-я sha1 - функция хеширования

print(hashlib.sha1(b'Hello World.').hexdigest())
# стоит изменить хотя бы одну букву, хеш менятеся целиком

s = hashlib.sha1(b'Hello World.').hexdigest()

print(s.encode('utf-8')) #меняется из byte в кодировку utf-8

print(hashlib.sha1(b'qwefdg'+ bytes(s.encode('utf-8'))).hexdigest())  #'qwefdg' - это секретное слово