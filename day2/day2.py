f = open("input", "r")

def part_one():
    def get_score(a, x):
        if ord(a) + 23 == ord(x):
            return 3
        if x == "X" and a == "C":
            return 6
        if x == "Y" and a == "A":
            return 6
        if x == "Z" and a == "B":
            return 6
        return 0

    score = 0
    for match in f:
        score += get_score(match[0], match[2])
        score += ord(match[2]) - 23 - 64

    return score

def part_two():
    def get_score(a, x):
        if x == "Z":
            if a == "A":
                return 2
            if a == "B":
                return 3
            if a == "C":
                return 1
        if x == "Y":
            return ord(a) - 64
        if x == "X":
            if a == "A":
                return 3
            if a == "B":
                return 1
            if a == "C":
                return 2
        return 0

    score = 0
    for match in f:
        score += get_score(match[0], match[2])
        score += (ord(match[2]) - 23 - 65) * 3

    return score


out = part_two()
print(out)
    
f.close()
