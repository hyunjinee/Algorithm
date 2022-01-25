def ccw(a,b,c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1])
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())
A, B, C, D = [x1,y1], [x2,y2], [x3,y3], [x4,y4]

if ccw(A,B,C)*ccw(A,B,D) < 0 and ccw(C,D,A)*ccw(C,D,B) < 0:
    print(1)
else:
    print(0)