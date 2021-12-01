# Day 1 - determine how many times the depth measurement 
# increases relative to the previous measurement(s).
#

with open('input', 'r') as f:
    numbers = f.readlines()
    numbers = [int(n) for n in numbers]

use_numpy = False

# Part 1 - how many times do two consecutive measurements increase?

if use_numpy:
    import numpy as np

if use_numpy:
    result_p1 = sum( np.diff(numbers) > 0 )
else:
    result_p1 = 0
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            result_p1 += 1
#

print("Part 1")
print(result_p1)

##########

# Part 2.
#
# In this version, the problem asks us to do a three-number sliding window.
# Look for increases in the three-number sliding window.

if use_numpy:
    numbers = np.array(numbers)
    rolling = numbers[:-2] + numbers[1:-1] + numbers[2:]
    result_p2 = sum( np.diff(rolling) > 0 )
else:
    # After a little staring at the process, comparing rolling sums 
    # is equivalent to comparing numbers spaced three apart, 
    # instead of one apart.
    result_p2 = 0
    for i in range(3,len(numbers)):
        if numbers[i] > numbers[i-3]:
            result_p2 += 1
#

print("Part 2")
print(result_p2)
