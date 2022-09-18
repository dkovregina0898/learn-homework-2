"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
from dataclasses import field
user_list = [
    {'name': 'Daria', 'age':'23', 'job': 'teacher'},
    {'name': 'Valeria', 'age':'22', 'job': 'translater'},
    {'name': 'Olga', 'age':'34', 'job': 'director'},
    {'name': 'Anna', 'age':'17', 'job': 'artist'},
    {'name': 'Larisa', 'age':'48', 'job': 'doctor'},
]

def main():
   with open('export.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)

if __name__ == "__main__":
    main()
