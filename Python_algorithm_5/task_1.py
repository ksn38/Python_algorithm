# Пользователь вводит данные о количестве предприятий, их наименования и прибыль 
# за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict

num_f = int(input('Введите данные о количестве предприятий '))
counter = 0
name_f = []
prof_f = []

while counter < num_f:
    name_f.append(input('Введите данные о наименовании предприятия '))
    prof_f.append(int(input('Введите данные о прибыли предприятий ')))
    counter += 1

#num_f = 4
#name_f = ['GMK', 'GAZ', 'TAT', 'LUK']
#prof_f = [100, 400, 300, 50]

dict_f = dict((k, v) for k, v in zip(name_f, prof_f))

dict_f['med'] = sum(prof_f)/num_f
dict_f = OrderedDict(sorted(dict_f.items(), key=lambda item: item[1]))

print('средняя прибыль', dict_f['med'])

for i in range(0, num_f + 1):
    if list(dict_f.values())[i] > dict_f['med']:
        print('выше среднего', list(dict_f.items())[i])
    elif list(dict_f.values())[i] < dict_f['med']:
        print('ниже среднего', list(dict_f.items())[i])

