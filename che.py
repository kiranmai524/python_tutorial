def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1

count = 1 # 2 already counted
p = 2     # starting from 3 (see below, p+1)

while count <= 10000:
    p = p + 1
    count = count + isprime(p)

print p