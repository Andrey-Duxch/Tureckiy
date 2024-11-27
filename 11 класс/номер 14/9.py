for x in range(2030,0,-1):
  num = 7**170 +7**100 - x
  num_7 = []
  while num >0:
      num_7.append(num%7)
      num//=7
  if num_7.count(0) ==71:
      print(x)
      break