#!/usr/bin/env python

from itertools import product

def repeats_generator(n) :
    for seq in product(*([[0,1]]*n)) :
        seq2 = seq + seq
        found_shadow = any([[seq2[:j] == seq2[j:2*j]] for j in range(1,n)])
        if not found_shadow :
            yield seq2
            
def count_repeats(depth=10) :
    for i in xrange(2**depth) :
        for j in range(depth/2-1) :
            if (i&(2**j-1))==(i>>j) :
                print i,j
                break
                
def draw_repeat_sections(depth=10,fillstyle='solid',fillcolor='gray') :
    psparams = 'fillstyle=%s,fillcolor=%s' % (fillstyle,fillcolor)
    for i in range(1,depth) :
        nsteps = 2**(2*i)
        width = 1./nsteps
        for j in range(nsteps) :
            # does it repeat the first i binary digits
            if (j&(2**i-1))==(j>>i) :
                print(r'\psframe*[%s](%f,%f)(%f,%f)' %
                      (psparams,j*width,i-1,(j+1)*width,i))

if __name__ == '__main__' :
    draw_repeat_sections()
