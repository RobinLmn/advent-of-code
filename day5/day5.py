import re

f = open("input")

i = 0
lines = f.readlines()
rows = []

# get stack rows

while lines[i] != "\n":
    rows.append([lines[i][j:j+4] for j in range(0, len(lines[i]), 4)])
    i += 1

for row in rows:
    for j in range(len(row)):
        row[j] = row[j].replace("[", "")
        row[j] = row[j].replace("]", "")
        row[j] = row[j].replace("\n", "")
        row[j] = row[j].replace(" ", "")

stack_number = int(rows[-1][-1])
rows = rows[:-1]

# from stack rows, build the stacks

stacks = []
for i in range(stack_number):
    stack = []
    for row in rows:
        if row[i] != "":
            stack.append(row[i])
    stacks.append(stack)

# collect the move operations

i += 2  
moves = []
while i < len(lines):
    ops = [int(x) for x in re.findall(r'\d+', lines[i])] 
    moves.append(ops)
    i += 1 

# apply the move operations

for ops in moves:
    moving_crates = []
    for j in range(ops[0]):
        new = stacks[ops[1] - 1].pop(0)
        moving_crates.insert(0, new)
    for crate in moving_crates:
        stacks[ops[2] - 1].insert(0, crate)

# print the solution

for stack in stacks:
    print(stack[0], end="")

f.close()