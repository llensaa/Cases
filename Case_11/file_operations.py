import ru_local as ru

def read_gas_stations(filename: str) -> list[dict]:
    """
    Reads fuel station data from a file.
    
    Args:
        filename (str): Path to the file containing gas station data.
    
    Returns:
        list[dict]: List of dictionaries, each representing a fuel station with:
            - 'num': station number
            - 'car capacity': maximum queue length
            - 'oil types': list of fuel types served
    """
    fuel_types = {'АИ-100', 'АИ-92', 'АИ-95', 'АИ-98'}
    gas_st_list = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()
            gas_st_list.append({
                ru.car_keys['num']: int(parts[0]),
                ru.station_labels['max_queue']: int(parts[1]),
                ru.station_labels['fuel_types']: [p for p in parts if p in fuel_types]
            })
    return gas_st_list


def read_cars_input(filename: str) -> list[dict]:
    """
    Reads car arrival data from a file.
    
    Args:
        filename (str): Path to the file containing car data.
    
    Returns:
        list[dict]: List of dictionaries, each representing a car with:
            - 'time': arrival time (HH:MM)
            - 'fuel amount': requested liters
            - 'oil type': fuel type
    """
    cars_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()
            cars_list.append({
                ru.car_keys['time']: parts[0],
                ru.car_keys['fuel_amount']: int(parts[1]),
                ru.car_keys['oil_type']: parts[2]
            })
    return cars_list
