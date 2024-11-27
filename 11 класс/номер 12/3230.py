for k in range(81,90):
    s = "1" * k
    while '111' in s:
        s = s.replace('111','2',1)
        s = s.replace('2222','1',1)
    print("при",k, s)
    #ответ 83
