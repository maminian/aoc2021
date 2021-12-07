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
# Presumably a "tie" situation (median is between two integers) 
# means that n and n+1 have the same fuel cost.

optimal_location = np.median(positions)
fuel_cost = sum( np.abs(positions - optimal_location) )

print("Optimal position: %i"%optimal_location)
print("Total fuel cost: %i"%fuel_cost)

# part 2.

# fuel cost is now scaling by distance traveled; 
# each additional displacement is increasing the effort by 
# one. So, one unit is +1, two units +2, three +3, etc.
#
# Metric is more like the sum from 0 to abs(x-xstar) of i, 
# which is N*(N+1)/2. In plain terms, this is the cost function 
# which is the average of the mean and median. But it's not clear 
# that the minimizer here is actually the average of the 
# argminimizers (the mean and median). Worth a shot, though...

def cost(x,xstar):
    if isinstance(x,int) or isinstance(x,float) or isinstance(x,np.int64):
        N = abs(x-xstar)
        return int( N*(N+1)/2 )
    else:
        return sum([cost(xi,xstar) for xi in x])
# 

mean_location = np.mean(positions)
median_location = np.median(positions)

av_mm = (mean_location + median_location)/2
if av_mm != int(av_mm):
    print("oh no...")
    print(av_mm)
    print("Rounding down to int.")
    av_mm = int(av_mm)

# some tinkering shows that averaging the argminimizers doesn't work.
# But it's a continuous process, so I should be able to 
# brute force check values between mean and median.
candidates = np.arange(median_location,mean_location+2, dtype=int)
vals = np.array([cost(positions, c) for c in candidates])

for c,v in zip(candidates, vals):
    print("%10i | %10i"%(c,v))
    
idx = np.argmin(vals)
print("Position %i has minimum fuel of %i"%(candidates[idx], vals[idx]))

# seems too close to the mean; theoretically should be distinct 
# from mean for arbitrary data? since cost function should be 
# purely the quadratic for the mean? 

