number = int(input())
a = input().split()
a_ = [int(i) for i in a]
b = a_.sort()
output = a_[number//2]
print(output)