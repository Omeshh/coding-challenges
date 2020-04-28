
# https://www.geeksforgeeks.org/longest-increasing-subarray/

def solution(arr):
    i = m = l = 1

    while i < len(arr):
        if arr[i] > arr[i-1]:
            l = l + 1
        else:
            if m < l:
                m = l
            l = 1
        i = i + 1

    if m < l:
        m = 1
    return m


print(solution([5, 6, 3, 5, 7, 8, 9, 1, 2]))


