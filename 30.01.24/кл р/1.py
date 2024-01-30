m = 185
c = 0
for i in range(m//15):
    for j in range(m//17):
        for k in range(m//21):
            if (i * 15 + j * 17 + k * 21) > 185:
                break
            elif (i * 15 + j * 17 + k * 21) == 185:
                c += 1
                # print(i,j,k,i * 15 + j * 17 + k * 21)
print(c)
