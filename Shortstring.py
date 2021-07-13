import re
d = []
asci = []
A = 'abcde'
data = list(A)
print(data)
data = [ord(i) if i.isupper() else ord(i.upper())*-1 for i in data]
print(data)
res = -1
for i in range(len(A)):
    for j in range(i+1,len(A)+1):
        #d = asci.append(A[i:j])
        l = len(data[i:j])
        val = sum(list(set(data[i:j])))
        if val == 0:
            if res == -1 or res > l :
                res = l
print(res)




