def input_list(tiles):
    tempa=[]
    for letters in tiles[0]:
        tempa.append(letters)
    tempb=[]
    for letters in tiles[1]:
        tempb.append(letters)
    return(tempa,tempb)
    
def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
    total= 0
    for index in word:
        for index1 in index:
            total=total+score[index1.lower()]
    return total

def best_word(plays):
    word=''
    for index in plays:
        score=scrabble_score(index)
        if score>scrabble_score(word):
            word=index
    for index in word:
        word=index
    x='The best play is '+str(word)+' worth '+str(scrabble_score(word))+' points '
    return(x)
    
def possible_combos(a,b):
    import itertools
    list_of_possibilities=[]
    for index in a:
        index=index.upper()
        temp=[]
        temp.append(index)
        for index1 in b:
            temp.append(index1)
        for r in range(2,(len(temp)+1)):
            for word in itertools.permutations(temp,r):
                tlist=[''.join(word)]
                list_of_possibilities.append(tlist)
    return(list_of_possibilities)

def possible_plays(wordlist,possibilities):
    temp=[]
    for index in possibilities:
        for index1 in index:
            if index1 in wordlist:
                temp.append(index)
    return(temp)


