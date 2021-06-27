def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]

   
print(oddTuples((17, 9, 1, 0, 13, 8, 0, 20, 4, 17)))