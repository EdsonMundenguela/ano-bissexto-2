from datetime import date
ano = int(input('Que ano você quer analisar:'))
if ano == 0:
    ano = data.today(). year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ano bissexto {}'.format(ano))
else:
    print('o ano nao é bissexto {}'.format(ano))