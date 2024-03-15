matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
] # call this matrix `A`

# for i in range(2):
#     for j in range(3):
#         print(matrix[j][i], end=' ')
#     print()

def traverse(matrix):
    for x in matrix:
        print_val = ''
        for y in x:
            print_val += str(y) + " "
        print(print_val)


# traverse(matrix)

def super_nest(ls):
    if type(ls[0]) == list:
        return super_nest(ls[0])
    else:
        return ls

def super_nest_it(ls):
    while type(ls[0]) == list:
        ls = ls[0]
    return ls

# matrix2 = [[[[[[[[[1,2,3,4]]]]]]]]]
# print(super_nest(matrix2))
# print(super_nest_it(matrix2))

def times_table(n):
    ls = []
    for x in range(1,n+1):
        row = []
        for y in range(1,n+1):
            row.append(x*y)
        ls.append(row)
    return ls

print(times_table(3))