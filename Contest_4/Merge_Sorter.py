import heapq


def merge_sorter(*args):
    iterators = [iter(arg) for arg in args]
    merged_iterator = heapq.merge(*iterators)

    for value in merged_iterator:
        yield value


list_1 = [1, 4, 6, 9, 10, 14]
list_2 = [4, 8, 12, 15, 17, 18]
list_3 = [2, 101, 1101]

gen = merge_sorter(list_1, list_2, list_3)
for i in range(15):
    print(next(gen))
