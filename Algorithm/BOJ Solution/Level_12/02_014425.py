import sys

checker, check_num = list(map(int,input().split()))
checker_list = []
counter = 0

for i in range(checker):
    checker_list.append(input())

for i in range(check_num):
    input_word = sys.stdin.readline().split('\n')[0]
    try :
        checker_list.index(input_word)
        counter += 1
    except :
        continue

print(counter)

'''
import sys

checker, check_num = list(map(int,input().split()))
checker_list = []
counter = 0

for i in range(checker):
    checker_list.append(input())

input_word = []
for i in range(check_num):
    input_word.append(sys.stdin.readline().split('\n')[0])

result = len([i for i in input_word if i in checker_list])

print(result)
'''