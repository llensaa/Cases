def create_station_queues(stations: list[dict]) -> dict:
    """Создание словаря очередей для всех АЗС"""
    return {station['num']: [] for station in stations}


def find_best_station(car: dict, stations: list[dict], queues: dict) -> int:
    """Поиск наиболее подходящей АЗС для автомобиля"""
    suitable_stations = []

    for station in stations:
        station_num = station['num']
        if (car['oil type'] in station['oil types']) \
                and (len(queues[station_num]) < station['car capacity']):
            suitable_stations.append(station_num)

    if not suitable_stations:
        return 0

    return min(suitable_stations, key=lambda x: len(queues[x]))


def add_car_to_queue(car: dict, station_num: int, queues: dict, end_time: str) -> None:
    """Добавление автомобиля в очередь АЗС"""
    car_in_queue = car.copy()
    car_in_queue['end_time'] = end_time
    queues[station_num].append(car_in_queue)


def remove_departed_cars(queues: dict, current_time: str) -> list[dict]:
    """Удаление автомобилей, закончивших заправку"""
    departed_cars = []

    for station_num, queue in queues.items():
        leaving_cars = [car for car in queue if car['end_time'] == current_time]
        for car in leaving_cars:
            queue.remove(car)
            departed_cars.append(car)

    return departed_cars