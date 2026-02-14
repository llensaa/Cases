import some_functions as sf


gas_st_info = sf.gas_st_read(f'gas_stations.txt')
cars_info = sf.input_read(f'input.txt')

gas_st_queue = {station['num']: 0 for station in gas_st_info}

for day in range(1440):
    hours = day // 60
    minutes = day % 60
    actual_time = f'{hours:02d}:{minutes:02d}'
