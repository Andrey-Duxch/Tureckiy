a = int(input("Введите возраст:"))
if a % 10 == 1 and a % 100 != 11:
     print("Вам", a, "год")
elif a % 10 == 4 or a % 10 == 3 or a % 10 == 2:
     print("Вам", a, "года")
else:
     print("Вам", a, "лет")