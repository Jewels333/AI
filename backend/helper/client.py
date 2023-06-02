def retrieve(word, subject):
    if subject == 'synonym':
        pass #do later
    f = open('backend/helper/knowledge.txt', 'r')
    lines = f.readlines()
    targets = {}
    for lines in Lines:
        count += 1
        if Lines.startswith(f'Synonyms for {word}:'):
            for i in lines:
                count2 += 1
                f.readline()
                if count2 == count:
                    content = f.readline()
                    break
                else:
                    continue
        else:
            continue
    cutpoint = len(f'Synonyms for {word}')
    content.split(cutpoint)
    for lines in Lines:
        
    