s = 0
d = 0
x = 1
for i in range(1, 101):
    k = 1/i
    d = d + k*x*(-1)**(i-1)
    s = s + k * x
    x = k
print("Мужчина будет находиться в", d, "км. от дома")
print("Общий путь, который прошел мужчина = ", s, "км.")
