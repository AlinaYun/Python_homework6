#   Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. приоритет операций стандартный.Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# Правило вычисления: разбиваем строку на простые элементы. создаем 2 стека: для чисел и для операторов.
# Проходимся по элементам:
# 1. если это число, то добавляем его в стек для чисел
# 2. если это оператор, проверяем его приоритет:
# 2.1. если он выше последнего, находящегося в стеке, то добавляем его в стек
# 2.2. если ниже или равен, то перед добавлением в стек выполняем все операции, находящиеся в стеке, используя последние 2 числа в стеке чисел
#  и оператор в стеке операторов, пока не "наткнеся" на скобку, либо оператор с меньшим приоритетом
# 3. если это закрывающаяся скобка, то выполняем все операции, пока не "наткнемся" на открывающуюся скобку

import operator

priority = {'+': 1, '-': 1, '*': 2, '/': 2}  
operators={"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def get_list_of_tokens(string):
    list_of_tokens = []
    index = 0
    while index < len(string):        
        if string[index] in '()+-/*^':
            list_of_tokens.append(string[index])
            index += 1
            continue
        elif string[index].isdigit():
            string_builder = ''
            while string[index].isdigit():
                string_builder += string[index]
                index += 1
                if index >= len(string):
                    break
            list_of_tokens.append(int(string_builder))
        else:
            if string[index] != ' ':    #проверка корректности входных данных
                return False
            else:
                index += 1
    return list_of_tokens


def calculate (list):
    numbers_stek = []
    operators_stek = []
    for i in range(len(list)):
        if type(list[i]) == int or type(list[i]) == float:
            numbers_stek.append(list[i])
            continue
        else:
            if list[i] == ')':
                while operators_stek[-1] != '(':
                    num1 = numbers_stek.pop()
                    num2 = numbers_stek.pop()
                    numbers_stek.append(operators[operators_stek[-1]](num2, num1))    
                    operators_stek.pop()
                operators_stek.pop()
                continue
            if len(operators_stek) < 1 or list[i] == '(' or operators_stek[-1] == '(' or priority[list[i]] > priority[operators_stek[-1]]:
                operators_stek.append(list[i])
                continue
            if list[i] in priority and priority[list[i]] <= priority[operators_stek[-1]]:
                while priority[list[i]] <= priority[operators_stek[-1]]:
                    num1 = numbers_stek.pop()
                    num2 = numbers_stek.pop()
                    numbers_stek.append(operators[operators_stek[-1]](num2, num1))
                    operators_stek.pop()
                    if len(operators_stek) < 1 or operators_stek[-1] == '(':
                        break
                operators_stek.append(list[i])
                continue
    num1 = numbers_stek.pop()
    num2 = numbers_stek.pop()
    result = operators[operators_stek[-1]](num2, num1)
    return result

print (calculate(get_list_of_tokens('(1+2)*3 => 9')))




            

