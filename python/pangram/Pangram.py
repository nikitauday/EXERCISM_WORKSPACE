def pan(X):
	set1=set(X)
	if (len(set1)==26):
		print("String is a pangram")
	else:
		print("String is not a pangram")
X=input("Enter string \n")
X=X.replace(" ", "")
X=X.lower()
if all(x.isalpha() for x in X):
	pan(X)
else:
	print("String should not contain special characters")

