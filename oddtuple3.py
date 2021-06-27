oddTuples = (17, 9, 1, 0, 13, 8, 0, 20, 4, 17)
new_tuple = ()


for i, v in enumerate(oddTuples):
    
    if i == 0:
        new_tuple = new_tuple + (v,)
    elif i % 2 == 0:
        new_tuple = new_tuple + (v,)
        print(i, v)

print(new_tuple)