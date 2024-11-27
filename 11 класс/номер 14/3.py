num = 15 + 2**10 +16
num_16 = []
while num >0:
    num_16.append(num%16)
    num//=16
print(num_16.count(15))
