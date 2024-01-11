a = int(input("Возраст Антона"))
b = int(input("Возраст Бориса"))
c = int(input("Возраст Виктора"))
if a > b and a > c:
    print("Антон старше всех")
elif b > a and b > c:
    print("Борис старше всех")
elif c > a and c > b:
    print("Виктор старше всех")
elif a == b > c:
    print("Антон и Борис старше Виктора")
elif b == c > a:
    print("Борис и Виктор старше Антона")
elif a == c > b:
    print("Антон и Виктор старше Бориса")

