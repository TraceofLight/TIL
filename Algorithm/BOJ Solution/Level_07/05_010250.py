testdata = int(input())
output = []
for i in range(testdata) :
    hotel_info = input().split()
    height = int(hotel_info[0])
    width = int(hotel_info[1])
    guest = int(hotel_info[2])
    hotel_room = []
    for j in range(width) :
        for k in range(height) :
            room_number = (k + 1) * 100 + (j + 1)
            hotel_room.append(room_number)
    output.append(hotel_room[guest - 1])
for l in range(len(output)) :
    print(output[l])