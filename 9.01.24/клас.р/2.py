import math
a1, b1 = [float(i) for i in input().split()]
a2, b2 = [float(i) for i in input().split()]
print(math.sqrt(((a2-a1)**2)+((b2-b1)**2)))