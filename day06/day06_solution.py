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
    
    pop = [len(simulation.feesh)]
    for day in range(80):
        print(len(simulation.feesh))
        pop.append(len(simulation.feesh))
        simulation.next()
    print("Part 1")
    print("Population after day 80: %i"%len(simulation.feesh))

    # Expect this to obey a difference equation of some kind.
    pop = np.array(pop)
    
    # matrix of consecutive sequence values.
    max_recurrence = 10
    A = np.array([pop[i:i+max_recurrence] for i in range(max_recurrence)])
    rhs = pop[max_recurrence:2*max_recurrence]
    
    recurrence = np.linalg.solve(A,rhs)
    
    terms = np.where(abs(recurrence) > 1e-8 )[0]
    print(terms)
    print(recurrence[terms])
    # manual inspection: F_i = 1*F_{i-7} + 1*F_{i-9}
    # maybe shouldn't be surprised...
    for i in range(10,13):
        assert pop[i] == pop[i-7] + pop[i-9]
    
    # great!
    simulation = Lanternfish_simulation()
    
    pl = [len(simulation.feesh)]
    for day in range(10):
#        print(len(simulation.feesh))
        pl.append(len(simulation.feesh))
        simulation.next()
        
    p = pl[-1]
    pl = list(pl)
    for i in range(day+1, 257):
        # scratching my head with the off-by-ones.
        pl.append( pl[i-6] + pl[i-8] )
        if i<80:
            print("%4i | %9i | %9i"% (i, pl[i], pop[i]) )
            assert(pl[i] == pop[i])

    
    print("Part 2: on day 256, %i feesh via difference equation." % pl[-1])
    
