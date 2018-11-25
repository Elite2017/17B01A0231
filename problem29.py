list = []
for i in range(2,101):
    for j in range(2,101):
        list.append(pow(i,j))
s = set(list)
print(len(s))
