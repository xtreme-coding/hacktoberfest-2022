import random

numList=[]
number=9
for i in range(number):
	numList.append(random.randint(1,number))
print("[*,*,*,*,*,*,*,*,*]")
print("Guess the number from 1 to 9")
numgeuss=int(input("try your luck enter the  value\n"))
print("Number list \n ",numList)
if numgeuss in numList:
  print("Congrats you got the number !")
else:
  print("Bad luck You losse !")
