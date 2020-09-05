def merge(a,p,q,r):
    l = a[p:q+1]
    r = a[q+1:r+1]
    i,j = 0,0
    si = p #si is starting index
    while i < len(l) and j < len(r): # Sorting the list by comparing elements in two sub lists a[p:q] & a[q+1:r]
        if l[i] <= r[j]:
            a[si] = l[i]
            i += 1
        else:
            a[si] = r[j]
            j += 1
        si += 1
    while i < len(l): # Checking whether any elements are left in the left list to be sorted
        a[si] = l[i]
        i += 1
        si += 1
    while j < len(r): # Checking whether any elements are left in right list to be sorted
        a[si] = r[j]
        j += 1
        si += 1
def merge_sort(a,p,r):
    if p < r:
        q = int((p+r)/2) #finding the mid point in the list
        merge_sort(a,p,q)
        merge_sort(a,q+1,r)
        merge(a,p,q,r)

r = int(input('Enter the last index: '))
a = []
for i in range(0,r+1):
    a.append(int(input('enter the element you want: ')))
merge_sort(a,0,r)
print('The sorted array is: '+ str(a))
