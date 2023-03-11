import csv
import os


def load_csv() -> list:
    """загрузка данных из csv файла"""
    csv_data = []
    with open("../src/items.csv", encoding="CP1251") as csv_file:
        take_csv_data = csv.reader(csv_file, delimiter=",")
        count = 0
        for roe in take_csv_data:
            if count != 0:
                csv_data.append(roe)
            count += 1
    return csv_data