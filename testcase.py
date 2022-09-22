
import random
import json

fread = open('data/corpus.txt','r')
sentence = fread.read()
lines = sentence.split('\n')
# print(lines)
fread.close()
confmat=open('data/conf_matrix.json')
replace=json.load(confmat)
fwrite = open('data/input.txt','w')
inputtotal = ''
# print(replace['a'][0])
for line in lines:
    if(line=='\n' or line==' ' or line==''):
        print('ALL TEST CASES OVER')
        break
    else:
        l = len(line)
        change = random.randint(4,10)
        indices = []
        inputtext = ''
        for c in range(change):
            ind = random.randint(0,l-1)
            indices.append(ind)
        indices.sort()
        for i in range(len(line)):
            if(len(indices)>0):
                if(i==indices[0] and line[i]!=' '):
                    conf_arr=replace[line[i]]
                    r = random.randint(0,len(conf_arr)-1)
                    inputtext+=(replace[line[i]][r])
                    indices.pop(0)
                else:
                    inputtext+=line[i]
            else:
                inputtext+=line[i]
                
        inputtotal+=(inputtext+'\n')
fwrite.write(inputtotal)
fwrite.close()

        
    