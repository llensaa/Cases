# Константы с ценами
FUEL_PRICES = {
    'АИ-92': 63.04,
    'АИ-95': 67.32,
    'АИ-98': 83.25,
    'АИ-100': 89.10
}

def create_fuel_statistics() -> dict:
    """Создание словаря для статистики продаж топлива"""
    return {fuel: 0 for fuel in FUEL_PRICES.keys()}


def calculate_revenue(car: dict) -> float:
    """Расчет выручки от одного автомобиля"""
    return FUEL_PRICES[car['oil type']] * car['fuel amount']


def update_fuel_statistics(fuel_stats: dict, car: dict) -> None:
    """Обновление статистики продаж топлива"""
    fuel_stats[car['oil type']] += car['fuel amount']


def print_daily_statistics(fuel_stats: dict, total_revenue: float, lost_revenue: float) -> None:
    """Вывод дневной статистики"""
    print('\n=====ДНЕВНАЯ СТАТИСТИКА=====')
    print('\nПродано бензина:\n')
    for fuel, amount in fuel_stats.items():
        print(f'{fuel}: {amount} литров')

    print(f'\nОбщая сумма продаж: {total_revenue:.2f} руб')
    print(f'Упущенная выгода: {lost_revenue:.2f} руб')