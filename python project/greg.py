def list_of_words():
    try:
        f=open('scrabble_words.txt','r')
        words=[]
        words=f.read().rstrip().split(' ')
        f.close()
    except:
        print('input file not found')
    wordlist={}
    for index in words:
        wordlist[index]=''
    return(wordlist)



