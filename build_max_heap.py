""" This is an algorithm to build a max heap out of given input array.
    This builds the heap in such a way that the root node of the heap
    is the largest element from the given array."""

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

a = []
n = int(input('Enter the no. of elements u want in an array: '))
for i in range(1,n+1):
    a.append(int(input('Enter the element to be added in the array: ')))
a = build_max_heap(a,n)
print('The max heap for given array is: ',a)