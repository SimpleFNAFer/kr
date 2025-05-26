print('enter number')
n = int(input())

if n % 21 == 0:
    print(f"{n} can be divided by 7 and 3")
elif n % 7 == 0:
    print(f"{n} can be divided 7")
elif n % 3 == 0:
    print(f"{n} can be divided by 3")
else:
    print(f"{n} cannot be divided neither by 7 nor by 3")
