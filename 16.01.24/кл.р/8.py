a = int(input("Стоимость квартиры, в рублях"))
b = int(input("Площадь квартиры,  в квадратных метрах"))
if b >= 100 and a<= 10000000 or b >= 80 and a <= 7000000:
    print("Подходит")
else:
    print("не подходит")
