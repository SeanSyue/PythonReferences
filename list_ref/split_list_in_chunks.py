def split_list(a_list, wanted_parts=1):
    length = len(a_list)
    return [a_list[i*length // wanted_parts: (i+1)*length // wanted_parts]
            for i in range(wanted_parts)]


A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(split_list(A, wanted_parts=1))
print(split_list(A, wanted_parts=2))
print(split_list(A, wanted_parts=8))
