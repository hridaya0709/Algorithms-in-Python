"""This program calculates whether a given number is the sum of any two elements in the list."""
def sum_search(a,x):
    set_of_pairs = []
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if (a[i] + a[j]) == x:
                l = [a[i],a[j]]
                if l not in set_of_pairs:
                    set_of_pairs.append(l)
            else:
                j += 1
        i += 1
    return set_of_pairs

a = []
n = int(input('Enter the size of the list '))
for i in range(0,n):
    a.append(int(input('Enter the element you wanna add into the list: ')))
print('The list you created is: ',a)
x = int(input('Enter the number you wanna check whether that number is equal to the sum of any two elements in the list '))
res = sum_search(a,x)
print('The pair/pairs of two elements in the list which is equal to the given number: ' + str(x) + ' is ' + str(res))
