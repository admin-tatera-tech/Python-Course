def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for i in lettersGuessed:
       
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        #Need to return alphabet if the list of lettersGuessed is empty, but not sure how
        return ''.join(sorted(list.append(set(list(alphabet)).difference(set(lettersGuessed)))))
    
# works when player has guessed a letter but not when list is empty  
print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))
