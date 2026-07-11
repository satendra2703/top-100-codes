#Find the Nth row in Pascal’s Triangle in Python ?
"""We are given a non-negative integer and we need to print the Nth row. We are assuming a zero-based starting of the rows. For example, if the input is 3, then the output should be [1, 3, 3, 1]"""

def getRow(rowIndex):
    cur_row = []
    cur_row.append(1)

    if rowIndex == 0:
        return cur_row

    prev = getRow(rowIndex - 1)

    for i in range(1, len(prev)):
        cur_row.append(prev[i - 1] + prev[i])

    cur_row.append(1)

    return cur_row

n = int(input("Enter the row: "))
arr = getRow(n)

for i in range(len(arr)):
    if i == len(arr) - 1:
        print(arr[i])
    else:
        print(arr[i], end=" ")