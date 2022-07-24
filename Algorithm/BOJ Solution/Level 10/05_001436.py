number = int(input())
six = []
here = 0
while True :
    here += 1
    if str(here).find('666') != -1 :
        six.append(here)
    if len(six) == number :
        break
print(six[-1])