a = input("Введите строку:\n")
b = input("Что меняем?")
c = input("Чем заменить?")
d = [i for i in a.split(b)]
print("Результат:\n" + c.join(d))