row_num = int(input('输入行数：'))
for row in range(1, row_num + 1):
    print(' ' * (row_num + 1 - row), ' *' * row)
