fil = open("data/pred.txt","r")
fil2 = open("data/output.txt","r")
j = 0
accur = 0
while True:
    s1 = fil.readline()
    s2 = fil2.readline()
    if(s1=='\n' or s2=='\n'):
        print('END OF TEST CASES')
        print(f'TOTAL ACCURACY FOR {j} TEST CASES: {accur/j}%')
        break
    diff=0
    count = 0
    for i in range(len(s2)):
        if s1[i]==s2[i]:
            diff+=1
        count += 1  
    curracc=  (diff/count)*100
    j += 1
    print(f'ACCURACY {j}: {curracc}% CHARACTERS MATCH')
    accur += curracc
    
