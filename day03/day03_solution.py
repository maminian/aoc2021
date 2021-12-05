
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
        print(self.gamma_rate * self.epsilon_rate)
        
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
    
    
    
if __name__=="__main__":
    solver = Solver()
    solver.solve()
