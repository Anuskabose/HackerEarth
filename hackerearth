a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    d = int(input())

    amt = 0
    e = min(b,c)
    u = max(b,c)
    h = 0
    k = 0
    for i in range(d):
        p1,p2 = map(int, input().split())
        h+= p1
        k += p2

    if h >= k:
        amt += h*e
        amt += k*u
    else:
        amt += k*e
        amt += h*u
    print(amt)
