import random as rm
import math as mt


def gas_st_read(filename):
    fuel_types = {'АИ-100', 'АИ-92', 'АИ-95', 'АИ-98'}
    gas_st_list = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()

            gas_st_list.append({
                'num': int(parts[0]),
                'car capacity': int(parts[1]),
                'oil types': [p for p in parts if p in fuel_types]
            })

    return gas_st_list


def input_read(filename):
    cars_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()

            cars_list.append({
                'time': parts[0],
                'fuel amount': int(parts[1]),
                'oil type': parts[2]
            })
    return cars_list


def queue_add(car: dict, gas_st: list[dict], gas_st_q: dict) -> int:
    suitable_st = []

    for station in gas_st:
        num = station['num']
        if (car['oil type'] in station['oil types']) \
                and (len(gas_st_q[num]) < station['car capacity']):
            suitable_st.append(num)

    if not suitable_st:
        return 0

    best_st = min(suitable_st, key=lambda x: len(gas_st_q[x]))

    return best_st


def time_for_fueling(tank_capacity: int) -> int:
    return mt.ceil(tank_capacity / 10) + rm.randint(-1, 1)


