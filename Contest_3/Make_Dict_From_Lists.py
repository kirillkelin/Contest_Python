str1, str2 = input(), input()
result_dict = {}
for i in range(min(len(str1), len(str2))):
    result_dict[str1[i]] = str2[i]

if len(str1) > len(str2):
    for i in range(len(str1) - len(str2)):
        result_dict[str1[i + len(str2)]] = None

print(sorted(result_dict.items()))
