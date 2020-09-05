def max_subarray_brute(a):
    max = a[0]
    for i in range(0,len(a)):
        sum = 0
        for j in range(i,len(a)):
            sum += a[j]
            if sum > max:
                l = i+1
                h = j+1
                max = sum
    return (l,h,max)
a = []
n = int(input('Enter the size of the list '))
for i in range(n):
    a.append(int(input('Enter the element into the list: ')))
print('The list you created is: ',a)
l,h,max = max_subarray_brute(a)
print('The maximum subarray sum is: ',max)
print('The maximum subarray starts at position ' + str(l) + ' and ends at position ' + str(h))

