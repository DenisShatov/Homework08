from pprint import pprint
import os

cook_book = {}

with open('CookBook.txt') as file:
    for d in file:
        quantity = int(file.readline().strip())
        lines = []
        for item in range(quantity):
            ingredients = {}
            data = file.readline().strip().split(' | ')
            ingredients['ingredient_name'] = data[0]
            ingredients['quantity'] = int(data[1])
            ingredients['measure'] = data[2]
            lines.append(ingredients)

        cook_book[d.strip()] = lines
        file.readline().strip()

    pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for recipe in cook_book[dish]:
                if recipe['ingredient_name'] not in shopping_list:
                    shopping_list[recipe['ingredient_name']] = {'measure': recipe['measure'],
                                                                'quantity': recipe['quantity'] * person_count}
                else:
                    shopping_list[recipe['ingredient_name']]['quantity'] += recipe['quantity'] * person_count

    pprint(shopping_list)


get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Омлет'], 12)

#Задача3
work_dir = os.getcwd()
name_dir = 'sort'
list_files = os.listdir(r"sort")
files = {}

for name_file in list_files:
    with open(os.path.join(work_dir, name_dir, name_file), encoding="utf-8") as lines:
        count = sum(1 for line in lines)
        files[name_file] = count

sorted_tuples = sorted(files.items(), key=lambda x: x[1])
sorted_dict = {k: v for k, v in sorted_tuples}

with open('sorted.txt', 'a', encoding="utf-8") as sort_txt:
    for name, count_lines in sorted_dict.items():
        sort_txt.write(f'{name}\n{count_lines}\n')
        with open(os.path.join(work_dir, name_dir, name), encoding="utf-8") as texts:
            for text in texts:
                x = text.strip()
                sort_txt.write(f'{x}\n')





