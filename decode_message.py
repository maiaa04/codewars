import math
def decode(s):
    print(
    encode("a"*26*2))
    print(
    encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(encode("!@#$%^&*()_+-;:"))
    a,b,c,x = "", "", "", ""
    for w in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789., ":
        a += encode(  "" + w)[0]
        b += encode( "_" + w)
        c += ' ' + encode("__" + w)
    for z in "zyxwvutsrqponmlkjihgfedcba":
        x += encode(z)[0]
    print('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789., ')
    print(a*2)
    print(b*2)
    print(c)
    print()
    print(x)
    print(encode('H'*40))
    print(encode('The quick brown fox jumped over the lazy developer.'))
    
    key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789., '*3
    string = 'yFNYhdmEdViBbxc40,ROYNxwfwvjg5CHUYUhiIkp2CMIvZ.1qPz'
    output = []
    for x in range(len(string)):
        index = a.find(string[x])
        print(index)
        print((1/2**x)*(index+len(key)*2**x))
        if x != 0:
            letter = key[math.round(index - ((x+1)/2**x*index))]
        else:
            letter = key[index]
        print(letter)
        output.append(letter)
    print(output)
    #