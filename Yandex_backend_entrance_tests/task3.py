import json
import copy
import time

# ввод JSON-данных
json_data = input()
data = sorted(json.loads(json_data), key=lambda x: x["id"])
data_copy = copy.deepcopy(data)  # далее изменяю структуру полей data[], поэтому для вывода результата сделана копия

# ввод фильтров
filters = dict(input().split() for i in range(5))
filters["DATE_BEFORE"] = time.strptime(filters["DATE_BEFORE"],
                                       "%d.%m.%Y")  # преобразование даты в формат, пригодный для сравнения
filters["DATE_AFTER"] = time.strptime(filters["DATE_AFTER"], "%d.%m.%Y")

result = []

# доп. обработка JSON, проверка условий
for i in range(len(data)):
    data[i]["date"] = time.strptime(data[i]["date"], "%d.%m.%Y")

    if filters["NAME_CONTAINS"].lower() in data[i]["name"].lower() and \
            int(filters["PRICE_LESS_THAN"]) >= data[i]["price"] >= int(filters["PRICE_GREATER_THAN"]) and \
            filters["DATE_BEFORE"] >= data[i]["date"] >= filters["DATE_AFTER"]:
        result.append(data_copy[i])

print(json.dumps(result))
