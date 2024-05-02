def A(n):
    rom = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    r = " "
    i = 0
    while i < len(n):
        if i < len(n) - 1 and n[i] in rom and n[i+1] in rom:
            if rom[n[i]] < rom[n[i+1]]:
                r += str(rom[n[i+1]]) - rom[n[i]]
                i +=2
            else:
                r += str(rom[n[i]])
                i+=1
        else:
            if n[i] in rom:
                r += str(rom[n[i]])
                i +=1
            else:
                r += n[i]
    return r
n = "В MMXIII году в школе CXXIII состоялся очередной выпуск XI классов."
d =A(n)
print(d)
