t = int(input("Введите количество минут"))
a = t//5
b = t - (a*5)
if b == 1 or b == 2 or b == 3 :
    print("Горит зелёный")
elif b == 0 or b == 4:
    print("Горит красный")