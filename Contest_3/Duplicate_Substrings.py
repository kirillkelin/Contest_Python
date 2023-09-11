main_str, N = input(), int(input())

unique_str = set()
result = []
for i in range(len(main_str) - N + 1):
    cur_str = main_str[i:(N + i)]
    if cur_str not in unique_str:
        unique_str.add(cur_str)
    else:
        result.append(cur_str)

print(sorted(list(set(result))))
