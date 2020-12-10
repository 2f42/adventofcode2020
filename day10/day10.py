def read_input(fname="input.txt"):
    out = []
    with open(fname) as f:
        for line in f.readlines():
            out.append(int(line.strip()))
    return out

def find_jolt_chain(adapters):
    start = 0
    target = max(adapters)
    diffs = [0,0,1]
    while start != target:
        for i in range(3):
            if i+1+start in adapters:
                diffs[i] += 1
                start += i+1
                break
    return diffs

def find_all_chains(adapters):
    adapters.sort()
    chains = {0: 1}
    for adapter in adapters:
        chains[adapter] = 0
        for i in range(3):
            if adapter-i-1 not in chains: ## this adapter doesnt exist
                chains[adapter-i-1] = 0   ## so you cant get to it
            chains[adapter] += chains[adapter-i-1]
            ## number of chains to this adapter is the sum of the
            ## number of chains to each adapter able to connect to it
    return chains[max(adapters)]

inp = read_input()
diffs = find_jolt_chain(inp)
print(diffs[0] * diffs[2])
chains = find_all_chains(inp)
print(chains)
