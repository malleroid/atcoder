import collections

s = input()

c = collections.Counter(s)
n = ord('a')
ans = pow(10, 9)
for i in range(26):

    t = chr(n+i)

    if c[t] == 0:
        continue

    else:
        index_list = []

        for j in range(len(s)):
            if s[j] == t:
                index_list.append(j)

        if len(index_list) <= 1:
            num = (len(s)+1)//2 if len(s) > 1 else 0

        else:
            diff_list = [index_list[0]]

            for k in range(len(index_list)-1):
                diff_list.append(index_list[k+1]-index_list[k]-1)

            diff_list.append(len(s)-index_list[-1]-1)

            num = max(diff_list)

        ans = min(ans, num)

print(ans)
