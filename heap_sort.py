""" This is a sorting technique based on heaps.
    This algorithm takes an input of n elements
    and build a max heap out of it and
    then sorts the array in ascending order."""

def max_heapify(a,i,n):
    # Maintains max heap condition using input array a and node i
    # n is the length of the array a
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
    # Builds a max heap out of given input array a
    for i in range(n//2-1,-1,-1):
        max_heapify(a,i,n)

def heapsort(a,n):
    # Sorts the max heap in ascending order
    build_max_heap(a,n)
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i],a[0]
        max_heapify(a,0,i)
    return a

a = []
n = int(input('Enter the no. of elements u want in an array: '))
for i in range(1,n+1):
    a.append(int(input('Enter the element to be added in the array: ')))
a = heapsort(a,n)
print('The sorted array is: ',a)
