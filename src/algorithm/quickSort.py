def kpgc(arr, i, j):
    base = arr[i]
    while i < j:
        while i < j and arr[j] >= base:
            j -= 1
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = base
    return i


def kp(arr, i, j):
    if i < j:
        base = kpgc(arr, i, j)
        kp(arr, i, base)
        kp(arr, base + 1, j)


arr = [1, 3, 44, 5, 6, 1, 231, 23, 123, 1, 23, 1, 52]
kp(arr, 0, arr.__len__()-1)

print arr
