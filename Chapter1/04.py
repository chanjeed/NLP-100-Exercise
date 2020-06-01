sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.replace('.','')
words = words.replace(',','')
words = words.split(' ')
dic={}
for index,word in enumerate(words):
    if index==1 or \
            index==5 or \
            index==6 or \
            index==7 or \
            index==8 or \
            index==9 or \
            index==15 or \
            index==16 or \
            index==19 :
                dic[word[0:1]]=index
    else:
        dic[word[0:2]]=index

print(dic)
