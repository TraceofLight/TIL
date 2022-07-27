s = input()
list_s = list(s)
alphabet_ascii = []
output = []
for i in range(97, 123) :
    alphabet_ascii.append(i)
alphabet = [chr(i) for i in alphabet_ascii]
for j in range(len(alphabet)) :
    try :
        output.append(list_s.index(alphabet[j]))
    except :
        output.append(-1)
for k in range(len(output)) :
    print(output[k], end = ' ')