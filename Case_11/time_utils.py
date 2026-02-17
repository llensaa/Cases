import math as mt
import random as rm
import ru_local as ru

def time_to_minutes(time: str) -> int:
    """
    Converts time in HH:MM format to total minutes from start of the day.
    
    Args:
        time (str): Time string in format HH:MM.
    
    Returns:
        int: Total minutes since 00:00.
    """
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes


def minutes_to_time(minutes: int) -> str:
    """
    Converts total minutes to HH:MM format.
    
    Args:
        minutes (int): Total minutes from start of the day.
    
    Returns:
        str: Time string in format HH:MM.
    """
    return f'{minutes // 60:02d}:{minutes % 60:02d}'


def calculate_fueling_duration(fuel_amount: int) -> int:
    """
    Calculates the fueling duration in minutes based on fuel amount.
    The speed is 10 liters per minute with a random variation of -1, 0, or +1 minute.
    Minimum duration is 1 minute.
    
    Args:
        fuel_amount (int): Amount of fuel in liters.
    
    Returns:
        int: Duration in minutes.
    """
    duration = mt.ceil(fuel_amount / 10) + rm.randint(-1, 1)
    return max(1, duration)


def calculate_end_time(start_time: str, fuel_amount: int) -> str:
    """
    Calculates the end time of fueling based on start time and fuel amount.
    
    Args:
        start_time (str): Start time in HH:MM format.
        fuel_amount (int): Amount of fuel in liters.
    
    Returns:
        str: End time in HH:MM format.
    """
    start_minutes = time_to_minutes(start_time)
    duration = calculate_fueling_duration(fuel_amount)
    end_minutes = start_minutes + duration

    if end_minutes >= 1440:
        end_minutes = 1439

    return minutes_to_time(end_minutes)
