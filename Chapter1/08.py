def cipher(string):
    out_string = ""
    for c in string:
        if c.isalpha():
            out_string += chr(219-ord(c))
        else:
            out_string += c
    return out_string
print(cipher("hello world"))
print(cipher(cipher("hello world")))
