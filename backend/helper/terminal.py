import googlesearch
import google

f = open('backend/helper/knowledge.txt', 'a')

#f.write(input('Enter Knowledge:'))
towrite = input('Enter Knowledge:')
f.write('\n' + towrite)
