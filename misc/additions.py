ADD_CNTR = 0


def tFunc(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 1
    global  ADD_CNTR
    ADD_CNTR += 1
    return tFunc(n-1, k) + tFunc(n-1, k-1)


tFunc(10, 5)
print(ADD_CNTR)


