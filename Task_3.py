# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите. 
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.


alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def encoding (string_to_encode):
    enc_string = ''
    for i in string_to_encode.upper():
        if i in alph:
            enc_string += alph[(alph.find(i) + 13) % len(alph)]
        else:
            enc_string += i
    return enc_string

print(encoding(input()))

def decoding (string_to_decode):
    decode_string = ''
    for i in string_to_decode.upper():
        if i in alph:
            decode_string += alph[(alph.find(i) - 13) % len(alph)]
        else:
            decode_string += i
    return decode_string

print(decoding(input()))



