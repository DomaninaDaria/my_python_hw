N = int(input("Input value of  row:"))
M = int(input("Input value of column: "))
massif = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        print("Input element in position ")
        massif[i][j] = int(input())
for i in range(N):
    for j in range(M):
        print("\t",massif[i][j], end="")
    print("")
min_in_row = 0
min_index_i = 0
min_index_j = 0
sedl = 0
for i in range(N):
    min_in_row = massif[i][0]
    for j in range(M-1):
        min_index_i = i
        if massif[i][j+1] < min_in_row:
            min_in_row = massif[i][j+1]
            min_index_j = j+1
    f = True
    for k in range(N):
        if massif[min_index_i][min_index_j] < massif[k][min_index_j]:
            f = False
            break
    if(f):
        sedl = massif[min_index_i][min_index_j]
        print(sedl)




