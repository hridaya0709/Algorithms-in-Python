""" This is an algorithm to
    extract the largest value from the
    max heap i.e root node."""

def max_heapify(a,i,n):
    lar = i
    l = (2*i)+1
    r = (2*i)+2
    if l < n and a[l] > a[lar]:
        lar = l
    if r < n and a[r] > a[lar]:
        lar = r
    if lar != i:
        a[i],a[lar] = a[lar],a[i]
        max_heapify(a,lar,n)

def build_max_heap(a,n):
    for i in range(n//2-1,-1,-1):
        max_heapify(a,i,n)
    return a

def heap_extract_max(a,n):
    build_max_heap(a,n)
    if n < 0:
        print('Heap underflow..')
    max = a[0]
    a[0] = a[n-1]
    n -= 1
    max_heapify(a,0,n)
    return max

a = []
n = int(input('Enter the no. of elements u want in an array: '))
for i in range(1,n+1):
    a.append(int(input('Enter the element to be added in the array: ')))
a = heap_extract_max(a,n)
print('The largest element extracted is: ',a)
