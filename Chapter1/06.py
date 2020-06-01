sentence_1 = "paraparaparadise"
sentence_2 = "paragraph"

def n_gram(string,n=2):
    
    return [string[idx:idx+n] for idx in range(len(string) - n +1)]

X=set(n_gram(sentence_1,2))
Y=set(n_gram(sentence_2,2))
print(X)
print(Y)

X_union_Y = X|Y
print(X_union_Y)

X_inter_Y = X & Y
print(X_inter_Y)

X_dif_Y = X - Y
print(X_dif_Y)
Y_dif_X = Y - X
print(Y_dif_X)

print("se" in X)
print("se" in Y)
