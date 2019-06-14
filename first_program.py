x = [1,2,3,4,[10,20,30,40,[100,200,300,400],"rishabh_",5+5j],4000]
innerlist = x[4]
innermostlist= innerlist[4]

#print([x[4][0],x[4][1]])
c = innerlist[0:2]
print(c)
print(innerlist[6])

#print(x[4][6])
#print([x[4][4][2],x[4][4][3]])

z = innerlist[3:6]
a = innermostlist[2:4]
print(a)
print(z)





