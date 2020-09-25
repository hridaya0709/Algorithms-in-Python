""" This is an algorithm which is used to insert
    a value into the heap satisfying the max heap
    condition."""

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
    print('The old max heap with the last node having key 0 is: ',a)

def parent(i):
    # Finds the parent node of node i
    return i//2

def heap_increase_key(a,i,n,k):
    # Increases the key value i to the value k
    build_max_heap(a,n)
    if k < 0:
        print('New key is smaller..')
    else:
        i -= 1
        a[i] = k
        while i > 1 and a[parent(i)] < a[i]:
            a[i],a[parent(i)] = a[parent(i)],a[i]
            i = parent(i)
        return a


def max_heap_insert(a,n,k):
    # Inserts the key k into the heap maintaining the max heap property.
    n += 1
    a.append(0)
    heap_increase_key(a,n,n,k)
    return a


a = []
n = int(input('Enter the no. of elements u want in an array: '))
for i in range(1,n+1):
    a.append(int(input('Enter the element to be added in the array: ')))
k = int(input('Enter the value you wanna insert in the heap: '))
a = max_heap_insert(a,n,k)
print('The new max heap is: ',a)
