main_str = input()
list_str = []
for i in main_str:
    list_str.append(i)

result_dict = {}
unique_keys = set()

for i in range(len(list_str)):
    value = 1
    for j in range(i, len(list_str) - 1):
        if list_str[j] == list_str[j + 1]:
            value += 1
        else:
            break
    if list_str[i] not in unique_keys:
        unique_keys.add(list_str[i])
        result_dict[list_str[i]] = value
    else:
        if value > result_dict[list_str[i]]:
            result_dict[list_str[i]] = value

sorted_result_dict = sorted(result_dict.items(), key=lambda x: x[0])
for items in sorted_result_dict:
    print(*items)


