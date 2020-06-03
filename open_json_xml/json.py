import json

def open_json(file):
    with open(file, encoding='utf-8') as file_json:
        info = json.load(file_json)
        list_date = []

        for item in info['rss']['channel']['items']:
            list_date.append(item['description'])

    return list_date


def get_ten_rated(descriptions_list):
    dict_word = {}
    rated_list = []

    for word in descriptions_list:
        if len(word) > 6:
            if word in dict_word:
                dict_word[word] += 1
            else:
                dict_word[word] = 1
        else:
            continue

    for key, value in dict_word.items():
        rated_list.append((value, key))
    rated_list.sort(reverse=True)

    for item in rated_list[:10]:
        print(f'{item[1]}: {item[0]}')


get_ten_rated(open_json('newsafr.json'))