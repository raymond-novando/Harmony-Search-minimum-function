import random
import numpy
import math
#method
def score(harmony):
    return sphere(harmony)
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
def cetak_hm(hm):
    print("X,Y,score")
    for harmony in hm:
        print(format(harmony["harmony"][0],".3f"),",",format(harmony["harmony"][1],".3f"),",",format(harmony["skor"],".3f"))
#parameter
random.seed(0)
numpy.random.seed(0)
hm = []
hmcr = .9
par = 0
bw = 0
max = 10
min = -10
parmin = 0.01
parmax = 0.99
bwmin = 0.0001
bwmax = 1
dimension = 2
hms = 5
iterasi = 50
for i in range(hms):
    har = numpy.random.uniform(min,max,dimension)
    skor = score(har)
    hm.append({"harmony":har,"skor":skor})
hm.sort(key=get_skor)

for i in range(iterasi):
    print("iterasi",i)
    par = parmin + ((parmax - parmin) / iterasi) * (i + 1)
    c = numpy.log(bwmin / bwmax) / iterasi
    bw = bwmax * numpy.exp(c * (i + 1))
    # print("par = ",par)
    # print("bw = ",bw)
    cetak_hm(hm)
    harmonybaru = [None] * dimension
    for j in range(dimension):
        # print("dimensi = ",j)
        randhmcr = random.random()
        # print("randhmcr = ",randhmcr)
        if hmcr >= randhmcr:
            # print("memory consideration")
            harmonybaru[j] = random.choice(hm)["harmony"][j]
            # print(harmonybaru[j])
            randpar = random.random()
            # print("randpar = ",randpar)
            if par >= randpar:
                # print("pitch adjustment")
                randbw = random.uniform(-1,1)
                # print("randbw =",randbw)
                harmonybaru[j] += random.uniform(-1,1) * bw
                # print(harmonybaru[j])
        else:
            # print("randomization")
            harmonybaru[j] = random.uniform(min,max )
            # print(harmonybaru[j])
    skorbaru = score(harmonybaru)
    # print("score baru = ",skorbaru)
    if skorbaru < hm[hms-1]["skor"]:
        # print("update")
        hm[hms-1]["harmony"] = harmonybaru
        hm[hms-1]["skor"] = skorbaru
        hm.sort(key=get_skor)
print("iterasi 50")
cetak_hm(hm)