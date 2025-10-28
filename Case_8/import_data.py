import json
from datetime import datetime


def is_valid_date(date_str: str, date_format: str = '%Y-%m-%d') -> bool:
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

def read_csv_file(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as f:
        csv_list = [line.strip().split(',') for line in f]
    return csv_list


def read_json_file(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as f:
        json_list = json.load(f)
        return json_list


def import_financial_data(filename: str) -> list:
    if filename.endswith('.csv'):
        data = read_csv_file(filename)
    else:
        data = read_json_file(filename)

    records = []

    if all(isinstance(row, list) for row in data):
        for row in data:
            if len(row) >= 4:
                date_str = row[0].strip()
                if not is_valid_date(date_str):
                    print(f'Пропущена строка с некорректной датой: {date_str}')
                    continue

                try:
                    amount = float(row[1])
                except ValueError:
                    print(f'Пропущена строка с некорректной суммой: {row[1]}')
                    continue

                record = {
                    'date': date_str,
                    'amount': amount,
                    'description': row[2].strip(),
                    'type': ''
                }
                if int(record['amount']) >= 0:
                    record['type'] += 'Доход'
                else:
                    record['type'] += 'Расход'
                records.append(record)

    elif all(isinstance(row, dict) for row in data):
        for row in data:
            if 'date' in row and is_valid_date(row['date']):
                records.append(row)
            else:
                print(f'Пропущен элемент JSON с некорректной датой: {row}')

    else:
        print(f'Файл содержит смешанные или неизвестные типы данных!')

    return sorted(records, key=lambda x: x['date'])

