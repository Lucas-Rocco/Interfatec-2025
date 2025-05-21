import math

a, b, c = 1, 1, 1

while a != 0 and b != 0 and c != 0 :

    a, b, c = map(float,input().split())

    if a != 0 and b != 0 and c != 0 :

        c = math.radians(c)
        
        area = 1/2*(a*b)*math.sin(c)

        print('{:.4f}'.format(area))

