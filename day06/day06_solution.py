import numpy as np

# lanternfish creates new one once very 7 days
class Lanternfish:
    def __init__(self,circ=8):
        self.circ = circ   # if 0, then spawn a new one and reset to 6.
    def next(self):
        if self.circ==0:
            self.circ=7
            flag = True
        else:
            flag = False
        self.circ -= 1
        return flag

class Lanternfish_simulation:
    def __init__(self, fname='input'):
        with open('input', 'r') as f:
            lines = f.readlines()
        lines = lines[0].split(',')
        counts = [int(l) for l in lines]
        self.feesh = [Lanternfish(c) for c in counts]
        self.day = 0
        
    def next(self):
        to_spawn = []
        for f in self.feesh:
            spawn = f.next()
            if spawn:
                to_spawn.append( Lanternfish() )
        self.day += 1
        self.feesh += to_spawn
        
    def get_readout(self):
        print('Day: %i'%self.day)
        print('Feesh: ')
        print( np.array([c.circ for c in self.feesh]) )
#

if __name__=="__main__":
    simulation = Lanternfish_simulation()
    
    for _ in range(80):
        print(len(simulation.feesh))
        simulation.next()
    print("Part 1")
    print("Population after day 80: %i"%len(simulation.feesh))

    
    simulation = Lanternfish_simulation()
    
    # probably fails
    if False:
        for i in range(256):
            print(i+1,len(simulation.feesh))
            simulation.next()
        print("Part 2")
        print("Population after day 80: %i"%len(simulation.feesh))
