s = open('8.txt').readline()
s  = s.replace('BA', '1').replace('BO', '1').replace('CA', '1').replace('CO', '1').replace('DA', '1').replace('DO', '1').replace('B', ' ').replace('D', ' ').replace('C', ' ').replace('A', ' ').replace('O', ' ').split()
print(max(len(i) for i in s))