#Python Program to Merge Intervals ?
"""In this problem we have to merge all possible overlapping intervals and print them.

Input : [ [1, 3], [2, 6], [8, 10], [15, 18], [18, 20] ]
Output : [ [1, 6], [8, 10], [15, 20] ]
Explanation : In this [1,3] and [2,6] are overlapping so we’ll merge then and replace with [1,6]. [8,10] will remain same as it is not overlapping with any interval. Again as we can see [15,18] is overlapping with [18,20] there for it will be replaced by [15,20]. """

def merge(arr, l):
    arr.sort()
    i = 0
    while i < l - 1:
        if arr[i][0] == arr[i + 1][0] and arr[i][1] == arr[i + 1][1]:
            i += 1
            continue
        a = []
        for n in range(arr[i][0], 1 + arr[i][1]):
            a.append(n)
        for n in range(arr[i + 1][0], 1 + arr[i + 1][1]):
            if n in a:
                new_pair = [min(arr[i][0], arr[i + 1][0]), max(arr[i][1], arr[i + 1][1])]
                arr[i] = new_pair
                arr[i + 1] = new_pair
                i = 0
                break
        i += 1
    ans = []
    for i in arr:
        if i not in ans:
            ans.append(i)
    return ans


arr = [[1, 3], [2, 6], [8, 10], [15, 18], [18, 20]]
l = len(arr)
print(merge(arr, l))