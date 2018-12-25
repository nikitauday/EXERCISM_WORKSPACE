from string import ascii_lowercase

def pan(X):
	set1=set(X)
	alpha=set(ascii_lowercase)
	print(True if(alpha.issubset(X)) else False)


X=input("Enter string \n")
X=X.lower()
if all(ord(c) < 128 for c in X):
	pan(X)
else:
	print("False String")

