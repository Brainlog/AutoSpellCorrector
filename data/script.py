fil = open("pred.txt","r")
fil2 = open("output.txt","r")
j = 1
while j <= 15:
    s1 = fil.readline()
    s2 = fil2.readline()
    print(f's1: {s1}')
    print(f's2: {s2}')
    diff=0
    count = 0
    for i in range(len(s2)):
        if s1[i]==s2[i]:
            diff+=1
        count += 1    
    print(f'{(diff/count)*100}% CHARACTERS MATCH...\n\n')
    j += 1