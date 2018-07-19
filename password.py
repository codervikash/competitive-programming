def cal_lps(pat):
    l = len(pat)
    lps = [0 for i in xrange(l)]
    lps_len = 0
    i = 1

    while i <  l:
        if pat[i] == pat[lps_len]:
            lps_len += 1
            lps[i] = lps_len
            i += 1
        else:
            if lps_len != 0:
                lps_len = lps[lps_len - 1]
            else:
                lps[i] = lps_len
                i += 1

    return lps

def solution(string):
    n = len(string)

    lps = cal_lps(string)
    print lps
    suffix_len = lps[n - 1]

    if suffix_len == 0 or string[:suffix_len] != string[n - suffix_len- 1:]:
        return 'Just a legend'
    else:
        return 'Just a legend' if suffix_len not in lps[suffix_len: n - 1] else  string[:suffix_len]



print solution('fixprefixsuffix')
