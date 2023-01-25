# https://stepik.org/lesson/623073/step/11?auth=login&unit=618703
import json
import csv

with open('students.json', encoding='utf-8') as file:
    row = json.load(file)
    arr = []
    shapka = ["name", "phone"]
    for i in row:
        x={}
        if i["age"] >=18 and i["progress"]>=75:
            x[i["name"]]=i["phone"]
            arr.append(x)

with open('data.csv', 'w', encoding='utf-8') as file2:
    row = csv.writer(file2)
    row.writerow(shapka)
    for key, value in x.items():
        row.writerow(key, value)

