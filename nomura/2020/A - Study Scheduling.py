h1, m1, h2, m2, k = map(int, input().split())

active_time = (h2-h1)*60 + (m2-m1)

run_time = active_time-k

print(run_time)
