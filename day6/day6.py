f = open("input")

buffer = f.readline()

marker_num = 14

stack = []
for index, c in enumerate(buffer):

    if len(stack) < marker_num:
        stack.append(c)
    else:
        if len(set(stack)) == marker_num:
            print(index)
            exit()
        else:
            stack.pop(0)
            stack.append(c)
            

f.close()