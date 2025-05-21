ds, ys = map(int, input().split()) 
dm, ym = map(int, input().split())  

for t in range(1, 5001):
    if (t + ds) % ys == 0 and (t + dm) % ym == 0:
        print(t)
        break
