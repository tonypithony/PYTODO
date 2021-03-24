# Отсортируйте словарь по значению в порядке возрастания и убывания

import operator 

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print(d)

#Сортируем в порядке возрастания:

result = dict(sorted(d.items(), key=operator.itemgetter(1)))

print(result)

#И в порядке убывания:

result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

print(result)