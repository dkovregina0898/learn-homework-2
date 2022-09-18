"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import  datetime, timedelta

def print_days():
   today = datetime.now()
   delta_yesterday = timedelta(days=1)
   delta_thirty_days = timedelta(days=30)
   yesterday = today - delta_yesterday
   thirty_days_ago = today - delta_thirty_days
   print (today.strftime('%d-%m-%Y'))
   print (yesterday.strftime('%d-%m-%Y'))
   print (thirty_days_ago.strftime('%d-%m-%Y'))


def str_2_datetime(date_string):
    date_time = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    print (date_time)


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
