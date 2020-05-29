from context_manager import Start_code

print('Приветствуем в задании №1 по польской нотации!')
print('Команды для работы:')
print('s - запустить польскую нотацию')
print('q - выход из программы')

def main():
    with Start_code ('log_file.txt'):
        while True:
            user_input = input('Введите команду: ')
            if user_input == 's':
                polish_notation()
            elif user_input == 'q':
                print('Выход из спрограммы')
                break

def polish_notation():
    try:
        user_input = input('Введите пример в формате маски через пробелы (+ 1 2): ')
        keys = user_input.split()
        key1 = str(keys[0])
        key2 = int(keys[1])
        key3 = int(keys[2])
        assert len(keys) == 3, 'Вы превысили лимит'

        try:
            if key1 == '-':
                result = key2 - key3
                return print(result)
            elif key1 == '+':
                result = key2 + key3
                return  print(result)
            elif key1 == '/':
                result = key2 / key3
                return print(result)
            elif key1 == '//':
                result = key2 // key3
                return print(result)
            elif key1 == '*':
                result = key2 * key3
                return print(result)
            else:
                print('Вы где-то допустли ошибку, будьте внимательны!')

        except ZeroDivisionError as e:
            print(f'Делить на 0 нельзя! текст ошибки: {e}')

    except AssertionError as e:
        print(f'Попробуйте еще раз! текст ошибки: {e}')

    except ValueError as e:
        print(f'Вы ввели буквы! ошибка: {e}')

main()