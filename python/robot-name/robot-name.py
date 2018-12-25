import string
import random
unique=set()
X=input("Generate name? Y/N ")
while True :
	if(X=='Y'or X=='y'):
		while True:
			A=(''.join(random.choice(string.ascii_uppercase) for _ in range(2)))+(''.join(random.choice(string.digits) for _ in range(3)))
			if A not in unique:
				unique.add(A)
				break
		print(A)
		X=input("Generate name? Y/N ")
	elif(X=='N' or X=='n'):
		print(unique)
		break
	else:
		print("Wrong input press Y to continue and N for exit")
		X=input()
