from datetime import datetime

def date_range(date: str):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    first_day = date_obj.replace(day=1)
    last_day = date_obj.replace(month=(date_obj.month + 1))
    return {
        'first': datetime.strftime(first_day, '%Y-%m-%d'),
        'last': datetime.strftime(last_day, '%Y-%m-%d')}