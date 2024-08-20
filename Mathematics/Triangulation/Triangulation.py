import math
from sys import argv

def main(): # only executes if not imported by another program
    if len(argv) != 7 or "-h" in argv or "--help" in argv:
        usage = """
        Usage: python %s x1 y1 x2 y2 angle1(degrees) angle2(degrees)

        When given two points A(x1, y1) and B(x2, y2), and the angles PAB(angle1) and PBA(angle2), finds the coordinate of P using triangulation.(outputs both possibilities) \n"""%argv[0]
        print(usage)
        exit(0)


    for i in range(len(argv)):
        try:
            argv[i] = float(argv[i])
        except:
            continue

    _, x1, y1, x2, y2, angle1, angle2 = argv
    angle1 = math.radians(angle1)
    angle2 = math.radians(angle2)

    if (x1>x2): # swap points if x2 is smaller than x1 (equation only works if the second point has a greater x value)
        temp = x1
        x1 = x2
        x2 = temp
        temp = y1
        y1 = y2
        y2 = y1
    
    x,y = Triangulate(x1, y1, x2, y2, angle1, angle2)
    print(f"\n({x[0]}, {y[0]})\n\n({x[1]}, {y[1]})\n")

def get_intersections_between_circles(x0, y0, r0, x1, y1, r1): # https://stackoverflow.com/questions/55816902/finding-the-intersection-of-two-circles
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        return [x3,x4],[y3,y4]

def Triangulate(x1, y1, x2, y2, angle1, angle2): # Triangulate
    # Distance from the two given points
    d1 = math.sqrt(math.pow(x1-x2, 2)+math.pow(y1-y2, 2))

    # https://en.wikipedia.org/wiki/Triangulation_(surveying)#:~:text=%F0%9D%9B%BD-,therefore%3A,-%F0%9D%91%91

    # Calculate the distance from line between two points to the point P
    d = d1*((math.sin(angle1)*math.sin(angle2))/(math.sin(angle1+angle2)))

    # Calculate the distance from P to A and P to B
    d_A = d/math.sin(angle1)
    d_B = d/math.sin(angle2)

    # Calculate intersection between two circles that represent the possible coordinates (oh god help me pls)
    # https://math.stackexchange.com/questions/256100/how-can-i-find-the-points-at-which-two-circles-intersect
    x = [0, 0] # two solutions for coordinate
    y = [0, 0]
    x,y = get_intersections_between_circles(x1, y1, d_A, x2, y2, d_B)

    return x, y

if __name__ == '__main__':
    main()