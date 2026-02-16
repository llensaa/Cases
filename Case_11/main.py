import some_functions as sf
import economic_analysis as ef


def main():
    gas_st_info = sf.gas_st_read('gas_stations')
    cars_info = sf.input_read('input_file')
    petrol_info = ef.petrol_stat()

    for car in cars_info:
        car['fuel_end_time'] = ef.count_time(car)
        car['fuel_end_minutes'] = ef.transform_to_minutes(car['fuel_end_time'])

    lost_rev = 0
    total_rev = 0

    gas_st_queue = {station['num']: [] for station in gas_st_info}

    for minute in range(1440):
        current_time = f'{minute // 60:02d}:{minute % 60:02d}'

        current_cars = [car for car in cars_info if car['time'] == current_time]
        for car in current_cars:
            best_st = sf.queue_add(car, gas_st_info, gas_st_queue)

            if not best_st:
                lost_rev += ef.revenue(car)
                print(f'Клиент {car['time']} {car['oil type']} {car['fuel amount']} '
                      f'не смог заправиться и покинул АЗС')
                continue


            car_in_queue = car.copy()
            car_in_queue['end_time'] = car['fuel_end_time']
            gas_st_queue[best_st].append(car_in_queue)

            print(f'Клиент {car['time']} {car['oil type']} {car['fuel amount']} встал в очередь к автомату {best_st}')
            petrol_info[car['oil type']] += car['fuel amount']
            total_rev += ef.revenue(car)

        for st_num, queue in gas_st_queue.items():
            leaving_cars = [car for car in queue if car['end_time'] == current_time]
            for car in leaving_cars:
                queue.remove(car)
                print(f'В {car['end_time']} клиент {car['time']} {car['oil type']} {car['fuel amount']} заправил свой автомобиль и покинул АЗС')

    ef.print_stat(petrol_info, total_rev, lost_rev)


if __name__ == '__main__':
    main()















