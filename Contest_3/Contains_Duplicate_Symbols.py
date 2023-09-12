from collections import Counter

d = Counter(input()).most_common(1)
print(True if d[0][1] != 1 else False)
