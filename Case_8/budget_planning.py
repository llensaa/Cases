import transaction_class as trans
import import_files as im
import financial_analysis as fin
from datetime import datetime
import ru_local as ru


def analyze_historical_spending(transactions: list) -> dict:
    if not transactions:
        return {
            ru.AVERAGE_BY_CATEGORY: {},
            ru.SEASONAL_PATTERNS: {},
            ru.TOP_CATEGORIES: [],
            ru.RECOMMENDATIONS: [ru.NO_DATA_FOR_ANALYSIS],
            ru.CURRENT_MONTH_STATS: {}
        }
    
    categorized_transactions = trans.categorize_all_transactions(transactions)
    time_stats = fin.analyze_by_time(categorized_transactions)
    
    category_totals = {}
    category_counts = {}
    
    for month, month_data in time_stats.items():
        for category, stats in month_data.items():
            if category not in category_totals:
                category_totals[category] = 0
                category_counts[category] = 0
            category_totals[category] += stats[ru.COSTS]
            category_counts[category] += 1
    
    average_by_category = {}
    for category in category_totals:
        if category_counts[category] > 0:
            average_by_category[category] = (
                category_totals[category] / category_counts[category]
            )
    
    seasonal_patterns = {}
    for category in average_by_category:
        monthly_data = {}
        for month, month_data in time_stats.items():
            if category in month_data:
                monthly_data[month] = month_data[category][ru.COSTS]
        seasonal_patterns[category] = monthly_data
    
    current_stats = fin.calculate_by_category(categorized_transactions)
    sorted_categories = sorted(
        current_stats.items(),
        key=lambda x: x[1][ru.COSTS],
        reverse=True
    )
    
    top_categories = []
    for category, stats in sorted_categories[:3]:
        share = stats.get(ru.COSTS_PART, 0)
        top_categories.append({
            'category': category,
            'amount': stats[ru.COSTS],
            'share': share,
            'share_percent': share * 100
        })
    
    recommendations = []
    
    if top_categories:
        recommendations.append(
            f"{ru.BIGGEST_SPENDING} "
            f"'{top_categories[0]['category']}' - "
            f"{top_categories[0]['amount']:.2f} {ru.RUB} "
            f"({top_categories[0]['share_percent']:.1f}% {ru.PERCENT_OF_ALL_EXPENSES})"
        )
    
    for category, monthly_data in seasonal_patterns.items():
        if len(monthly_data) >= 3:
            max_month = max(monthly_data, key=monthly_data.get)
            min_month = min(monthly_data, key=monthly_data.get)
            if monthly_data[max_month] > monthly_data[min_month] * 1.5:
                recommendations.append(
                    f"{ru.SEASONALITY_DETECTED} '{category}': "
                    f"{ru.PEAK_MONTH} - {max_month} ({monthly_data[max_month]:.2f} {ru.RUB})"
                )
    
    total_expenses = fin.calculate_basic_stats(categorized_transactions)[ru.EXPENSES]
    if total_expenses > 0:
        recommendations.append(
            f"{ru.RECOMMENDED_SAVINGS} 15%: "
            f"{total_expenses * 0.15:.2f} {ru.RUB}"
        )
    
    return {
        ru.AVERAGE_BY_CATEGORY: average_by_category,
        ru.SEASONAL_PATTERNS: seasonal_patterns,
        ru.TOP_CATEGORIES: top_categories,
        ru.RECOMMENDATIONS: recommendations,
        ru.CURRENT_MONTH_STATS: current_stats
    }


