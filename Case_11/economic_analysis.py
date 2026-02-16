import some_functions as sf

def transform_to_minutes(time: str) -> int:
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def revenue(car: dict) -> int:
    prices = {'АИ-92': 63.04,
              'АИ-95': 67.32,
              'АИ-98': 83.25,
              'АИ-100': 89.10}

    rev = prices[car['oil type']] * car['fuel amount']

    return rev


def petrol_stat() -> dict:
    return {'АИ-92': 0,
            'АИ-95': 0,
            'АИ-98': 0,
            'АИ-100': 0}


def count_time(car: dict) -> str:
    start = transform_to_minutes(car['time'])
    length = sf.time_for_fueling(car['fuel amount'])

    return f'{(start + length) // 60:02d}:{(start + length) % 60:02d}'


def print_stat(petrol_st: dict, rev: int, lost_rev: int) -> None:
    print('\n=====ДНЕВНАЯ СТАТИСТИКА=====')
    print('\nПродано бензина:\n')
    for petrol in petrol_st.keys():
        print(f'{petrol}: {petrol_st[petrol]} литров')

    print(f'\nОбщая сумма продаж: {rev:.2f} руб')
    print(f'\nУпущенная выгода: {lost_rev:.2f} руб')


