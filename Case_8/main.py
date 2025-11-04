import import_files as im
import transaction_class as trans
import financial_analysis as fin
import ru_local as ru


def print_comprehensive_report(data):
    transactions = trans.categorize_all_transactions(im.import_financial_data(data))
    stats = fin.calculate_basic_stats(transactions)
    month_stats = fin.analyze_by_time(transactions)


    print(ru.FINANCIAL_REPORT)
    print(ru.MAIN_RATIOS)
    for item in stats:
        if item == ru.AMOUNT:
            continue
        print(f'{item}: {stats[item]} руб.')

    print(ru.MONTH_STATS)
    for item in month_stats:
        print(f'{item}:')
        category_stats = month_stats[item]
        for category in category_stats:
            print(f'{category}: {category_stats[category][ru.COSTS]} руб.'
            f'({category_stats[category][ru.COSTS_PART] * 100:.0f}%)')
        print('\n')


if __name__ == '__main__':
    print_comprehensive_report('data.csv')

