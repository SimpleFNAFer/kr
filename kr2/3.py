def list_compare(a, b: list):
    common = []
    a_only = []
    b_only = []

    elems_stats = {}

    for elem in a:
        elems_stats[elem] = 'a'

    for elem in b:
        if elem in elems_stats:
            common.append(elem)
            elems_stats.pop(elem)
        else:
            b_only.append(elem)

    for elem in elems_stats:
        a_only.append(elem)

    return common, a_only, b_only


print('enter text a:')
a = input().split()
print('enter text b:')
b = input().split()
res = list_compare(a, b)
print(f'list compare:\n\tcommon: {res[0]}\n\ta_only: {res[1]}\n\tb_only: {res[2]}')
