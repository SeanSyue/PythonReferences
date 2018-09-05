import itertools

for comb_re in itertools.combinations_with_replacement(range(9, -1, -1), 3):
    print(comb_re)

for prod in itertools.product('ABCD', repeat=2):  # AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
    print(prod)

for perm in itertools.permutations('ABCD', 2):  # AB AC AD BA BC BD CA CB CD DA DB DC
    print(perm)

for comb in itertools.combinations('ABCD', 2):  # AB AC AD BC BD CD
    print(comb)

for comb_re2 in itertools.combinations_with_replacement('ABCD', 2):  # AA AB AC AD BB BC BD CC CD DD
    print(comb_re2)
