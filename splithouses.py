a= int(input())
b= input()
h = []
v = 0
c = ['']*a
for k,t in enumerate(b):
    if t == 'H':
        c[k] = 'H'
        v += 1 
        if k== a-1:
            h.append(v)
    else:
        c[k] = 'B'
        if v> 0:
            h.append(v)
            v= 0
            
if len(h) == 0 or max(h) == 1:
    print('YES')
    print(''.join(c))
else:
    print('NO')
