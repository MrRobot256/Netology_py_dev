documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            ask_document_author()
        elif user_input == 's':
            ask_document_shelf()
        elif user_input == 'l':
            print_list()
        elif user_input == 'a':
            add_document()
        elif user_input == 'c':
            create_key_errors()
        elif user_input == 'q':
            print('Выход из спрограммы')
            break


def ask_document_author():
    '''
    команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    '''

    ask_document = input('Введите номер документа: ')
    document_value = []

    for document in documents:
        for key, value in document.items():
            if ask_document in document.values():
                document_value.append(value)
    print('Автор документа - ', document_value[2])
    return


def ask_document_shelf():
    '''
    команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
    '''

    ask_document = input('Введите номер документа: ')

    for shelf, document in directories.items():
        if ask_document in document:
            print(f'Документ на полке № {shelf}')
            return
    print('Нет такого документа')


def print_list():
    '''
    команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    '''
    for document in documents:
        print(document["number"], document["name"])
    return


def add_document():
    '''
    команда, которая добавит новый документ в каталог и в перечень полок,
    спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
    '''
    document_number = input('Номер документа: ')
    document_type = input('Тип ')
    document_author = input('Имя владельца: ')
    document_shelf = input('Номер полки: ')
    if document_shelf in directories.keys():
        documents.append({'type': document_type, 'number': document_number, 'name': document_author})
        directories[document_shelf].append(document_number)
        print('Документ добавлен')
        print(documents, directories)
    else:
        print('Введен неверный номер полки')

def create_key_errors():
    '''
    Задание 3
    Расширить домашние задание из лекции 2.1 «Функции — использование встроенных и создание собственных»
    новой функцией, выводящей имена всех владельцев документов.
    С помощью исключения KeyError проверяйте, есть ли поле "name" у документа.
    '''
    user_input = input('Введите номер документа: ')
    document_value = []

    try:
        for document in documents:
            for key, value in document.items():
                if user_input in document.values():
                    document_value.append(value)
        print(document_value[2])
    except Exception as e: #если документа не существует, ловим ошибку, выходим из функции и переходим к циклу
        print(f'Введены неверные данные! текст ошибки: {e}')
    return

main()
