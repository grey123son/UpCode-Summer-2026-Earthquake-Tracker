import numpy as np

def intersect(x1, y1, x2, y2, b1, b2): # calcs intersect location
    # input is coeff of x1, y1, x2, y2, then the two y intercepts
    A = np.array([[x1, y1], [x2, y2]])
    b = np.array([b1, b2])
    return np.linalg.solve(A, b)
    # output is [x, y] of intersect 

def findTheta(x1, y1, x2, y2): # input is x and y of CHOSEN POINT, then x and y of other point
    if (x2 - x1) == 0:
        return np.pi / 2
    elif y2 - y1 == 0:  
        if (x2 - x1) > 0:
            return 0
        else:
            return np.pi
    else:
        return np.arctan2(y2 - y1, x2 - x1)
