def max_subarr_cross_mid(a,l,m,h):
    l_sum = float('-inf')
    sum,max_l,max_r = 0,0,0
    for i in range(m,l,-1):
        sum += a[i]
        if sum > l_sum:
            l_sum = sum
            max_l = i
    r_sum = float('-inf')
    sum = 0
    for j in range(m+1,h):
        sum += a[j]
        if sum > r_sum:
            r_sum = sum
            max_r = j
    return (max_l,max_r,l_sum+r_sum)

def max_subarr(a,l,h):
    if h == l:
        return (l,h,a[l])
    else:
        m = (l+h) // 2
        (l_l,l_h,l_sum) = max_subarr(a,l,m)
        (r_l,r_h,r_sum) = max_subarr(a,m+1,h)
        (c_l,c_h,c_sum) = max_subarr_cross_mid(a,l,m,h)
    if l_sum >= r_sum and l_sum >= c_sum:
        return(l_l,l_h,l_sum)
    elif r_sum >= l_sum and r_sum >= c_sum:
        return(r_l,r_h,r_sum)
    else:
        return(c_l,c_h,c_sum)

a = []
n = int(input('Enter the size of the list '))
for i in range(n):
    a.append(int(input('Enter the element into the list: ')))
print('The list you created is: ',a)
(s_i,e_i,sum) = max_subarr(a,0,n-1)
print('The maximum subarray sum is: ',sum)
print('The maximum subarray starts at position ' + str(s_i) + ' and ends at position ' + str(e_i))
