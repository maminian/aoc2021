import numpy as np
import itertools

with open('input', 'r') as f:
    lines = f.readlines()
    lines = [list( l.split()[0] ) for l in lines]
    octo = np.array(lines, dtype=int)

#

def finished(a,f):
    '''
    Returns True only if the two arrays match in all entries.
        a : 'active' mask; an octopus is ready to fire or has fired.
        f : 'fired' mask; has fired on this step.
    '''
    return np.all( a==f )
#

nbr_cache = {}

def neighbors(ij, dims=octo.shape):
    '''
    Gets neighbors (including diagonals) of octopus (i,j). 
    Variable ij should be a tuple with two entries.
    '''
    # note: hacky; also excites original octopus more.
    ij = tuple(ij)
    if ij in nbr_cache.keys():
        nbrs = nbr_cache[ij]
    else:
        i,j = ij
        lx = max(0,i-1)
        rx = min(i+2, dims[0])
        ly = max(0,j-1)
        ry = min(j+2, dims[1])
        nbrs = []
        for ii,jj in itertools.product(range(lx,rx), range(ly,ry)):
            if ii==i and jj==j:
                continue
            nbrs.append((ii,jj))
        nbr_cache[(i,j)] = nbrs
    return nbrs
#

######

maxsteps = 100
step=0
firings = 0

step_idxs = []
states = []

while True:
    octo += 1
    
    step_idxs.append( step )
    states.append( np.array(octo) )
    
    active = (octo > 9)
    flashed = np.zeros(active.shape, dtype=bool)  # copy

    while np.any(active):
        for coord in zip(*np.where(active)):
            flashed[coord] = True
            for nn in neighbors(coord):
                octo[nn] += 1
        active = np.logical_and( (octo > 9), np.logical_not(flashed) )
        
        step_idxs.append( int(step) )
        states.append( np.array(octo) )
    #
    
    # reset all octos that flashed.
    octo[flashed] = 0
    firings += np.sum(flashed)

    step_idxs.append( int(step) )
    states.append( np.array(octo) )

    step += 1
    if np.all(flashed):
        print("dong ding part 2 step %i"%(step))
        break
    
    
print("Part 1: %i total flashes."%firings)

