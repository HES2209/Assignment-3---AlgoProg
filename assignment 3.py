def union_list(A,B):
    return list(set(A).union(set(B)))

def modify_tuprings (tup,string):
    har = tup
    ris = string
    return ''.join([har * ris for har, ris in zip(string,tup)])

a1 = [1,3,5]
b1 = [1,2,3]
a2 = [2,4,6]
b2 = [2,4,6]
a3 = [1,2,3,4]
b3 = [4,5,6,7]

tup1, str1 = (1,2,3,4),'alex'
tup2, str2 = (1,2,1),'pan'
tup3, str3 = (5,), 'z'

union_results = [union_list(a1,b1),union_list(a2,b2), union_list(a3,b3)]
modify_results = [modify_tuprings(tup1,str1), modify_tuprings(tup2,str2), modify_tuprings(tup3,str3)]
print(union_results)
print(modify_results)