from datetime import datetime, date, timedelta

dt_now = datetime.now()
print(dt_now)

# Напечатать в консоль даты
# Вчерашняя дата
delta = timedelta(days=1)
yesteday = dt_now - delta
print(yesteday.strftime('%d.%m.%Y'))

# Сегодняшняя дата
print(dt_now.strftime('%d.%m.%Y'))

# Месяц назад
delta = timedelta(days=30)
month_ago = dt_now - delta
print(month_ago.strftime('%d.%m.%Y'))

# Превратите строку в объект datetime
date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)