def lin_srch(a,v):
    while i>=0 and i<=n:
        if a[i] == v:
            return v
        else:
            return None

v = int(input('Enter the key u wanna search? '))
r = lin_srch(a,v)
if r == v:
    print('Key value exists')
else:
    print('Key value does not exists')
n = int(input('Enter the number of elements you want to sort: '))
a = []
for i in range(0,n):
    a.append(int(input('enter the element you want: ')))