s = ">" + "1" *10 + "2" *20  + "3" *30
while ">1" in s or ">2" in s or ">3" in s:
    if ">1" in s:
        s = s.replace(">1","22>",1)
    else:
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        else:
            if ">3" in s:
                s = s.replace(">3", "1>", 1)
print(sum(int(x) for x in s if x != ">"))
