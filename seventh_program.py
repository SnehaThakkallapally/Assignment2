x = [1,2,3,4]
l = [1,2,3,4,"a"]

z = all(isinstance(i,int)for i in x )
print(z)

z = all(isinstance(i,int)for i in l )
print(z)
	