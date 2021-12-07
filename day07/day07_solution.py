import numpy as np

with open('input', 'r') as f:
    lines = f.readlines()
    positions = lines[0].split(',')
    positions = np.array( [int(p) for p in positions] )
#

# part 1.

# speculate: the median of positions gives the optimal 
# fuel position.
# probably true because fuel cost is based on one-norm.
# Presumably a "tie" situation means that n and n+1 have 
# the same fuel cost.

optimal_location = np.median(positions)
fuel_cost = sum( np.abs(positions - optimal_location) )

print("Optimal position: %i"%optimal_location)
print("Total fuel cost: %i"%fuel_cost)
