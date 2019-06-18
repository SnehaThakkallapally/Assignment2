#list = [1,2,3,4,5,6]
#items = [1, 2, 3, 5, 6]
items = range(1, 22) 
#print(list(items))
even_pair = [(items[i],items[j]) for i in range(len(items)) for j in range(i+1, len(items)) 
if((items[i]+items[j])%2 == 0 and (items[i]+items[j]) in range(22)) ]

print(even_pair)
