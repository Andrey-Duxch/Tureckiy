def game(s1,s2,step):
    if s1 == s2:
        return step % 2 == 0
    if step == 0:
        return 0
    h = []
    if s1<s2:
        h = [game(s1+1,s2,step-1), game(s1+3,s2,step-1)]
    if s2<s1:
        h = [game(s2+1,s1,step-1),game(s2+3,s1,step-1)]
    return any(h) if (step - 1) % 2 == 0 else all(h)
print('19', [s2 for s2 in range(1,24) if game(13,s2,2) and not game(13,s2,1) and s2!=13])
print('20', [s2 for s2 in range(1,24) if game(13,s2,3) and not game(13,s2,1) and s2!=13])
print('21', [s2 for s2 in range(1,24) if game(13,s2,4) and not game(13,s2,2) and s2!=13])