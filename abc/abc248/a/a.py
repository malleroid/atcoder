S = list(input())

set_S = set(S)
set_s = set(str(i) for i in range(10))

extra_nums = set_s - set_S

print(list(extra_nums)[0])
