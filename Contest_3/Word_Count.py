import collections

basic_str = input().split()
c = collections.Counter()
for word in basic_str:
    c[word] += 1

max_value = 0
values = []
for value in c.values():
    values.append(value)

max_value = max(values)
result = (max_value / len(basic_str))
print(result)
