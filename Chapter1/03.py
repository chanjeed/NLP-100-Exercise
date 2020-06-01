sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sentence.replace(',','')
words = words.replace('.','')
words = words.split(" ")

l=[]
for word in words:
    l.append(len(word))
print(l)
