import sys

Start, End = list(map(int,sys.stdin.readline().split()))
distance = abs(End - Start)
counter = distance
def HideNSeek(depart, destination, count) :
    global counter
    if destination == depart :
        if count < counter :
            counter = count
    elif destination < depart :
        if counter > depart - destination + count :
            counter = depart - destination + count
    elif depart < destination :
        while True :
            if count > distance :
                break
            depart_1 = 2 * depart
            count_1 = count + 1
            HideNSeek(depart_1, destination, count_1)
            break
        while True :
            if count > distance :
                break
            depart_2 = depart + 1
            count_2 = count + 1
            HideNSeek(depart_2, destination, count_2)
            break
        while True :
            if count > distance :
                break
            depart_3 = depart - 1
            count_3 = count + 1
            HideNSeek(depart_3, destination, count_3)
            break

while True :
    if Start == End :
        print(0)
        break
    else :
        HideNSeek(Start, End, 0)
        print(counter)
        break