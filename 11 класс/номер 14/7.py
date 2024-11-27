for x in '0123456789ABCDEFGH':
    a = f'98897{x}21'
    b = f'2{x}923'
    s = int(a,19) + int(b,19)
    if s%18 == 0:
        print(s//18)
