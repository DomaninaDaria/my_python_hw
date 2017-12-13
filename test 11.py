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

for i in range(N):
    for j in range(M):
        if j % 2 == 0:
            for k in range(N-1):
                while massif[k][j] > massif[k+1][j]:
                    temp = massif[k][j]
                    massif[k][j] = massif[k+1][j]
                    massif[k+1][j] = temp
        else:
            for k in range(N-1):
                while massif[k][j] < massif[k+1][j]:
                    temp = massif[k][j]
                    massif[k][j] = massif[k+1][j]
                    massif[k+1][j] = temp
print()
for i in range(N):
    for j in range(M):
        print("\t",massif[i][j], end="")
    print()




