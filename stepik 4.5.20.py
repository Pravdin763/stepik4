# https://stepik.org/lesson/547172/step/18?auth=login&unit=540798


from datetime import datetime

def timez(x):                    # функция перевода даты и времени
    return datetime(x[0], x[1], x[2], x[3], x[4], x[5])

from zipfile import ZipFile

with ZipFile('workbook.zip') as zfile:
    s = {}                        # ключ: имя файла, значение: список f-строк (3 шт)
    for i in zfile.infolist():

        if not i.is_dir():        # отсеиваем папки
            y = []                # список, где будут храниться 3 f-строки, обновляемый
            if '/' in i.filename:    # избавляемся от пути, если еть /
                y.extend([f'  Дата модификации файла: {timez(i.date_time)}', f'  Объем исходного файла: {i.file_size} байт(а)', f'  Объем сжатого файла: {i.compress_size} байт(а)'])
                i= i.filename.split('/')[1] # избавляемся от пути
                s[i]=y      # словарь ключ: имя файла, значение [f'', f'', f'']
            else:           # если обычный файл без пути, тоже самое
                y.extend([f'  Дата модификации файла: {timez(i.date_time)}', f'  Объем исходного файла: {i.file_size} байт(а)',
                      f'  Объем сжатого файла: {i.compress_size} байт(а)'])
                s[i.filename] = y        # словарь ключ: имя файла, значение [f'', f'', f'']
    s= sorted(s.items(), key=lambda x: x[0])    # сортируем по ключу, получаем кортеж
    for i in s:
        if i==s[-1]:                # для последней строки чтобы не было лишнего отсутпа!
            print(i[0], end='\n')
            print(*i[1], sep='\n')
        else:
            print(i[0], end='\n')
            print(*i[1], sep='\n')
            print()


