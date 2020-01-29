from datetime import datetime
import glob
import random
import os.path

dec = input('czy zamierzasz wczytać poprzednia sesje T/N')
while (dec == 'T'):
    slownik = open('slownik.txt','r') as f
    words = []
        lines = f.readlines()
        for line in lines:
            line = line.split(';')
            line[3] = line[3].strip('\n')
            t = datetime.strptime(line[3], '%m/%d/%Y').date()
            words.append({'key': line[0], 'value': line[1], 'score': int(line[2]), 'time': t})
        return words
    
    break
dec2 = input('czy zamierzasz dodać nowe słowa do słownika T/N')
while (dec2 == 'T'):
    polski = str(input('znaczenie slowa po polsku'))
    pl.append(polski)
    angielski = str(input('znaczenie slowa po angielsku'))
    en.append(angielski)
    dec3 = input('czy zamierzasz dodać nowe słowa do słownika T/N')
    if (dec3 == 'N'):
        break

for i in pl:
    value = input('Podaj znaczenie slowa',pl[i])
    if (value == en[i]):
        print('brawo')
    else:
        print('blad')





slownik = close('slownik.txt','w')

