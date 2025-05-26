def count_elements(lst: list):
    result = {}

    for elem in lst:
        result[elem] = result.get(elem, 0) + 1

    return result


print('enter text:')
t = input()
l = t.split()
print(f"words frequencies: {count_elements(l)}")
