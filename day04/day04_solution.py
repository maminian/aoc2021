import numpy as np


# line 0 indicates the sequence of numbers called in bingo.

class BingoCard:
    '''
    Class for a single bingo card. Remembers the card itself, and a boolean 
    mask indicating whether numbers have been called or not. 
    Does row-sums and col-sums on the mask to search for bingos, 
    and can report True/False for every new number called.
    
    Also calculates its own "bingo score" (defined by the description of 
    the problem) as well as a more intuitive max of max-rowsum and max-colsum.
    '''
    def __init__(self,fivelines,idx=0):
        self.idx = idx
        self.card = np.zeros((5,5), dtype=int)
        for i,l in enumerate(fivelines):
            sub = l.split()
            for j,s in enumerate(sub):
                self.card[i,j] = int(s)
        self.mask = np.zeros((5,5), dtype=bool)
        self.rowsums = np.zeros(5)
        self.colsums = np.zeros(5)
        self.last = -1  # most recent number called.
        
    def check(self,number, verbose=True):
        '''
        Inputs:
            number : integer; a number called by the BingoGame.
            verbose : boolean; optional; whether to print info to terminal.
        Outputs:
            Boolean True/False; whether this card reached bingo this round.
            If verbose is True, it will also tell you its "bingo score".
        '''
        self.last = number
        self.mask += (self.card == number)
        if verbose:
            print(self.idx)
            print(self.longest_streak())
            print('')
        if max( self.mask.sum(axis=0) )==5 or max( self.mask.sum(axis=1) )==5:
            print("Bingo, card %i"%self.idx)
            print("Score: %i"%self.calculate_score())
            return True
        else:
            return False    # no bingo on this turn.
    #
    def longest_streak(self):
        return max(max(self.mask.sum(axis=0)), max(self.mask.sum(axis=1)) )
    def calculate_score(self):
        sum_unmarked = sum( self.card[ np.logical_not(self.mask) ] )
        return (self.last * sum_unmarked)
#

class BingoGame:
    '''
    Class loads the input, stores all bingo cards; serves them numbers; 
    tracks the sequence of calls; gets them to report bingos and scores.
    '''
    def __init__(self,fname='input'):
        with open('input', 'r') as f:
            lines = f.readlines()

        # load data.

        sequence = lines[0][:-1].split(',') # expecting a \n
        sequence = [int(s) for s in sequence]

        cards = []
        bingolines = []
        idx = 0
        
        for i,l in enumerate(lines[2:]):
            if len(l)>1:
                bingolines.append(l)
            if len(bingolines)==5:
                bc = BingoCard(bingolines, idx=idx)
                cards.append(bc)
                bingolines = []
                idx += 1
        self.cards = cards
        self.seq = sequence
        self.round = 0
    #
    def next(self, verbose=False):
        '''
        Inputs:
            verbose : boolean; optional; whether to print stuff to terminal.
        Outputs:
            update : boolean array; whether each bingo card has won on the 
                current round or not.
        '''
        update = np.zeros(len(self.cards), dtype=bool)
        for j,c in enumerate( self.cards ):
            update[j] = c.check(self.seq[self.round], verbose=verbose)
        self.round += 1
        return update
        
    def run_until_bingo(self, verbose=False):
        '''
        Repeatedly calls self.next() until the first bingo is achieved.
        
        Inputs:
            verbose : boolean; optional; whether to print stuff to terminal.
        '''
        winners = [False]
        while not any(winners):
            winners = self.next(verbose=verbose)
        
    def run_until_all_bingo(self, verbose=False):
        '''
        Repeatedly calls self.next() until the **last** bingo is achieved.
        Different from run_until_bingo(), as this also does the score 
        processing for that final bingo winner.
        
        '''
        self.winners = [False for _ in self.cards]
        while sum(self.winners)<99:
            self.winners = self.next(verbose=verbose)
        for j,w in enumerate(self.winners):
            if not w:
                card = self.cards[j]
                break
        while sum(self.winners)<100:
            self.winners = self.next(verbose=verbose)
        print("Last card to win: %i" % j)
        print("Last card's score: %i" % card.calculate_score())
        
    def get_status(self):
        return np.array([c.longest_streak() for c in self.cards], dtype=int)

if __name__=="__main__":
    game = BingoGame()
    game.run_until_bingo()
    game.run_until_all_bingo()