def create_budget_template(analysis: dict) -> dict:
    if not analysis.get(ru.AVERAGE_BY_CATEGORY):
        return {
            ru.METADATA: {
                ru.ERROR: ru.NO_DATA_FOR_BUDGET,
                ru.CREATION_DATE: datetime.now().strftime('%Y-%m-%d')
            }
        }
    
    budget_limits = {}
    for category, avg_amount in analysis[ru.AVERAGE_BY_CATEGORY].items():
        budget_limits[category] = avg_amount * 0.9
    
    total_budget_expenses = sum(budget_limits.values())
    
    savings_category = {ru.SAVINGS: total_budget_expenses * 0.15}
    emergency_category = {ru.EMERGENCY: total_budget_expenses * 0.1}
    
    budget_template = {
        **budget_limits,
        **savings_category,
        **emergency_category
    }
    
    budget_template[ru.METADATA] = {
        ru.TOTAL_PLANNED_EXPENSES: total_budget_expenses,
        ru.SAVINGS_PERCENTAGE: 15,
        ru.EMERGENCY_PERCENTAGE: 10,
        ru.CREATION_DATE: datetime.now().strftime('%Y-%m-%d')
    }
    
    return budget_template


def compare_budget_vs_actual(budget: dict, actual_transactions: list) -> dict:
    if not actual_transactions:
        return {
            ru.CATEGORY_COMPARISON: {},
            ru.SUMMARY: {
                ru.TOTAL_BUDGET: 0,
                ru.TOTAL_ACTUAL: 0,
                ru.TOTAL_DIFFERENCE: 0,
                ru.OVERALL_STATUS: ru.NO_DATA
            },
            ru.EXCEEDED_CATEGORIES: [],
            ru.WITHIN_BUDGET_CATEGORIES: []
        }
    
    categorized_transactions = trans.categorize_all_transactions(actual_transactions)
    actual_stats = fin.calculate_by_category(categorized_transactions)
    
    comparison = {}
    total_budget = 0
    total_actual = 0
    
    clean_budget = {
        k: v for k, v in budget.items()
        if not k.startswith('_')
    }
    
    all_categories = set(
        list(clean_budget.keys()) + list(actual_stats.keys())
    )
    
    for category in all_categories:
        budget_amount = clean_budget.get(category, 0)
        actual_amount = actual_stats.get(category, {}).get(ru.COSTS, 0)
        
        total_budget += budget_amount
        total_actual += actual_amount
        
        difference = actual_amount - budget_amount
        
        if budget_amount > 0:
            percentage = (actual_amount / budget_amount) * 100
        else:
            percentage = 100 if actual_amount == 0 else float('inf')
        
        status = ru.WITHIN_BUDGET if actual_amount <= budget_amount else ru.EXCEEDED
        
        comparison[category] = {
            ru.BUDGET_AMOUNT: budget_amount,
            ru.ACTUAL_AMOUNT: actual_amount,
            ru.DIFFERENCE: difference,
            ru.PERCENTAGE: percentage,
            ru.STATUS: status
        }
    
    overall_status = ru.WITHIN_BUDGET if total_actual <= total_budget else ru.EXCEEDED
    
    return {
        ru.CATEGORY_COMPARISON: comparison,
        ru.SUMMARY: {
            ru.TOTAL_BUDGET: total_budget,
            ru.TOTAL_ACTUAL: total_actual,
            ru.TOTAL_DIFFERENCE: total_actual - total_budget,
            ru.OVERALL_STATUS: overall_status
        },
        ru.EXCEEDED_CATEGORIES: [
            category for category, data in comparison.items()
            if data[ru.STATUS] == ru.EXCEEDED
        ],
        ru.WITHIN_BUDGET_CATEGORIES: [
            category for category, data in comparison.items()
            if data[ru.STATUS] == ru.WITHIN_BUDGET
        ]
    }


def complete_financial_analysis(filename: str) -> dict:
    try:
        transactions = im.import_financial_data(filename)
        if not transactions:
            return {ru.ERROR: ru.FILE_EMPTY_OR_INVALID}
        
        historical_analysis = analyze_historical_spending(transactions)
        budget_template = create_budget_template(historical_analysis)
        comparison_report = compare_budget_vs_actual(budget_template, transactions)
        
        return {
            ru.HISTORICAL_ANALYSIS: historical_analysis,
            ru.BUDGET_TEMPLATE: budget_template,
            ru.COMPARISON_REPORT: comparison_report
        }
    except FileNotFoundError:
        return {ru.ERROR: ru.FILE_NOT_FOUND.format(filename=filename)}
    except (ValueError, TypeError) as e:
        return {ru.ERROR: ru.ANALYSIS_ERROR.format(error=str(e))}