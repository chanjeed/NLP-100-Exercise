import random
sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
output = ""

words = sentence.split(" ")
for word in words:
    if len(word)>4:
        output += word[0] + ''.join(random.sample(word[1:-1],len(word)-2))+ word[-1]
    else:
        output += word
    output+= ' '

#Remove the space of the last word
output = output[:-1]

print(output)
