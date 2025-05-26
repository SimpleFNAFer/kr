print('enter sentence')

s = input()
char_set = {}

for c in s:
    if c in char_set:
        continue

    char_set[c] = True

print(f"sentence [{s}] has {len(char_set)} unique characters:\n{list(char_set.keys())}")
