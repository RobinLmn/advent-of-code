f = open("input", 'r')

def process(line):
    pair = line.split(',')
    a = [int(x) for x in pair[0].split('-')]
    b = [int(x) for x in pair[1].split('-')]
    return a, b

def contains(a, b):
    return (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])

def overlaps(a, b):
    return b[0] <=  a[1] and a[0] <= b[1]

out = 0
for pair in f:
    a, b = process(pair)
    if overlaps(a, b):
        out += 1

print(out)
f.close()