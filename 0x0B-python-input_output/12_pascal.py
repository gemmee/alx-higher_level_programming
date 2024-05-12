# Print Pascal's Triangle in Python

# input n
n = 6

pascal = []
# iterate up to n
for i in range(n):
    # adjust space
    # print(' '*(n-i), end='')

    # compute each value in the row
    coef = 1
    elem = []
    for j in range(0, i + 1):
        # print(coef, end=' ')
        elem.append(coef)
        coef = coef * (i - j) // (j + 1)
    pascal.append(elem)
    # print()
print(pascal)
