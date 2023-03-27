import csv
from src.csverror import InstantiateCSVError


def load_csv() -> list:
    """загрузка данных из csv файла
    :return: список нужного формата
     """
    csv_data = []
    try:
        with open("../src/items.csv", encoding="CP1251") as csv_file:
            take_csv_data = csv.reader(csv_file, delimiter=",")
            count = 0
            for roe in take_csv_data:
                if count != 0:
                    csv_data.append(roe)
                else:
                    if len(roe) != 3:
                        raise InstantiateCSVError
                    count += 1
        return csv_data
    except InstantiateCSVError:
        csv_error = InstantiateCSVError()
        print(csv_error)
        exit(1)
    except Exception:
        print("Отсутствует файл item.csv")
        exit(1)
