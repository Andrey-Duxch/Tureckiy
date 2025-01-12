def f(c, e, flag = False, flag1 = False):
    if c == 9:
        flag = True
    if c == 12:
        flag1 = True
    if c > e:
        return 0
    if c == e:
        return flag and flag1
    if c < e:
        return f(c+1,e, flag, flag1)+ f(c*2, e, flag, flag1) + f(c+3, e, flag, flag1)
print(f(3,20))