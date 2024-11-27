from random import randint
a, b = map(int,input("Введите границы диапозона:\n").split())
c = [randint(a, b) for i in range(5)]
print(" ".join(str(i) for i in c))