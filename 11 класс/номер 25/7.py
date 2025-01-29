def a(n):
    div = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            div.add(i)
            if i != n // i:
                div.add(n // i)
    return sorted(div)

def P_n(N):
    div1 = a(N)
    if len(div1) < 5:
        return 0, 0
    else:
        P = 1
        for d in div1[:5]:
            P *= d
        return P, max(div1[:5])
results = []
n = 400000001
while len(results) < 5:
    P_N, max_div1 = P_n(n)
    if P_N != 0 and P_N <= n and P_N % 100 == 17:
        results.append((n, P_N, max_div1))
    n += 1
for num, p, max_div in results:
    print(num, p, max_div)
