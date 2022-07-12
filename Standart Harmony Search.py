import random
import numpy
import math
#method
def score(harmony):
    return ackley(harmony)
def sphere(harmony):
    return sum([x ** 2 for x in harmony])
def schwefel222(harmony):
    return sum([abs(x) for x in harmony]) + math.prod([abs(x) for x in harmony])
def rosenbrock(harmony):
    val = 0.0
    for i in range(len(harmony)-1):
        val += (100 * (harmony[i+1]-harmony[i]**2)**2 + (harmony[i]-1)**2)
    return val
def step(harmony):
    return sum([(x + 0.5) ** 2 for x in harmony])
def schwefel(harmony):
    return 418.9829*len(harmony) - sum([x * math.sin(math.sqrt(abs(x))) for x in harmony])
def rastrigin(harmony):
    return sum([x**2 - 10 * math.cos(2 * math.pi * x) + 10 for x in harmony])
def ackley(harmony):
    d = len(harmony)
    sum1 = sum([x ** 2 for x in harmony])
    sum2 = sum([math.cos(2 * math.pi *x) for x in harmony])
    term1 = -20 * math.exp(-0.2 * math.sqrt(sum1 / d))
    term2 = -math.exp(sum2 / d)
    return term1 + term2 + 20 + math.exp(1)
def get_skor(harmony):
    return harmony.get('skor')
#parameter
hm = []
hmcr = .9
par = .3
bw = .01
max = 32
min = -32
dimension = 2
hms = 5
iterasi = 50000
for i in range(hms):
    har = numpy.random.uniform(min,max,dimension)
    skor = score(har)
    hm.append({"harmony":har,"skor":skor})
hm.sort(key=get_skor)
for i in range(iterasi):
    harmonybaru = [1] * dimension
    for j in range(dimension):
        if hmcr >= random.random():
            harmonybaru[j] = random.choice(hm)["harmony"][j]
            if par >= random.random():
                harmonybaru[j] += random.uniform(-1,1) * bw
        else:
            harmonybaru[j] = random.uniform(min,max)
    skorbaru = score(harmonybaru)
    if skorbaru < hm[hms-1]["skor"]:
        hm[hms-1]["harmony"] = harmonybaru
        hm[hms-1]["skor"] = skorbaru
        hm.sort(key=get_skor)
print(hm[0]["skor"])