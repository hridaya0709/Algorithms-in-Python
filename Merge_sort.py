def merge(a,p,q,r):
    l = a[p:q+1]
    r = a[q+1:r+1]
    i,j = 0,0
    si = p
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            a[si] = l[i]
            i += 1
        else:
            a[si] = r[j]
            j += 1
        si += 1
    while i < len(l):
        a[si] = l[i]
        i += 1
        si += 1
    while j < len(r):
        a[si] = r[j]
        j += 1
        si += 1
def merge_sort(a,p,r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)

r = int(input('Enter the last index: '))
a = []
for i in range(0,r+1):
    a.append(int(input('enter the element you want: ')))
merge_sort(a,0,r)
print('The sorted array is: '+ str(a))