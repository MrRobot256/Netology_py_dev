print('Приветствуем в задании №1 по польской нотации!')
print('Команды для работы:')
print('s - сумма чисел')
print('v - вычитание чисел')
print('d - деление чисел')
print('m - умножение числе')
print('q - выход из программы')

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 's':
            summ()
        elif user_input == 'v':
            subtraction()
        elif user_input == 'd':
            division()
        elif user_input == 'm':
            multiplication()
        elif user_input == 'q':
            print('Выход из спрограммы')
            break

def summ():
    '''Функция суммы чисел'''
    try:
        user_input1 = int(input('Введите 1 число: '))
        user_input2 = int(input('Введите 2 число: '))
        user_input3 = input('Введите операнд: ')

        if user_input3 == '+':
            result = user_input1 + user_input2
            print(f'По Польской нотации Ваш пример: {user_input3} {user_input1} {user_input2}')
            print(result)
            return result
        else:
            print('Вы выбрали сложение. Введите "+"!')
    except Exception as e:
        print(f'Вы допустили ошибку!{e}')

def subtraction():
    '''Функция вычитания чисел'''
    try:
        user_input1 = int(input('Введите 1 число: '))
        user_input2 = int(input('Введите 2 число: '))
        user_input3 = input('Введите операнд: ')
        if user_input3 == '-':
            result = user_input1 - user_input2
            print(f'По Польской нотации Ваш пример: {user_input3} {user_input1} {user_input2}')
            print(result)
            return result
        else:
            print('Вы выбрали вычитания. Введите "-"!')
    except Exception as e:
        print(f'Вы допустили ошибку!{e}')

def division():
    '''Функция деления чисел'''
    try:
        user_input1 = int(input('Введите 1 число: '))
        user_input2 = int(input('Введите 2 число: '))
        user_input3 = input('Введите операнд: ')
        if user_input3 == '/':
            result = user_input1 / user_input2
            print(f'По Польской нотации Ваш пример: {user_input3} {user_input1} {user_input2}')
            print(result)
        elif user_input3 == '//':
            result = user_input1 // user_input2
            print(f'По Польской нотации Ваш пример: {user_input3} {user_input1} {user_input2}')
            print(result)
            return result
        else:
            print('Вы выбрали деление. Введите "/"!')
    except ZeroDivisionError as e:
        print(f"Деление на ноль! Так нельзя! текст исключения: {e}")

def multiplication():
    '''Функция умножения чисел'''
    try:
        user_input1 = int(input('Введите 1 число: '))
        user_input2 = int(input('Введите 2 число: '))
        user_input3 = input('Введите операнд: ')
        if user_input3 == '*':
            result = user_input1 * user_input2
            print(f'По Польской нотации Ваш пример: {user_input3} {user_input1} {user_input2}')
            print(result)
            return result
        else:
            print('Вы выбрали умножение. Введите "*"!')
    except Exception as e:
        print(f'Вы допустили ошибку!{e}')

main()