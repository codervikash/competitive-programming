def check_parity(n):
    parity = 0

    while n:
        result ^= 1
        n >> 1
