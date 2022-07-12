def remainder(a) :
    return(a % 2)

n, m = map(int, input().split())
chess_map = []
output = []
counter = 0
for i in range(n) :
    chess_map.append(list(input()))

for i in range(n - 7) :
    for j in range(m - 7) :
        counter = 0
        for k in range(8) :
            for l in range(8) :
                if chess_map[i][j] == 'W' :
                    if remainder(k) == 1 and remainder(l) == 1 :
                        if chess_map[i + k][j + l] != 'W' :
                            counter = counter + 1
                    if remainder(k) == 1 and remainder(l) == 0 :
                        if chess_map[i + k][j + l] != 'B' :
                            counter = counter + 1                    
                    if remainder(k) == 0 and remainder(l) == 1 :
                        if chess_map[i + k][j + l] != 'B' :
                            counter = counter + 1                    
                    if remainder(k) == 0 and remainder(l) == 0 :
                        if chess_map[i + k][j + l] != 'W' :
                            counter = counter + 1

                if chess_map[i][j] == 'B' :
                    if remainder(k) == 1 and remainder(l) == 1 :
                        if chess_map[i + k][j + l] != 'B' :
                            counter = counter + 1
                    if remainder(k) == 1 and remainder(l) == 0 :
                        if chess_map[i + k][j + l] != 'W' :
                            counter = counter + 1                    
                    if remainder(k) == 0 and remainder(l) == 1 :
                        if chess_map[i + k][j + l] != 'W' :
                            counter = counter + 1                    
                    if remainder(k) == 0 and remainder(l) == 0 :
                        if chess_map[i + k][j + l] != 'B' :
                            counter = counter + 1
        if counter > 32 :
            counter = 64 - counter
        output.append(counter)

print(min(output))