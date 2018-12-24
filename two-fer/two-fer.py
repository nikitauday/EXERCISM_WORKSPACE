def func(X,Y):
	Z=Y if(X=="") else X
	print("One for {},one for me".format(Z))

X=input("Enter input ")
func(X,"you") 
