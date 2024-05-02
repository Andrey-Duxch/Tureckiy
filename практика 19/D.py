def A(n):
    c = 1
    c1 = []
    for i in range(len(n)):
        if n[i] == n[i+1:i+2]:
            c +=1
            continue
        c1.append(n[i] + str(c))
        c = 1
    return c1
n = input("Введите строку:")
r = A(n)
print("Закодированная строка:",''.join(r))