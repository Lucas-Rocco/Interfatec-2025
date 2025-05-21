q = int(input())
cont = 0

for i in range(q*2):
 
    if i % 2 == 0:
        valdor = int(input())
        cont += 1
    else:
        valdag = int(input())
        cont += 1
    
    if cont == 2:
        
        if valdor > valdag and (valdor + valdag) > 40:
            print("DOROTHY DECIDE E A NONNA VAI")
        elif valdor > valdag:
            print("DOROTHY DECIDE")
        elif valdag > valdor and (valdor + valdag) > 40:
            print("DAGMAR DECIDE E A NONNA VAI")
        else:
            print("DAGMAR DECIDE")
        
        valdor = 0
        valdag = 0
        cont = 0