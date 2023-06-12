
# l = [1, 2, 3, 9]
# r = 8
#
# low = 0
# high = len(l) - 1
#
# while low < high:
#     s = l[low] + l[high]
#     if s == r:
#         print(l[low], ' ', l[high])
#         break
#     elif s < r:
#         low = low + 1
#     else:
#         high = high - 1
# else:
#     print("No")


# Unsorted
l = [1, 4, 2, 4, 9, 8]
r = 8

i = 0
c = set()
while i < len(l):
    v = r - l[i]
    if l[i] in c:
        print('Yes')
        break
    else:
        c.add(v)
    i = i + 1
else:
    print("No")



