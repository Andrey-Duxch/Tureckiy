b = int(input("Введите количество мальчиков:"))
g = int(input("Введите количество девочек:"))
a = ""
if b > g * 2 or g > b * 2:
    print("Нет решений")
elif b >= g:
    n = b - g
    f = g - n
    for bgb in range(n):
        a += "BGB"
    for bg in range(f):
        a += "BG"
else:
    n = g - b
    f = b - n
    for gbg in range(n):
        a += "GBG"
    for gb in range(f):
        a += "GB"
print(a)
