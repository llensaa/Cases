import import_files as im
import transaction_class as trans
import financial_analysis as fin


def print_comprehensive_report(data):
    transactions = trans.categorize_all_transactions(im.import_financial_data(data))
    stats = fin.calculate_basic_stats(transactions)
    month_stats = fin.analyze_by_time(transactions)


    print(f'===ФИНАНСОВЫЙ ОТЧЁТ===\n')
    print('ОСНОВНЫЕ ПОКАЗАТЕЛИ:')
    for item in stats:
        if item == 'Количество операций':
            continue
        print(f'{item}: {stats[item]} руб.')

    print('\n===СТАТИСТИКА ПО МЕСЯЦАМ===\n')
    for item in month_stats:
        print(f'{item}:')
        category_stats = month_stats[item]
        for category in category_stats:
            print(f'{category}: {category_stats[category]['Затраты']} руб.'
            f'({category_stats[category]['Доля в общих расходах'] * 100:.0f}%)')
        print('\n')


if __name__ == '__main__':
    print_comprehensive_report('data.csv')
