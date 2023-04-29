n = int(input())
a = []
p = []
for i in range(n):
    a_i, p_i = map(int, input().split())
    a.append(a_i)
    p.append(p_i)

for i in range(n-1):
    if p[i] < p[i+1]:
        p[i+1] = p[i]

min_cost = sum([a[i] * p[i] for i in range(n)])
print(min_cost)
