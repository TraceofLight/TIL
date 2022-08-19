import sys

meeting_number = int(sys.stdin.readline())
meeting_list = []

for _ in range(meeting_number):
    meeting_list.append(list(map(int, sys.stdin.readline().split())))

sorted_meeting = sorted(meeting_list, key=lambda x:(-x[1], -x[0]))


reservation = 0
start_meeting = -1

while sorted_meeting:
    meeting_time = sorted_meeting.pop()
    if start_meeting == -1:
        reservation += 1
        start_meeting = meeting_time[1]
    else:
        if start_meeting <= meeting_time[0]:
            reservation += 1
            start_meeting = meeting_time[1]

print(reservation)
