def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    new_tuple = ()

    for i in aTup:
        if aTup.index(i) == 0 or aTup.index(i) % 2 == 0:
            new_tuple = new_tuple + (i,)
            print(aTup.index(i))
    return new_tuple

oddTuples((17, 9, 1, 0, 13, 8, 0, 20, 4, 17))