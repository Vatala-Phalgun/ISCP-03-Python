n = int(input())
a = list(map(int, input().split()))

i = 1
while i < n and a[i] > a[i-1]:
    i += 1

while i < n and a[i] == a[i-1]:
    i += 1

while i < n and a[i] < a[i-1]:
    i += 1

if i == n:
    print("yes")
else:
    print("no")