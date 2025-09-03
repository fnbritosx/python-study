import random

num = ()

for c in range (0,5):
    n = random.randint(0,10)
    num += (n,)

ordem = sorted(num)

print (num)
print(ordem)
print(ordem[0])
print(ordem[-1])