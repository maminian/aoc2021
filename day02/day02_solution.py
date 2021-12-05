
# submarine 
# wowee

class Solver:

    def __init__(self,fname='input'):
        with open('input', 'r') as f:
            self.lines = f.readlines()
        self.x = 0
        self.y = 0
        self.aim = 0
        self.map = {'forward': self.forward,
                    'up': self.up,
                    'down': self.down
                    }
    #
    
    def forward(self,mag):
        self.x += int(mag)
        self.y += self.aim*int(mag)
    def up(self,mag):
        self.aim -= int(mag)
    def down(self,mag):
        self.aim += int(mag)
    
    def parse_one(self,line):
        dir,mag = line.split(' ')
        self.__getattribute__(dir)(mag)
    def parse_all(self):
        for line in self.lines:
            self.parse_one(line)
    def broadcast_position(self):
        print("Current position: (%5i, %5i)"%(self.x,self.y))
    def coordinate_product(self):
        print(self.x*self.y)
#

if __name__=="__main__":
    solver = Solver()
    solver.parse_all()
    solver.broadcast_position()
    solver.coordinate_product()
    
    
