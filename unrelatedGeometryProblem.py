import math

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculate coordinate differences
    xdiff = (x1 - x2, x3 - x4)
    ydiff = (y1 - y2, y3 - y4)

    # Determinant helper function
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    # Calculate the denominator (the main determinant)
    div = det(xdiff, ydiff)
    
    # If the denominator is 0, the lines are parallel or collinear
    if div == 0:
        return None

    # Calculate the numerators using Cramer's Rule
    d = (det((x1, y1), (x2, y2)), det((x3, y3), (x4, y4)))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    
    return x, y

def findTheta(x1, y1, x2, y2): # input is x and y of CHOSEN POINT, then x and y of other point
    if (x2 - x1) == 0:
        return math.pi / 2
    elif y2 - y1 == 0:
        if (x2 - x1) > 0:
            return 0
        else:
            return math.pi
    else:
        return math.atan2(y2 - y1, x2 - x1)

useLater = [0, 1, 2, 3]

def diagonal_crossing(points):
    # points is a list of [x, y] coordinates
    # returns the intersection point of the diagonals
    # screw codingbat for using python2 btw
    minYi = 0
    minY = points[0][1]
    for i in range(1, len(points)):
        if points[i][1] < minY:
            minY = points[i][1]
            minYi = i

    useLater.remove(minYi)
    
    thetas = [-1, -1, -1, -1] 
    # we chose min y so we're guaranteed to be in quadrant 1 or 2, meaning REAL thetas between 0 and pi
    for i in range(len(points)):
        if i != minYi:
            thetas[i] = findTheta(points[minYi][0], points[minYi][1], points[i][0], points[i][1])

    maxTheta = thetas.index(max(thetas))
    useLater.remove(maxTheta)

    if thetas[useLater[0]] > thetas[useLater[1]]:
        return intersect(points[minYi][0], points[minYi][1], points[useLater[0]][0], points[useLater[0]][1], points[maxTheta][0], points[maxTheta][1], points[useLater[1]][0], points[useLater[1]][1])
    else:
        return intersect(points[minYi][0], points[minYi][1], points[useLater[1]][0], points[useLater[1]][1], points[maxTheta][0], points[maxTheta][1], points[useLater[0]][0], points[useLater[0]][1])