def l(s, t):
    k, b = map(float, s.split("x"))
    # print(f'{k:<5}{b:<5}')
    x, y = map(float, t.split(";"))
    # print(f'{x:<5}{y:<5}')

    print(k * x + b == y)

l("1x+6", "1;7")