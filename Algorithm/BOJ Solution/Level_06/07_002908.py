number = input().split()
number_ = [list(i) for i in number]
for i in range(2) :
    process = number_[i].reverse()
number__ = [''.join(i) for i in number_ ]
if int(number__[0]) > int(number__[1]) :
    print(number__[0])
else :
    print(number__[1])