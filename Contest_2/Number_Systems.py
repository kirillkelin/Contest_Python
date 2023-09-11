value, M = list(map(int, input().split()))
arr = []
while value >= M:
    arr.append(value % M)
    value = value // M
    if M > value:
        arr.append(value)
arr.reverse()
print(*arr, sep='')
