n = int(input())

for i in range(n):
    T, U, P = map(float, input().split())
    P = int(P)
    
    if P == 1:
        print("NAO REGAR")
    else:
        if T > 30.0 and U < 50:
            print("REGAR")
        else:
            print("NAO REGAR")
