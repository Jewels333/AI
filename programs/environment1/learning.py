
supportWord = 'i', 'am', 'you'
context = ''
def define(word, base):
    definition = ''
    context = ''
    f = open('programs/environment1/databases/' + base + '.txt')
    database = f.read()
    word = extract(word)
    


    

def extract(str):
    extracted = ''
    context = ''
    wordList = str.split()
    wordDigit = int(len(wordList))
    x = 1
    for x in range(0, wordDigit):
        word = wordList.slice(x)
        if word != supportWord:
            extracted = extracted + word
        else:
            word.slice()
        x = x + 1
    print(extracted)

        
