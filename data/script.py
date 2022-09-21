fil = open("output.txt","r")
fil2 = open("pred.txt","r")
s1 = fil.read()
s2 = fil2.read()
diff=0
count = 0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        diff+=1
    count += 1    
print(f'{(diff/count)*100}% CHARACTERS MATCH...\n\n')