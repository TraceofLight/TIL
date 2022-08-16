import sys

stair_number = int(sys.stdin.readline())
stairs = []
for _ in range(stair_number):
    stairs.append(int(sys.stdin.readline()))

result_list = []


def stair_score(now, goal, score, counter):
    global stairs
    global result_list
    if now == goal:
        result_list.append(score)
    if counter < 3 and now < goal:
        score_1 = score + stairs[now + 1]
        now_1 = now + 1
        counter_1 = counter + 1
        stair_score(now_1, goal, score_1, counter_1)
    if now < goal:
        if now + 2 <= goal:
            score_2 = score + stairs[now + 2]
            now_2 = now + 2
            counter_2 = 0
            stair_score(now_2, goal, score_2, counter_2)    

stair_score(0, stair_number - 1, 0, 0)
print(max(result_list))




