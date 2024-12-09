c = 0
def F(n):
    if n <= 18:
        return n +3
    if n > 18 and n % 3 ==0:
        return (n//3) * F(n//3) + n - 12
    if n>18 and n% 3 !=0:
        return F(n-1) + n*n +5

for i in range(801):
    if all(int(j) % 2 == 0 for j in str(F(i))):
        c += 1
print(c)