word = input()
word = word.replace('dz=','#')
word = word.replace('c=','#')
word = word.replace('c-','#')
word = word.replace('d-','#')
word = word.replace('lj','#')
word = word.replace('nj','#')
word = word.replace('s=','#')
word = word.replace('z=','#')
print(len(word))

# 이하 코드는 오류 발생했지만 원인을 모름

word = input()
word_element = list(word)
length = 0
counter = 0
for i in range(len(word_element)) :
    try :
        if word_element[i] == 'c' :
            if word_element[i + 1] == '=' or word_element[i + 1] == '-':
                counter = counter + 1
        elif word_element[i] == 'd' :
            if word_element[i + 1] == 'z' and word_element[i + 2] == '=':
                counter = counter + 2
                word_element[i + 1] = 'not_z'
            if word_element[i + 1] == '-' :
                counter = counter + 1
        elif word_element[i] == 'l' :
            if word_element[i + 1] == 'j' :
                counter = counter + 1
        elif word_element[i] == 'n' :
            if word_element[i + 1] == 'j' :
                counter = counter + 1
        elif word_element[i] == 's' :
            if word_element[i + 1] == '=' :
                counter = counter + 1
        elif word_element[i] == 'z' :
            if word_element[i + 1] == '=' :
                counter = counter + 1
        elif word_element[i] == ' ' :
                counter = counter + 1
        length = length + 1
    except :
        continue
print(length - counter)



word = input()
word_element = list(word)
length = len(word_element)
counter = 0
for i in range(length) :
    try :
        if word_element[i] == 'j' :
            if (word_element[i - 1] == 'l') or (word_element[i - 1] == 'n') :
                counter = counter + 1
        elif word_element[i] == '-' :
            if (word_element[i - 1] == 'c') or (word_element[i - 1] == 'd') :
                counter = counter + 1
        elif word_element[i] == '=' :
            if (word_element[i - 1] == 'c') or (word_element[i - 1] == 's') or (word_element[i - 1] == 'z'):
                counter = counter + 1
                if word_element[i - 2] == 'd' :
                    counter = counter + 1
    except :
        print('Error')
        continue
print(length - counter)