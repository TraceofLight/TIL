subject = int(input())
score = input().split()
score = list(map(float,score))
sum = 0
max_score = max(score)
for i in range(len(score)) :
    score[i] = score[i] / max_score * 100
for j in range(len(score)) :
    sum = sum + score[j]
print(sum/len(score))