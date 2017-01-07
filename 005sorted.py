#-*- coding: utf-8 -*-  
#coding=utf-8

# sort
print sorted([36, 5, 12, 9, 21])




# coustom sort
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print sorted([36, 5, 12, 9, 21], reversed_cmp)



# coustom asc ii sort 
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)