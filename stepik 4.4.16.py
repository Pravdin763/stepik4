# https://stepik.org/lesson/623073/step/14?auth=login&unit=618703
import json
import csv
from datetime import datetime


def timed(t):                        # функция для перевода даты в iso (datetime) формат
    return datetime.fromisoformat(t)

with open('exam_results.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    res = {}                      # общий словарь (ключ: емайл, значение: список[словарей])

    for n, i in enumerate(rows):    # если индекс 0, создаем словарь и делаем ключами шапку(name, "surname" итд)
        s = {}                    # словарь каждый раз обнуляется
        if n==0:
            s[i[0]], s[i[1]], s[i[2]], s[i[3]], s[i[4]] = None, None, None, None, None,    # шапка(ключи)
        else:        # присваиваем значения ключам
            s['name'], s['surname'], s['best_score'], s['date_and_time'], s['email'] = i[0], i[1], int(i[2]), i[3], i[4]
            res.setdefault(i[4], []).append(s)    # добавляем словари в список по ключу(емайл)

    for k, v in res.items():
        v = sorted(v, key= lambda z: timed(z['date_and_time']), reverse=True)  # сортируем сначала по дате(последн)
        res[k]= max(v, key=lambda x: x['best_score'])     # из списка словарей оставляем максимальное 'best_score'
    res1 = sorted(res.items(), key=lambda y: y[1]['email'])    # сортируем по емайлу
    x = [i[1] for i in res1]    # убераем ключ емайл, оставляем только словарь, тут кортеж

with open('best_scores.json', 'w', encoding='utf-8') as file2:
    json.dump(x, file2, indent='   ')
