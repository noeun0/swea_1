a = [1,2,3,4,5,6,7,8,9,10]

b=list(map(lambda m : m*m, list(filter(lambda i : i%2==0, a))))

print(b)


# a = [1,2,3,4,5,6,7,8,9,10]

# b=list(filter(lambda i : i%2==0, a))

# result = list(map(lambda i : i*i, b))

# print(f"{result}")
