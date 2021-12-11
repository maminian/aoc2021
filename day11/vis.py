import day11_solution as d1s
from matplotlib import pyplot,colors,patheffects
import numpy as np
import os

pyplot.style.use('dark_background')
palette = pyplot.cm.Greys_r(np.linspace(0,1,20))
text_colors = {i:palette[i+1] for i in range(len(palette)-1)}

def number_grid(ax,idx,arr):
    # reset the axis.
    ax.set_title('Step: %4i'%idx, loc='left', fontsize=16)
    for t in ax.texts[::-1]:
        t.remove()
    for c in ax.collections[::-1]:
        c.remove()
    
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            # Create a glow effect that increases based on magnitude 
            # over 9 (here, linewidth is between 1 and 4 if arr[i,j]>9).
            thicc = (arr[i,j]>9)*(1 + min(max(0,arr[i,j]-10), 3))
            glowy = [patheffects.withStroke(linewidth=thicc, foreground="white")]
            
            ax.text(i+0.5,j+0.5,arr[i,j], color=text_colors[arr[i,j]], fontsize=24, ha='center', va='center', zorder=100, path_effects=glowy)

    return
#

sidx = d1s.step_idxs    # the step number (will have duplicates)
states = d1s.states     # the state of system (one to one with sidx)

# general settings
fig,ax = pyplot.subplots(1,1, figsize=(6,6), constrained_layout=True)
ax.set_xlim([0,states[0].shape[0]])
ax.set_ylim([0,states[0].shape[1]])
for s in ax.spines.values():
    s.set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

if True:
    # dump frames of movie in subfolder
    for i in range(len(sidx)):
        si,state = sidx[i], states[i]
        number_grid(ax, si, state)
        fname = 'frames/%s.png'%str(i).zfill(5)
        if not os.path.exists( os.path.dirname(fname) ):
            os.mkdir( os.path.dirname(fname) )
        fig.savefig(fname)
        print('%i of %i'%(i+1,len(sidx)))
        if si==51:
            break
else:
    # look at one frame for tinkering.
    i=2
    si,state = sidx[i], states[i]
    number_grid(ax, si, state)
    fig.show()
    pyplot.ion()
    

