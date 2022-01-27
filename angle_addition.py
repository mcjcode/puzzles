#!/usr/bin/env python

import math
from math import sin, cos, pi

def run(adeg=30,bdeg=15) :
    """
    Generate pstricks code for drawing a diagram
    to demonstrate the angle addition formulas.
    """

    a,b = map(lambda _ : _*pi/180.0, (adeg,bdeg))
    ca, cb, cab = map(cos, (a,b,a+b))
    sa, sb, sab = map(sin, (a,b,a+b))
    #
    # Here are the points, vaguely where they should
    # be on the graph (How's this for literate programming!)
    #
    D=(-sa*sb,sab);          Q=(cab,sab);           C=(ca*cb,sab)
    pass;                                           P=(ca*cb,ca*sb);
    R=(-sa*sb,sa*cb);            O=(0,0);
    A=(-sa*sb,0);                                   B=(ca*cb,0)

    lines = [(A,B),(B,C),(C,D),(D,A),(O,P),(P,Q),(Q,R),(R,O),(O,Q)]

    template = r'\psline[linewidth=0.1pt]{cc-cc}(%7.4f,%7.4f)(%7.4f,%7.4f)'
    for (P1,P2) in lines :
        print(template%(P1[0],P1[1],P2[0],P2[1]))
    template = r'\psarc[linecolor=black,linewidth=0.1pt](%7.4f,%7.4f)(%7.4f,%7.4f)'
    print(template % (O[0],O[1],0,b))
    print(template % (O[0],O[1],b,b+a))

if __name__ == '__main__' :
    run()
