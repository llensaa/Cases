import transaction_class as trans
import import_files as im
from datetime import datetime


def calculate_basic_stats(transactions: list) -> dict:
    income = 0
    expenses = 0
    transactions_count = len(transactions)

    for operation in transactions:
        match operation['type']:
            case 'Доход':
                income += float(operation['amount'])
            case 'Расход':
                expenses += float(operation['amount'])
    balance = income + expenses
    stats = {'Доходы': income, 'Расходы': abs(expenses),
             'Баланс': balance, 'Количество операций': transactions_count}
    return stats


def calculate_by_category(transactions: list) -> dict:
    categories = set(operation['category'] for operation in transactions
                     if float(operation['amount']) < 0)
    categories_transactions = {}
    categories_stats = {}
    for category in categories:
        category_transactions = [operation for operation in transactions
                                 if operation['category'] == category]
        categories_transactions[category] = category_transactions

    for category in categories:
        category_transactions = categories_transactions[category]
        balance = calculate_basic_stats(category_transactions)['Расходы']
        transactions_count = calculate_basic_stats(category_transactions)['Количество операций']
        costs_part = balance / calculate_basic_stats(transactions)['Расходы']
        categories_stats[category] = {'Затраты': balance,
                                      'Количество операций': transactions_count,
                                      'Доля в общих расходах': costs_part}
    return categories_stats


def analyze_by_time(transactions: list):
    time_stats = {}
    russian_months = {1: 'Январь', 2: 'Февраль', 3: 'Март',
                      4: 'Апрель', 5: 'Май', 6: 'Июнь',
                      7: 'Июль', 8: 'Август', 9: 'Сентябрь',
                      10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    months = set([datetime.strptime(operation['date'], '%Y-%m-%d').month
                  for operation in transactions])
    for month in months:
        monthly_transactions = [operation for operation in transactions
                                if datetime.strptime(operation['date'], '%Y-%m-%d').month == month]
        month_stats = calculate_by_category(monthly_transactions)
        month_name = russian_months[month]
        time_stats[month_name] = month_stats

    return time_stats

stats = im.import_financial_data('data.csv')
for item in analyze_by_time(trans.categorize_all_transactions(stats)):
    print(f'{item}: {analyze_by_time(trans.categorize_all_transactions(stats))[item]}')
