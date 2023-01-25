# https://stepik.org/lesson/623073/step/12?auth=login&unit=618703
import json
import csv

with open('students.json', encoding='utf-8') as file:
    row = json.load(file)
    arr = []
    for i in row:
        x = {}
        if i["age"] >= 18 and i["progress"] >= 75:
            x["name"] = i["name"]
            x["phone"] = i["phone"]
            arr.append(x)
    columns = ["name", "phone"]


with open('data.csv', 'w', encoding='utf-8') as file2:
    row = csv.DictWriter(file2, fieldnames=columns)
    row.writeheader()
    for i in sorted(arr, key = lambda x: x["name"]):
        row.writerow(i)

