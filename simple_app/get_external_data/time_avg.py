# Use with sanoma_6
from datetime import datetime

dates = ['2022-03-31T07:32:08.000Z',
         '2022-03-31T07:32:08.000Z',
         '2022-03-31T07:34:35.000Z',
         '2022-03-31T07:35:58.000Z',
         '2022-03-31T07:40:45.000Z]']




def get_arr_time(dt_list):
    for dt in dt_list:
        sum_dt_list = dt.split('T')[1].split('.')[0]
        time_obj = datetime.strptime(sum_dt_list, '%H:%M:%S').time()

        my_list = sum(map(datetime.timestamp, time_obj))
        length = len(my_list)
        average_time = datetime.fromtimestamp(my_list / length)
        result = datetime.strftime(average_time, '%H:%M:%S')
        return result




    # convert the time








print(get_arr_time(dates))
