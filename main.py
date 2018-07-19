from random import randint

input = ["5d12","6d4","1d2","1d8","3d6","4d20","100d100"]

for i in input:
  quantity = int(i.split('d')[0])
  faces = int(i.split('d')[1])
  rolls = [randint(1, faces) for p in range(0, int(i.split('d')[0]))]
  print(i," - ", sum(rolls),": ", (", ".join(map(str, rolls))), sep='')
  
