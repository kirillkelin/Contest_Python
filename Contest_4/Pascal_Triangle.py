def pascal_triangle():
    row = [1]
    while True:
        for value in row:
            yield value
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        row = next_row
