n = int(input('Enter the number of elements you want to sort: '))
a = []
for i in range(0,n):
    a.append(int(input('enter the element you want: ')))
    #a.append(ab)
def insertion_sort(a):
    for j in range(0,n):
        key = a[j]
        i = j-1
        while i>=0 and a[i]>key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a
insertion_sort(a)
print(a)