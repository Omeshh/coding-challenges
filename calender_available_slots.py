
def calc(c1, c2, t1, t2, d):
    c1 = c1 or [[t1[0], t1[0]]]
    c2 = c2 or [[t2[0], t2[0]]]
    c1 = [[t1[0], t1[0]]] if c1[0][0] != t1[0] else [] + c1 + [[t1[1], t1[1]]] if c1[-1][1] != t1[1] else []
    c2 = [[t2[0], t2[0]]] if c2[0][0] != t2[0] else [] + c2 + [[t2[1], t2[1]]] if c2[-1][1] != t2[1] else []

    # print(c1)
    # print(c2)

    free_slots = []
    i = j = 0
    while i < len(c1) - 1:
        if c1[i+1][0] != c1[i][1]:
            s1 = c1[i][1]
            e1 = c1[i+1][0]

        while j < len(c2) - 1:
            if c2[j+1][0] != c2[j][1]:
                s2 = c2[j][1]
                e2 = c2[j+1][0]

                gs = max(s1, s2)
                ge = min(e1, e2)

                if (ge - gs) >= d:
                    free_slots.append([gs, ge])

                if e2 > e1:
                    j = j - 1
                    break
            j = j + 1
        i = i + 1

    return free_slots


c1 = [[900, 1030], [1200, 1300], [1600, 1800]]
c2 = [[1000, 1130], [1230, 1430], [1430, 1500], [1600, 1700]]
t1 = [900, 2000]
t2 = [1000, 1830]
d = 30

print(calc(c1, c2, t1, t2, d))