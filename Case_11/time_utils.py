import math as mt
import random as rm


def time_to_minutes(time: str) -> int:
    """Преобразование времени в минуты от начала дня"""
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def minutes_to_time(minutes: int) -> str:
    """Преобразование минут в формат ЧЧ:ММ"""
    return f'{minutes // 60:02d}:{minutes % 60:02d}'


def calculate_fueling_duration(fuel_amount: int) -> int:
    """Расчет времени заправки с учетом случайных отклонений"""
    return mt.ceil(fuel_amount / 10) + rm.randint(-1, 1)


def calculate_end_time(start_time: str, fuel_amount: int) -> str:
    """Расчет времени окончания заправки"""
    start_minutes = time_to_minutes(start_time)
    duration = calculate_fueling_duration(fuel_amount)
    end_minutes = start_minutes + duration

    if end_minutes >= 1440:
        end_minutes = 1439

    return minutes_to_time(end_minutes)