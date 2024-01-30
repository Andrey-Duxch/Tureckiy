a = 10
b = 5
c = 0.5
for i in range(11):
    for j in range(21):
        for k in range(201):
            s = i * a + j * b + k * c
            g = i + k + j
            if s <= 100 and g == 100:
                print(f' быков {i}, коров {j}, телят {k}, остаток {100 - s} руб  ')