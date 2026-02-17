import file_operations as fo
import station_management as sm
import time_utils as tu
import economic_analysis as ec


def main() -> None:
    """Основная логика симуляции работы АЗС"""
    stations = fo.read_gas_stations('gas_stations.txt')
    cars = fo.read_cars_input('input_file.txt')

    queues = sm.create_station_queues(stations)
    fuel_stats = ec.create_fuel_statistics()
    total_revenue = 0
    lost_revenue = 0

    for car in cars:
        car['end_time'] = tu.calculate_end_time(car['time'], car['fuel amount'])
        car['end_minutes'] = tu.time_to_minutes(car['end_time'])

    for minute in range(1440):
        current_time = tu.minutes_to_time(minute)

        arriving_cars = [car for car in cars if car['time'] == current_time]
        for car in arriving_cars:
            best_station = sm.find_best_station(car, stations, queues)

            if not best_station:
                lost_revenue += ec.calculate_revenue(car)
                print(f'Клиент {car["time"]} {car["oil type"]} {car["fuel amount"]} '
                      f'не смог заправиться и покинул АЗС')
                continue

            sm.add_car_to_queue(car, best_station, queues, car['end_time'])
            print(f'Клиент {car["time"]} {car["oil type"]} {car["fuel amount"]}'
                  f' встал в очередь к автомату {best_station}')

            ec.update_fuel_statistics(fuel_stats, car)
            total_revenue += ec.calculate_revenue(car)

        departed_cars = sm.remove_departed_cars(queues, current_time)
        for car in departed_cars:
            print(f'В {car["end_time"]} клиент {car["time"]} {car["oil type"]} '
                  f'{car["fuel amount"]} заправил свой автомобиль и покинул АЗС')

    ec.print_daily_statistics(fuel_stats, total_revenue, lost_revenue)


if __name__ == '__main__':
    main()









