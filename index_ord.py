a = list(input())

al = [-1, -1, -1, -1,-1, -1,-1, -1,-1, -1,-1,-1,-1,-1, -1,-1, -1,-1, -1,-1, -1,-1, -1,-1, -1,-1,-1-1,-1-1,-1]

for i in a:
    al[ord(i)-97] = a.index(i)


print(al)

