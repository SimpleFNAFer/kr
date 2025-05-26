print('enter words, "Стоп" breaks the loop')
w_list = []
w = input()

while w != 'Стоп':
    w_list.append(w)
    w = input()

w_sorted = sorted(w_list, key=str.lower, reverse=True)
print(f"sorted list:\n{w_sorted}")
