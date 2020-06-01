sentence = "I am an NLPer"

def n_gram(string,n=2):
    
    return [string[idx:idx+n] for idx in range(len(string) - n +1)]

print(n_gram(sentence,2))
print(n_gram(sentence.split(' '),2))


