import file_operations as fo
import station_management as sm
import time_utils as tu
import economic_analysis as ec
import ru_local as ru


def main() -> None:
    """
    Main simulation logic for the gas station operation.

    Loads station and car data, simulates the arrival of cars,
    queue management, fueling process, and prints status updates
    after each event. At the end of the simulation, prints daily
    statistics including total fuel sold, revenue, and lost revenue.

    Args:
        None

    Returns:
        None
    """
    stations = fo.read_gas_stations('Cases/Case_11/gas_stations.txt')
    cars = fo.read_cars_input('Cases/Case_11/input_file.txt')

    queues = sm.create_station_queues(stations)
    fuel_stats = ec.create_fuel_statistics()
    total_revenue = 0
    lost_revenue = 0

    for minute in range(1440):
        current_time = tu.minutes_to_time(minute)
        arriving_cars = [
            car for car in cars if car[ru.car_keys['time']] == current_time
        ]

        for car in arriving_cars:
            best_station = sm.find_best_station(car, stations, queues)

            if not best_station:
                lost_revenue += ec.calculate_revenue(car)
                print(
                    f"{ru.messages['new_client']} {car[ru.car_keys['time']]} "
                    f"{car[ru.car_keys['oil_type']]} {car[ru.car_keys['fuel_amount']]} "
                    f"{ru.messages['client_unserved']}"
                )
                ec.print_station_status(stations, queues)
                continue

            sm.add_car_to_queue(car, best_station, queues)
            sm.start_service_if_possible(best_station, queues, car[ru.car_keys['time']])

            print(
                f"{ru.messages['new_client']} {car[ru.car_keys['time']]} "
                f"{car[ru.car_keys['oil_type']]} {car[ru.car_keys['fuel_amount']]} "
                f"{ru.messages['client_added']} №{best_station}"
            )
            ec.print_station_status(stations, queues)

            ec.update_fuel_statistics(fuel_stats, car)
            total_revenue += ec.calculate_revenue(car)

        departed_cars = sm.remove_departed_cars(queues, current_time)
        for car in departed_cars:
            print(
                f"{ru.messages['client_departed']} {car[ru.car_keys['end_time']]} "
                f"{car[ru.car_keys['time']]} {car[ru.car_keys['oil_type']]} "
                f"{car[ru.car_keys['fuel_amount']]}"
            )
            ec.print_station_status(stations, queues)

    ec.print_daily_statistics(fuel_stats, total_revenue, lost_revenue)


if __name__ == '__main__':
    main()
