""" This is an algorithm which is used to
    increase the value of a particular
    array element in tme max heap."""

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
    return a

def parent(i):
    # Finds the parent node of node i
    return i//2

def heap_increase_key(a,i,n,k):
    # Increase the key value i to the given value k
    build_max_heap(a,n)
    print('Max heap is: ',a)
    if k < 0:
        print('New key is smaller..')
    else:
        a[i] += k
        while i > 1 and a[parent(i)] < a[i]:
            a[i],a[parent(i)] = a[parent(i)],a[i]
            i = parent(i)
        return a

a = []
n = int(input('Enter the no. of elements u want in an array: '))
for i in range(1,n+1):
    a.append(int(input('Enter the element to be added in the array: ')))
i = int(input('Enter the index you wanna increase the key: '))
k = int(input('Enter the key you wanna increase the value at index ' + str(i) + ': '))
a = heap_increase_key(a,i,n,k)
if a != None:
    print('The new max heap is: ',a)
