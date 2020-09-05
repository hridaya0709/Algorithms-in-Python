def binary_search(a,f,l,v):
    if f<l:
        m = (f+l)//2
        if a[m] == v:
            print('Key found at index: ',m)
        elif a[m]>v:
            binary_search(a,0,m,v)
        else:
            binary_search(a,m+1,l,v)
    else:
        print('Key value not found!')

a = []
for i in range(0,100):
    a.append(i)
v = int(input('Enter the value you wanna search in your sorted array '))
n = len(a)
result = binary_search(a,0,n,v)
"""if result == None:
    print('Key value not found!')
else:
    print('Key value found at index: ',result)
"""


