import json

def task() -> float:
    input_filename = "input.json"

    # Чтение данных из JSON файла
    with open(input_filename, 'r') as json_file:
        data = json.load(json_file)

    # Вычисление суммы произведений "score" * "weight"
    total_sum = sum(item["score"] * item["weight"] for item in data)

    # Округление суммы до 3 знаков после запятой
    rounded_sum = round(total_sum, 3)

    return rounded_sum

if __name__ == '__main__':
    # Печать результата задачи
    print(task())
