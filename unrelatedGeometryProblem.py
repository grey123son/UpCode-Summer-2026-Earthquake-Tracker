# PI = 3.141592653589793
# HALF_PI = 1.5707963267948966
    
# def taylorArctan(y, x):
#     # Returns the angle in radians between -pi and pi
#     if x == 0:
#         if y > 0: return HALF_PI
#         if y < 0: return -HALF_PI
#         return 0.0 # Undefined, but defaults to 0

#     # Use the Taylor series for arctan
#     z = y / x
#     result = z
#     term = z
#     n = 1

#     while abs(term) > 1e-10:
#         term *= -z * z
#         result += term / (2 * n + 1)
#         n += 1

#     # Quadrant adjustment logic
#     if x > 0:
#         return result
#     elif x < 0 and y >= 0:
#         return result + PI
#     else:
#         return result - PI

# def findTheta(x1, y1, x2, y2): # input is x and y of CHOSEN POINT, then x and y of other point
#     if (x2 - x1) == 0:
#         return PI / 2
#     elif y2 - y1 == 0:
#         if (x2 - x1) > 0:
#             return 0
#         else:
#             return PI
#     else:
#         return taylorArctan(y2 - y1, x2 - x1)

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
    
    return [float(x), float(y)]

useLater = [0, 1, 2, 3]

def diagonal_crossing(points):
    # points is a list of [x, y] coordinates
    # returns the intersection point of the diagonals
    # screw codingbat for using python2 btw


    # minXi = 0
    # minX = points[0][0]
    # for i in range(1, len(points)):
    #     if points[i][0] < minX:
    #         minX = points[i][0]
    #         minXi = i

    # useLater.remove(minXi)
    
    # thetas = [-10, -10, -10, -10] 
    # # we chose min x so we're guaranteed to be in quadrant 1 or 4, meaning REAL thetas between -pi and pi
    # for i in range(len(points)):
    #     if i != minXi:
    #         thetas[i] = findTheta(points[minXi][0], points[minXi][1], points[i][0], points[i][1])

    # print(thetas)

    # maxTheta = thetas.index(max(thetas))
    # useLater.remove(maxTheta)

    # if thetas[useLater[0]] > thetas[useLater[1]]:
    #     return intersect(points[minXi][0], points[minXi][1], points[useLater[0]][0], points[useLater[0]][1], points[maxTheta][0], points[maxTheta][1], points[useLater[1]][0], points[useLater[1]][1])
    # else:
    #     return intersect(points[minXi][0], points[minXi][1], points[useLater[1]][0], points[useLater[1]][1], points[maxTheta][0], points[maxTheta][1], points[useLater[0]][0], points[useLater[0]][1])

    minX = min(points, key=lambda p: p[0])[0]
    minY = min(points, key=lambda p: p[1])[1]
    maxX = max(points, key=lambda p: p[0])[0]
    maxY = max(points, key=lambda p: p[1])[1]

    inter = intersect(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1], points[3][0], points[3][1])
    if inter is not None and inter[0] > minX and inter[1] > minY and inter[0] < maxX and inter[1] < maxY:
        return inter
    
    inter = intersect(points[0][0], points[0][1], points[2][0], points[2][1], points[1][0], points[1][1], points[3][0], points[3][1])
    if inter is not None and inter[0] > minX and inter[1] > minY and inter[0] < maxX and inter[1] < maxY:
        return inter
    
    return intersect(points[0][0], points[0][1], points[3][0], points[3][1], points[1][0], points[1][1], points[2][0], points[2][1])

print(diagonal_crossing(
[[0, 1], [0, 5], [4, 1], [4, 5]]
    ))