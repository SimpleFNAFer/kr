print('enter either word or number, "Стоп" breaks the loop')
inp = input()

nums = []
words = []

while inp != "Стоп":
    if inp.isnumeric():
        nums.append(inp)
        print(f"{inp} is a number")
    elif inp.isalpha():
        words.append(inp)
        print(f"{inp} is a word")
    else:
        print(f"{inp} is neither number nor word")

    inp = input()

print(f"\nRESULT\nnums: {nums}\nwords: {words}")
