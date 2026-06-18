import numpy as np

def intersect(x1, y1, x2, y2, b1, b2): # calcs intersect location
    # input is coeff of x1, y1, x2, y2, then the two y intercepts
    A = np.array([[x1, y1], [x2, y2]])
    b = np.array([b1, b2])
    return np.linalg.solve(A, b)
    # output is [x, y] of intersect