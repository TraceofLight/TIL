import sys

def move(coordinate, speed, distance, counter) :
    a = []
    b = []
    while counter < distance :
        try :
            coordinate = coordinate + speed
            counter += 1
            b.append(coordinate)
            if speed < 0 :
                break
            elif distance < coordinate :
                break
            if coordinate == distance and speed == 1 :
                a.append(counter)
            move(coordinate, speed + 1, distance, counter)
            move(coordinate, speed, distance, counter)
            move(coordinate, speed - 1, distance, counter)
        except :
            continue
    return(a,b)

number = int(input())
output = []
for i in range(number) :
    a, b = sys.stdin.readline().split()
    dist = int(b) - int(a)
    output.append(move(0, 1, dist, 0))

for i in range(number) :
    print(output[i])


