def a(n):
    div= []
    for i in range(2, n + 1, 2):
        if n % i == 0:
            div.append(i)
    return div
results = []
for number in range(190201, 190261):
    div1 = a(number)
    if len(div1) == 4:
        div1.sort(reverse=True)
        results.append((number, div1[0], div1[1]))
for number, max1 , max2 in results:
    print(number,max1,max2)
