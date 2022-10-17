import csv
import re
import camelot
import pandas as pd

hostel = 'Umiam'
timings = {
    'breakfast': '7:30AM - 9:45AM',
    'lunch': '12:00PM - 2:15PM',
    'dinner': '8:00PM - 10:15PM'
}
holiday_timings = {
    'breakfast': '8:00AM - 10:15AM',
    'lunch': '12:15PM - 2:30PM',
    'dinner': '8:00PM - 10:15PM'
}
use_holiday_time = False
merge_tables = False


def get_day(str):
    str = str.replace(' ', '')
    str = str.strip()
    first = str[0].lower()
    second = str[1].lower()
    if (first == 'w'):
        return "Wednesday"
    elif (first == 'm'):
        return "Monday"
    elif (first == 'f'):
        return "Friday"
    elif (first == 't'):
        if (second == 'u'):
            return "Tuesday"
        else:
            return "Thursday"
    else:
        if (second == 'u'):
            return "Sunday"
        else:
            return "Saturday"


def get_mess_csv():
    tables = camelot.read_pdf(
        f'PDFs/{hostel}.pdf', strip_text='\n', pages='all')
    df = tables[0].df

    if (tables.n > 1 and merge_tables):
        df = pd.concat([df, tables[1].df], ignore_index=True)

    df.columns = ['day', 'breakfast', 'lunch', 'dinner']
    df.drop(0, inplace=True)

    mess_menu = pd.DataFrame(
        columns=['hostel', 'day', 'meal', 'menu', 'timing'])
    #hostel,day, meal, menu, timing
    for i in df.index:
        meals = ['breakfast', 'lunch', 'dinner']
        for j in range(3):
            dict = {'hostel': [hostel]}
            dict['day'] = [get_day(df['day'][i])]
            dict['meal'] = [meals[j]]
            dict['menu'] = [df[meals[j]][i]]
            dict['timing'] = [timings[meals[j]]]
            if (dict['day'][0].lower() in ['saturday', 'sunday', 'sat', 'sun'] and use_holiday_time == True):
                dict['timing'] = [holiday_timings[meals[j]]]
            mess_day = pd.DataFrame(dict)
            mess_menu = pd.concat([mess_menu, mess_day], ignore_index=True)

    # mess_menu['menu'] = mess_menu['menu'].apply(
    #     lambda x: re.sub("\s*\d.", " ", x))
    mess_menu.to_csv(f'{hostel}.csv', index=False,
                     quoting=csv.QUOTE_NONNUMERIC)


get_mess_csv()
