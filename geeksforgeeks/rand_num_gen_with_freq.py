from random import randint

def find_ceil(arr, r, l, m):
    mid = 0
    while(l < m):
        mid = (l + m) / 2
        if r > arr[mid]:
            l = mid + 1
        else:
            h = mid

    return l if arr[l] >= r else -1

def rand_number_generator_with_freq(num, freq):
    l_n = len(num)
    prefix = [0 for i in xrange(l_n)]

    prefix[0] = 0
    for i in xrange(1, l_n):
        prefix[i] = prefix[i - 1] + freq[i]

    rand = (randint(1, prefix[l_n - 1])) + 1
    print rand
    index = find_ceil(prefix, rand, 0, l_n - 1)

    return arr[index]


arr = [1, 2, 3, 4]
freq = [10, 5, 20, 100]

print rand_number_generator_with_freq(arr, freq)
print rand_number_generator_with_freq(arr, freq)
print rand_number_generator_with_freq(arr, freq)
print rand_number_generator_with_freq(arr, freq)
print rand_number_generator_with_freq(arr, freq)
