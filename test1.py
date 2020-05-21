a= list(input())

b=list("*******")

del a[:7]
b.extend(a)

print("".join(b))

 