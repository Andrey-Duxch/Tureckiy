for k in range(301,320):
    s = "5" * k
    while '555' in s or '888' in s:
        s = s.replace('555','8',1)
        s = s.replace('888','55',1)
    print("при", k, s)
    #Ответ: 305
    #уникальных: 7