# Get each date frm the API

dates = ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', '2022-03-07',
         '2022-03-08', '2022-03-09', '2022-03-10', '2022-03-11', '2022-03-12', '2022-03-13', '2022-03-14',
         '2022-03-15', '2022-03-16', '2022-03-17', '2022-03-18', '2022-03-19', '2022-03-20', '2022-03-21',
         '2022-03-01', '2022-03-02' '2022-03-22', '2022-03-23', '2022-03-24', '2022-03-25', '2022-03-26',
         '2022-03-27', '2022-03-28', '2022-03-29', '2022-03-30', '2022-03-31']


def date_list():
    new_list = []
    for i in dates:
        new_list.append(str(i))
    return new_list


def date_list_2(my_date):
    return my_date


## test_dates = ['2022-03-27', '2022-03-28', '2022-03-29', '2022-03-30', '2022-03-31']
## result = map(date_list_2, test_dates)

## print(list(result))


def another_list():
    testo_dates = ['2022-03-27', '2022-03-28', '2022-03-29', '2022-03-30', '2022-03-31']
    resulto = map(date_list_2, testo_dates)
    # return list(resulto)
    return resulto