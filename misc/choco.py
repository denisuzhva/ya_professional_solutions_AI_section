import numpy as np



max_a = 0
max_b = 0
max_c = 0

maxVal = 10

for a in range(1, maxVal+1):
    for b in range(1, maxVal+1):
        for c in range(1, maxVal+1):
            for_a = b / (a+b+c)
            for_b = a / (a+b+c)
            for_c = c / (a+b+c) 

            max_for_a = max_b / (a+b+c)
            max_for_b = max_a / (a+b+c)
            max_for_c = max_c / (a+b+c) 

            if max_for_a < for_a:
                max_a = a
            if max_for_b < for_b:
                max_b = b
            if max_for_c < for_c:
                max_c = c


print(a)
print(b)
print(c)