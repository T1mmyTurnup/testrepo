fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    wrds = line.split()
    for w in wrds:
        counts[w] = counts.get(w,0) + 1
