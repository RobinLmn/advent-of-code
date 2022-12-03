f = open("input", 'r')

def part_one():

    def check_rustack(ruckstack):
        half = int(len(ruckstack) * 0.5)
        for c1 in ruckstack[:half]:
            for c2 in ruckstack[half:]:
                if c1 == c2:
                    if c1.islower():
                        return ord(c1) - ord('a') + 1
                    else:
                        return ord(c1) - ord('A') + 27

    score = 0
    for ruckstack in f:
        score += check_rustack(ruckstack)
    return score

def part_two():
    
    def check_rustack(r1, r2, r3):
        for c1 in r1:
            for c2 in r2:
                for c3 in r3:
                    if c1 == c2 and c2 == c3:
                        if c1.islower():
                            return ord(c1) - ord('a') + 1
                        else:
                            return ord(c1) - ord('A') + 27

    i = 0
    score = 0
    lines = f.readlines()
    while i < len(lines):
        score += check_rustack(lines[i], lines[i+1], lines[i+2])
        i += 3
    return score

score = part_two()
print(score)
f.close()