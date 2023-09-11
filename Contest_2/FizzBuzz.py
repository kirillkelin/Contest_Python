N = int(input())
list = []
for i in range(1, N + 1):
    if i % 15 == 0:
        list.append('Fizz Buzz')
        continue
    elif i % 3 == 0:
        list.append('Fizz')
    elif i % 5 == 0:
        list.append('Buzz')
    else:
        list.append(i)
print(*list, sep=', ')
