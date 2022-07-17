# need to modify according to the current code

def crossoverFunction(pop, w):
    child = []*w
    for i in range(0, w, 2):
        data = pop[i]
        data2 = pop[i+1]
        child.append(data[:16]+data2[:7])
        child.append(data2[:16]+data[:7])
    return child
