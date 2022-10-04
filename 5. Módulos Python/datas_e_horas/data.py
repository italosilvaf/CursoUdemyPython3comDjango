
from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')

data1 = datetime.now()
formatacao1 = data1.strftime('%A, %d de %B de %Y')
formatacao2 = data1.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)

mes_atual = int(data1.strftime('%m'))
print(mes_atual, mdays[mes_atual])
