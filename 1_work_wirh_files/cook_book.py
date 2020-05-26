def open_file():
    cook_book = {}

    with open('recipes.txt', encoding='utf-8') as file:
        for dish in file:
            dish = dish.strip()
            cook_book[dish] = []
            counter = int(file.readline().strip())
            for name in range(counter):
                ingridient = file.readline().strip().split('|')
                dictionary = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
                cook_book[dish].append(dictionary)
            file.readline()

        return cook_book

print(open_file())

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_file('recipes.txt')
    cook_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                if ingridient['ingredient_name'] in cook_list:
                    cook_list[ingridient['ingredient_name']]['quantity'] += int((ingridient['quantity']) * person_count)
                else:
                    cook_list[ingridient['ingredient_name']] = {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * person_count}

    return cook_list


print(get_shop_list_by_dishes('Утка по-пекински', 3))