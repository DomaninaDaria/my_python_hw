N = int(input("Input value of  rows:"))
M = int(input("Input value of columns: "))
matrix = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        print("Input element in position ")
        matrix[i][j] = int(input())
for i in range(N):
    for j in range(M):
        print("\t", matrix[i][j], end="")
    print("")
min_in_row = 0
min_index_i = 0
min_index_j = 0
saddle = 0
for i in range(N):
    min_in_row = matrix[i][0]
    for j in range(M-1):
        min_index_i = i
        if matrix[i][j+1] < min_in_row:
            min_in_row = matrix[i][j + 1]
            min_index_j = j+1
    is_max_in_column = True
    for k in range(N):
        if matrix[min_index_i][min_index_j] < matrix[k][min_index_j]:
            is_max_in_column = False
            break
    if(is_max_in_column):
        saddle = matrix[min_index_i][min_index_j]
        print(saddle)




