n = int(input('Enter the number of elements you want to sort: '))
a = []
for i in range(0,n):
    a.append(int(input('enter the element you want: ')))
def selection_sort(a):
    for j in range(n-1):
        sml = j
        for i in range(j+1,n):
            if a[i] < a[sml]:
                sml = i
        if sml != j:
            a[sml],a[j] = a[j],a[sml]
    return a

selection_sort(a)
print(a)