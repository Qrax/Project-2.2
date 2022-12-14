import math
import matplotlib.pyplot as plt


d = 3*10**-3 #Meter
n = 1.1 #Brekingsindex
lapda = 632.8*10**-9 #golflengte

meet_N = [1, 3, 5.5, 6, 10, 11, 13, 18, 5, 6, 7, 14, 39, 43, 32, 30, 29, 24, 24]
meet_i = [1, 2, 3, 4, 5.5, 6, 7, 9, 4, 3, 5, 8, 14, 15, 13, 12, 11.5, 11, 10]
print(len(meet_N))
checking = set(meet_i)
Ntest = 0
i_hoek = []
N = []
test1 = []
test2 = []
klaar = 0
kleine_kwadraten = []

plt.figure(figsize=(10, 5), dpi=400)

for p in range(0, 100, 1):
    n = n + 0.001
    #print("N =" + str(n))
    N = []
    i_hoek = []
    test1 = []
    for i in range(0, 31, 1):
        i = i / 2
        #print(i)
        ideg = math.radians(i)
        r_hoek = (math.asin(math.sin(ideg)/n)*(180/math.pi))
        isin = math.sin(math.radians(i))
        rsin = math.sin(math.radians(r_hoek))
        icos = math.cos(math.radians(i))
        rcos = math.cos(math.radians(r_hoek))
        itan = math.tan(math.radians(i))
        rtan = math.tan(math.radians(r_hoek))
        Ntest = ((2*d)/lapda)*((n/rcos)+(itan*isin)-(rtan*isin)-(n-1)-(1/icos))
        N.append(((2*d)/lapda)*((n/rcos)+(itan*isin)-(rtan*isin)-(n-1)-(1/icos)))
        i_hoek.append(i)
        #print(i)
        #plt.plot(i_hoek, N, zorder=1)
        #plt.plot(i_hoek, N)
        if (i in meet_i):
            index = meet_i.index(i)
            test1.append(abs(meet_N[index] - Ntest))
            test2.append(i)
            klaar += 1
            if (klaar == len(meet_i)-2):
                kleine_kwadraten.append(sum(test1))
                if (kleine_kwadraten[p] < kleine_kwadraten[p-1]):
                    beste_n = n
                    beste_N = N
                    beste_i = i_hoek
                    skreep = kleine_kwadraten[p]
                #print(kleine_kwadraten)
                klaar = 0
    #print("Totaal = " + str(p+1))


print("Brekingsindex = " + str(beste_n))
print(kleine_kwadraten)

plt.plot(beste_i, beste_N, zorder=1, label="Brekingsindex = " +str(beste_n))
plt.legend()
plt.scatter(meet_i, meet_N, zorder=2)
plt.show()