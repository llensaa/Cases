def read_gas_stations(filename: str) -> list[dict]:
    """Чтение данных об АЗС из файла"""
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


def read_cars_input(filename: str) -> list[dict]:
    """Чтение данных об автомобилях из файла"""
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
