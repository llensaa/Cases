import json
from datetime import datetime


def is_valid_date(date_str: str, date_format: str = "%Y-%m-%d") -> bool:
    '''
    function, checking wheteher date is correct or not
    :param: date_str
    :param: date_format
    :return: True or False
    '''
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


def read_csv_file(filename: str) -> list:
    '''
    function, reading csv file with recordings
    :param: filename
    :return: csv_list
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        csv_list = [line.strip().split(',') for line in f]
    return csv_list


def read_json_file(filename: str) -> list:
    '''
    function, reading json file with recordings
    :param: filename
    :return: json_list
    '''
    with open(filename, 'r', encoding='utf-8') as f:
        json_list = json.load(f)
        return json_list


def import_financial_data(filename: str) -> list:
    '''
    function, sorting file(csv or json) and creating a list of dictionaries from it
    :param: filename
    :return: records
    '''
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
                    print(f'Обнаружена строка с некорректной датой: {date_str}')
                    continue

                try:
                    amount = float(row[1])
                except ValueError:
                    print(f'Обнаружена строка с некорректной суммой: {row[1]}')
                    continue

                record = {
                    'date': date_str,
                    'amount': amount,
                    'description': row[2].strip(),
                    'type': row[3].strip().lower()
                }
                records.append(record)

    elif all(isinstance(row, dict) for row in data):
        for row in data:
            if 'date' in row and is_valid_date(row['date']):
                records.append(row)
            else:
                print(f'Пропущен элемент JSON с некорректной датой: {row}')

    else:
        print(f'Файл содержит смешанные или неизвестные типы данных!')

    return records
