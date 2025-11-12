from datetime import datetime
import ru_local as ru


def calculate_basic_stats(transactions: list) -> dict:
    '''
    function, summarizing all transactions and returning
    income, balance, expenses and count of all transactions
    :param: transactions 
    :return: stats
    '''
    income = 0
    expenses = 0
    transactions_count = len(transactions)

    for operation in transactions:
        match operation['type']:
            case ru.INCOME:
                income += float(operation['amount'])
            case ru.EXPENSE:
                expenses += float(operation['amount'])
    balance = income + expenses
    stats = {ru.INCOMES: income, ru.EXPENSES: abs(expenses),
             ru.BALANCE: balance, ru.AMOUNT: transactions_count}
    return stats


def calculate_by_category(transactions: list) -> dict:
    '''
    function, calculating balance, num of operations, part of all costs for every category
    :param: transactions: 
    :return: categories_stats
    '''
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
        balance = calculate_basic_stats(category_transactions)[ru.EXPENSES]
        transactions_count = calculate_basic_stats(category_transactions)[ru.AMOUNT]
        costs_part = balance / calculate_basic_stats(transactions)[ru.EXPENSES]
        categories_stats[category] = {ru.COSTS: balance,
                                      ru.AMOUNT: transactions_count,
                                      ru.COSTS_PART: costs_part}
    return categories_stats

def analyze_by_time(transactions: list) -> dict:
    '''
    function, analyzing and sorting all transactions depending on time
    :param transactions: 
    :return: time_stats
    '''
    time_stats = {}
    russian_months = {1: ru.JANUARY, 2: ru.FEBUARY, 3: ru.MARCH,
                      4: ru.APRIL, 5: ru.MAY, 6: ru.JUNE,
                      7: ru.JULY, 8: ru.AUGUST, 9: ru.SEPTEMBER,
                      10: ru.OCTOBER, 11: ru.NOVEMBER, 12: ru.DECEMBER}
    months = set([datetime.strptime(operation['date'], '%Y-%m-%d').month
                  for operation in transactions])
    for month in months:
        monthly_transactions = [operation for operation in transactions
                                if datetime.strptime(operation['date'], '%Y-%m-%d').month == month]
        month_stats = calculate_by_category(monthly_transactions)
        month_name = russian_months[month]
        time_stats[month_name] = month_stats

    return time_stats

