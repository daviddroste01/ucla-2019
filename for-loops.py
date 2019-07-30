import random
a = []
for x in range(10):
    a.append(random.randint(1,15))

s=0
for x in a:
    print(x)
    s=s+x
print(s)