import copy

orig_list = [1,2,3,4,5,6,7,8,9,10]
print("original list :", orig_list)

list_copy = copy.deepcopy(orig_list)
new_list = [i*3 for i in list_copy]
print("new list : ", new_list)
