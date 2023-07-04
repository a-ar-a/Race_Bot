a = list(str(i) for i in range(10))
map(lambda i: int(i), a)
print(list(map(lambda i: int(i), a)))


