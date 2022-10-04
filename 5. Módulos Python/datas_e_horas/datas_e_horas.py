# https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta

data1 = datetime(2022, 6, 24, 12, 47, 30)
print(data1)

print('\n------------------------------------------------------------------\n')

print(data1.strftime('%d/%m/%Y %H:%M:%S'))
# strtime(str, formato)

print('\n------------------------------------------------------------------\n')

data2 = datetime.strptime('29/03/2002', '%d/%m/%Y')
print(data2)
# .strftime(formato)

print('\n------------------------------------------------------------------\n')

print(data2.timestamp())  # Contagem de segundos desde 01/01/1970

print('\n------------------------------------------------------------------\n')

data3 = datetime.fromtimestamp(1017370800.0)
print(data3)

print('\n------------------------------------------------------------------\n')

data4 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
print(data4.strftime('%d/%m/%Y %H:%M:%S'))
data5 = data4 + timedelta(days=5, seconds=59)
print(data5.strftime('%d/%m/%Y %H:%M:%S'))

print('\n------------------------------------------------------------------\n')

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(dif)
print(dif.total_seconds())
print(dif.days)
print(d2 > d1)

print('\n------------------------------------------------------------------\n')
