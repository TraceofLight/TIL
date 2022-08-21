import sys
from itertools import combinations

people_number = int(sys.stdin.readline())
bonus_list = []
for _ in range(people_number):
    bonus_list.append(list(map(int, sys.stdin.readline().split())))

vs_val = float('inf')

for team in combinations([number for number in range(1, people_number + 1)], people_number // 2):
    other_team = [member for member in range(1, people_number + 1) if member not in team]
    team_bonus = 0
    for duo in combinations(team, 2):
        team_bonus += bonus_list[duo[0] - 1][duo[1] - 1]
        team_bonus += bonus_list[duo[1] - 1][duo[0] - 1]
    other_team_bonus = 0
    for other_duo in combinations(other_team, 2):
        other_team_bonus += bonus_list[other_duo[0] - 1][other_duo[1] - 1]
        other_team_bonus += bonus_list[other_duo[1] - 1][other_duo[0] - 1]
    vs_val = min(abs(team_bonus - other_team_bonus), vs_val)
    if vs_val == 0:
        break

print(vs_val)
