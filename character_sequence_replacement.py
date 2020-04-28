
def solution(S):
    s = S
    while True:
        match_flag = False
        r = ''
        i = 1
        while i <= len(s):
            if i == len(s):
                r += s[i-1]
                break
            comb = s[i-1]+s[i]
            if comb not in ['AB', 'BA', 'CD', 'DC']:
                r += s[i-1]
            else:
                i += 1
                match_flag = True
            i += 1

        if match_flag:
            s = r
            continue

        return s


print(solution('CBACD'))

