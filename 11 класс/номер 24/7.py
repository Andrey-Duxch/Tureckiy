s = open('7.txt').readline()
s  = s.replace('NPO', '1').replace('PNO', '1').replace('P', ' ').replace('N', ' ').replace('O', ' ').split()

print(max(len(i) for i in s))