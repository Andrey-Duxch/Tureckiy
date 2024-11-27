a = int(input("Напишите трехзначное число"))
b = a//100
c = a//10 % 10
d = a % 10
print(b, c, d)
e = b + c
f = c + d
print(e, f)
if e >= f:
    print(str(e) + str(f))
else:
    print(str(f) + str(e))
