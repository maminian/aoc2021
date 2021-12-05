
# Data format: x1,y1 -> x2,y2
import csv
import numpy as np

with open('input', 'r') as f:
    csvr = csv.reader(f, delimiter='\t')    # dummy so the dumb thing doesn't split
    lines = list(csvr)

def get_vent(csvline):
    c1,c2 = csvline[0].split(' -> ')
    x1,y1 = c1.split(',')
    x2,y2 = c2.split(',')
    return [np.array([int(x1), int(y1)]), np.array([int(x2), int(y2)])]

def get_track(vent):
    '''
    inputs:
        vent: list with two entries; coordinates of start/end of geothermal vent.
    outputs:
        track: list with multiple x,y coords (list of numpy arrays length two)
    '''
#    import pdb
#    pdb.set_trace()
    dv = vent[1] - vent[0]
    dv = np.array( dv/np.linalg.norm(dv), dtype=int )
    
    pos = np.array( vent[0] )
    coll = [np.array(pos)]
    while any(pos != vent[1]):
        pos += dv
        coll.append( np.array(pos) )
    #
    return coll
#

def test_intersection(t1,t2):
    '''
    inputs: 
        v1,v2 : two "vents;" start/end points for two 
        line segments; format [v1,v2] where v1,v2 are numpy arrays of x,y entries.
    outputs:
        intersection: Boolean; whether intersetion occurred
        loc : tuple of integers (?) if and where intersection occurred (else None)
    '''
    locs = []
    for ti in t1:
        for tj in t2:
            if all(ti==tj):
                locs.append(ti)
    if len(locs)>0:
        return True,locs
    else:
        return False,locs
#

vents = [get_vent(l) for l in lines]



# only consider horizontal/vertical lines for now.
vents_p1 = [v for v in vents if (v[0][0]==v[1][0] or v[0][1]==v[1][1]) ]

tracks_p1 = [get_track(v) for v in vents_p1]
tracks_p1 = np.concatenate( tracks_p1 )

M1 = np.zeros(tracks_p1.max(axis=0)+1)

for t in tracks_p1:
    M1[tuple(t)] += 1

intersection_count = (M1 > 1).sum()

#


