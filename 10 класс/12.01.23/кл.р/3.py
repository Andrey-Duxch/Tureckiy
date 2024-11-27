from random import *
a = randint(1, 999)
print('Число',a)
print('Сотни:', a//100)
print('Десятки:', a%100//10)
print('Единицы:', a%10)
