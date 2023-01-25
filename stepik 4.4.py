# https://stepik.org/lesson/623073/step/11?auth=login&unit=618703
import json
import csv

with open('playgrounds.csv', encoding='utf-8') as file:
    row = csv.reader(file, delimiter = ';')
    sm={}        # Общий словарь
    next(row)    # перелистываем шапку, тк. csv
    for i in row:        # в общий словарь ключ-i[1]: значение-{словарь}: ключ-i[2]:значение - список i[3]
        sm.setdefault(i[1], {}).setdefault(i[2], []).extend([i[3]])

with open('addresses.json', 'w', encoding='utf-8') as file2:
    json.dump(sm, file2, ensure_ascii=False, indent='   ')    # ensure_ascii !!