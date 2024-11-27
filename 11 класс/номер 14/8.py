num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 5*25**4 - 2025
num_25 = []
while num >0:
    num_25.append(num%25)
    num//=25
    print(num_25)
print(num_25.count(0))
