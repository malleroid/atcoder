A,B=input().split()

a_arr=list(map(int,A))
b_arr=list(map(int,B))

print(max(sum(a_arr),sum(b_arr)))