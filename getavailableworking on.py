def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for i in lettersGuessed:
       
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        return ''.join(sorted(list.append(set(list(alphabet)).difference(set(lettersGuessed)))))
    
    
print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))