import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def csv_to_json(csv_filename, json_filename, delimiter=",", line_terminator="\n"):
    # Чтение данных из CSV файла
    with open(csv_filename, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
        data = [row for row in csv_reader]

    # Сериализация данных в JSON формат
    json_data = json.dumps(data, indent=4)

    # Запись данных в JSON файл
    with open(json_filename, 'w') as json_file:
        json_file.write(json_data)

def task() -> None:
    csv_to_json(INPUT_FILENAME, OUTPUT_FILENAME)

if __name__ == '__main__':
    # Выполнение задачи
    task()

    # Печать содержимого JSON файла с отступами
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
