import random

A = set(())
B = set(())

# for i in range(10):
#     A.add(random.randint(1,20))
#     if i < 5:
#         B.add(random.randint(1,20))

while len(A) != 10:
    A.add(random.randint(1, 20))
while len(B) != 5:
    B.add(random.randint(1, 20))

print('A:', A)
print('B:', B)

print(f"A U B: {A.union(B)}")
print(f"A П B: {A.intersection(B)}")
print(f"A - B: {A.difference(B)}\nB - A: {B.difference(A)}")
print(f"A ^ B: {A.symmetric_difference(B)}")
print(f"A <= B: {A.issubset(B)}\nB <= A: {B.issubset(A)}")
