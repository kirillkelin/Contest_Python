N, M = list(map(int, input().split()))
arr = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        arr[i][j] = (i + 1) * (j + 1)
        print(arr[i][j], end=' ')
    print()
