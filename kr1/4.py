import random

l = []
l_odd = []
d = {}

for i in range(20):
    n = random.randint(0, 20)

    l.append(n)
    if i % 2 == 1 and n not in l_odd and n > 10:
        l_odd.append(n)
    if n in d:
        continue

    d[n] = True

print(f"list: {l}\nunique numbers: {len(d)}\nelements by odd indexes greater than 10: {l_odd}")
