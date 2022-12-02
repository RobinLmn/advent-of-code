def part_one():
    maximum = 0
    current_count = 0
    for line in f:
        if line == "\n":
            if maximum < current_count:
                maximum = current_count
            current_count = 0
        else:
            current_count += int(line)
    return maximum

def part_two():
    top = [0, 0, 0]
    
    current_count = 0
    for line in f:
        if line == "\n":
            if top[0] < current_count:
                top[0] = current_count
                top.sort()
            current_count = 0
        else:
            current_count += int(line)
            
    return sum(top)

    

f = open("input", "r")
out = part_two()
print(out)
f.close()
