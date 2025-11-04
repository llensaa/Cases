import import_files as im
import transaction_class as trans
import financial_analysis as fin
import budget_planning as bp
import ru_local as ru


def print_comprehensive_report(data):
    transactions = im.import_financial_data(data)
    categorized_transactions = trans.categorize_all_transactions(transactions)
    stats = fin.calculate_basic_stats(categorized_transactions)
    month_stats = fin.analyze_by_time(categorized_transactions)
    full_analysis = bp.complete_financial_analysis(data)
    
    print(ru.FINANCIAL_REPORT)
    
    print(ru.MAIN_RATIOS)
    print(f'{ru.INCOMES}: {stats[ru.INCOMES]:.2f} {ru.RUB}')
    print(f'{ru.EXPENSES}: {stats[ru.EXPENSES]:.2f} {ru.RUB}')
    print(f'{ru.BALANCE}: {stats[ru.BALANCE]:.2f} {ru.RUB}')
    print(ru.CATEGORY_STATS)
    
    current_stats = full_analysis[ru.HISTORICAL_ANALYSIS][ru.CURRENT_MONTH_STATS]

    sorted_categories = sorted(
    current_stats.items(),
    key=lambda x: x[1][ru.COSTS],
    reverse=True
    )

    for category, category_data in sorted_categories:
        share_percent = category_data.get(ru.COSTS_PART, 0) * 100
        print(f'{category.capitalize()}: {category_data[ru.COSTS]:.2f} {ru.RUB} ({share_percent:.0f}%)')

    print(ru.BUDGET_RECCOMENDATIONS)
    
    comparison = full_analysis[ru.COMPARISON_REPORT][ru.SUMMARY]
    if comparison[ru.OVERALL_STATUS] == ru.WITHIN_BUDGET:
        print(ru.EXCELLENT_BUDGET)
    else:
        print(f'{ru.BUDGET_EXCEEDED} {comparison[ru.TOTAL_DIFFERENCE]:.2f} {ru.RUB}')

    recommendations = full_analysis[ru.HISTORICAL_ANALYSIS][ru.RECOMMENDATIONS]
    for rec in recommendations[:2]:
        if ru.RECOMMENDED_SAVINGS in rec:
            print(f'{ru.GOAL}: {rec}')
        else:
            print(f'{ru.ATTENTION}: {rec}')

    top_categories = full_analysis[ru.HISTORICAL_ANALYSIS][ru.TOP_CATEGORIES]
    if top_categories:
        top_category = top_categories[0]
        print(f'{ru.GOAL}: {ru.REDUCE_SPENDING} {top_category["category"]} {ru.BY_PERCENT}')

    print(ru.MONTH_STATS)
    for month in month_stats:
        print(f'\n{month}:')
        category_stats = month_stats[month]
        for category in category_stats:
            print(f'  {category}: {category_stats[category][ru.COSTS]:.2f} {ru.RUB}'
                  f' ({category_stats[category][ru.COSTS_PART] * 100:.0f}%)')


if __name__ == '__main__':
    print_comprehensive_report('data.csv')

