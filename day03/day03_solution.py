
class Solver:
    def __init__(self,fname='input'):
        import csv
        with open(fname, 'r') as f:
            csvr = csv.reader(f)
            self.lines = [l[0] for l in csvr]
        self.width = len(self.lines[0])
        self.height = len(self.lines)
        
        self.gamma_rate_strb = ''
        self.epsilon_rate_strb = ''
        
    def get_gamma_strb(self):
        '''Problem describes gamma rate as 
        a strb number where each position is the 
        most common value seen in that position 
        for all strbs in the puzzle input.'''
        gamma_strb = ''
        for p in range(self.width):
            counts = {'0':0,'1':0}
            for i in range(self.height):
                counts[self.lines[i][p]] += 1
                if counts['0'] > self.height//2:
                    gamma_strb += '0'
                    break
                elif counts['1'] > self.height//2:
                    gamma_strb += '1'
                    break
        self.gamma_rate_strb = gamma_strb
        self.gamma_rate = self.strb_to_integer(gamma_strb)
        
    def get_epsilon_strb(self):
        if len(self.gamma_rate_strb)==0:
            self.get_gamma_strb()
        temp = ['1' if gi=='0' else '0' for gi in self.gamma_rate_strb]
        self.epsilon_rate_strb = ''.join(temp)
        self.epsilon_rate = self.strb_to_integer(self.epsilon_rate_strb)
    
    def solve(self):
        self.get_epsilon_strb()
        return self.gamma_rate * self.epsilon_rate
        
    def strb_to_integer(self,val):
        '''
        input: val; expected "string binary"
            (don't want to use built-in binary tools)
        '''
        assert( type(val) == str )
        s = 0
        for i,v in enumerate(val):
            s += 2**(len(val)-i-1)*int(v)
        return s
    
    def filter_raw(self):
        '''
        Working off of the gamma and epsilon values, 
        search bit by bit and filter out based on majority/minority 
        in the current list of entries by position, until a single 
        entry remains.
        
        Low tech version right now; todo (i.e. will never do)
        implement version that works based on operator.gt or operator.lt 
        input to switch between cases.
        
        Oxygen rating : ties for majority value go to '1'
        CO2 rating : ties for minority value go to '0'
        '''
        # oxygen
        mask = range(self.height)
        for p in range(self.width):
            counts = {'0':0,'1':0}
            keeps = []
            for m in mask:
                counts[self.lines[m][p]] += 1
            if counts['0'] > counts['1']:
                filter_bit = '0'
            else:
                filter_bit = '1'

            keeps = [m for m in mask if self.lines[m][p]==filter_bit]
            mask = list(keeps)
            if len(mask)==1:
                o2_result = mask[0]
                break

        # carbon dioxide
        mask = range(self.height)
        for p in range(self.width):
            counts = {'0':0,'1':0}
            keeps = []
            for m in mask:
                counts[self.lines[m][p]] += 1
            if counts['0'] > counts['1']:
                filter_bit = '1'
            else:
                filter_bit = '0'

            keeps = [m for m in mask if self.lines[m][p]==filter_bit]
            mask = list(keeps)
            if len(mask)==1:
                co2_result = mask[0]
                break

        return (self.lines[o2_result], self.lines[co2_result])
        
    def filter(self):
        o,c = self.filter_raw()
        self.o2_filter_strb = o
        self.co2_filter_strb = c
        
        self.o2_filter = self.strb_to_integer( self.o2_filter_strb )
        self.co2_filter = self.strb_to_integer( self.co2_filter_strb )
        
        return self.o2_filter * self.co2_filter
#


if __name__=="__main__":
    solver = Solver()
    p1 = solver.solve()
    print('part 1: %i'%p1)
    p2 = solver.filter()
    print('part 2: %i'%p2)
