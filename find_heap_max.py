""" This is an algorithm to find the largest element in the max heap.
    It takes an input array, builds a max heap and returns
    the largest element in the heap i.e root node."""

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

def find_max_heap(a):
    # Finds the largest element in the max heap which is root node.
    return a[0]

def build_max_heap(a,n):
    # Builds a max heap out of given input array a
    for i in range(n//2-1,-1,-1):
        max_heapify(a,i,n)
    max = int(find_max_heap(a))
    return max

a = []
n = int(input('Enter the no. of elements u want in an array: '))
for i in range(1,n+1):
    a.append(int(input('Enter the element to be added in the array: ')))
a = build_max_heap(a,n)
print('The largest value in the max heap is: ',a)
