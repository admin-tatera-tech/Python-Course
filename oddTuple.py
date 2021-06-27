def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    #new_tuple is a blank tuple to store values in
    new_tuple = ()
    
    #Creates a new for loop to interate of tuple aTup
    for i in aTup:
        
        #Checks the index value of i to see if it is odd or even
        if aTup.index(i) == 0 or aTup.index(i) % 2 == 0:
            
            #appends i to new_tuple
            new_tuple = new_tuple + (i,)
            
            #for debugging i
            print(aTup.index(i))
            
    #returns tuple new_tuple        
    return new_tuple

oddTuples((17, 9, 1, 0, 13, 8, 0, 20, 4, 17))
