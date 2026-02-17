import time_utils as tu
import ru_local as ru

def create_station_queues(stations: list[dict]) -> dict:
    """
    Creates a dictionary of empty queues for each fuel station.
    
    Args:
        stations (list[dict]): List of station dictionaries.
    
    Returns:
        dict: Dictionary with station numbers as keys and empty lists as queues.
    """
    return {station[ru.car_keys['num']]: [] for station in stations}


def find_best_station(car: dict, stations: list[dict], queues: dict) -> int:
    """
    Finds the most suitable station for a car based on fuel type and current queue length.
    
    Args:
        car (dict): Car information dictionary.
        stations (list[dict]): List of station dictionaries.
        queues (dict): Dictionary of current queues per station.
    
    Returns:
        int: Number of the best station, or 0 if no suitable station found.
    """
    suitable_stations = []

    for station in stations:
        station_num = station[ru.car_keys['num']]
        if (car[ru.car_keys['oil_type']] in station[ru.station_labels['fuel_types']]) \
                and (len(queues[station_num]) < station[ru.station_labels['max_queue']]):
            suitable_stations.append(station_num)

    if not suitable_stations:
        return 0

    return min(suitable_stations, key=lambda x: len(queues[x]))


def add_car_to_queue(car: dict, station_num: int, queues: dict) -> None:
    """
    Adds a car to the queue of a specified station.
    
    Args:
        car (dict): Car information dictionary.
        station_num (int): Station number to add the car to.
        queues (dict): Dictionary of queues per station.
    """
    car_in_queue = car.copy()
    queues[station_num].append(car_in_queue)


def remove_departed_cars(queues: dict, current_time: str) -> list[dict]:
    """
    Removes cars that have finished fueling at the current time and updates end_time for the next car in queue.
    
    Args:
        queues (dict): Dictionary of queues per station.
        current_time (str): Current time in format HH:MM.
    
    Returns:
        list[dict]: List of cars that have departed.
    """
    departed_cars = []

    for station_num, queue in queues.items():
        if not queue:
            continue

        if ru.car_keys['end_time'] in queue[0] and queue[0][ru.car_keys['end_time']] == current_time:
            departed_cars.append(queue.pop(0))

            if queue:
                queue[0][ru.car_keys['end_time']] = tu.calculate_end_time(
                    current_time,
                    queue[0][ru.car_keys['fuel_amount']]
                )

    return departed_cars


def start_service_if_possible(station_num: int, queues: dict, current_time: str) -> None:
    """
    Starts fueling the first car in the queue if it is not already being served.
    
    Args:
        station_num (int): Station number.
        queues (dict): Dictionary of queues per station.
        current_time (str): Current time in HH:MM format.
    """
    queue = queues[station_num]

    if not queue:
        return

    if ru.car_keys['end_time'] in queue[0]:
        return

    fuel_amount = queue[0][ru.car_keys['fuel_amount']]
    queue[0][ru.car_keys['end_time']] = tu.calculate_end_time(current_time, fuel_amount)
