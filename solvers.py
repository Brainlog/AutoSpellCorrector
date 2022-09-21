from decimal import ROUND_HALF_DOWN
from itertools import count
import time
import random
from tracemalloc import start
class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn
        self.best_state = None 
        
    def whole_string_substituter(self,str):
        #inverse dictionary
        conf_mat2 = []
        dict = {}        
        #whole string (which character to be substituted)
        conf_mat=[]                
        for i in range(0,26):
            conf_mat2.append([chr(97+i)])
        count = 0    
        for i in range(0,26):
            ch = chr(97+i)
            if self.conf_matrix[ch] == self.conf_matrix.keys():
                # pass
                print(count)
                count += 1
            else:
                for ch2 in self.conf_matrix[ch]:
                    conf_mat2[ord(ch2)-97].append(ch)
        for i in range(0,26):
            # print(conf_mat2[i])
            dict[chr(97+i)]= conf_mat2[i]               
        for x in range(len(str)):
            conf_mat.append([])
        for x in range(len(str)):
            if (str[x]!=' '):
                conf_mat[x]=dict[str[x]]
        return conf_mat  
    
    def local_search(self, str, left, right, segment_diff,israndom, debug, loopcounts, timeout):
        tabulist = []
        self.best_state = str
        curr = self.best_state
        next_node = curr
        count = 0
        conf_mat = self.whole_string_substituter(str)
        if debug:
            print(conf_mat)
        
        global_count = left
        loopcount = 0
        mintillnow = list(str)
        
        while True:
            count += 1
            if debug:
                print(f"Loop number : {count}")
            curr = next_node
            lisnext = list(next_node)
            mintillnow = lisnext
            end = min(global_count+segment_diff,right)
            peak = True
            
            
            for i in range(global_count,end):
                
                if lisnext[i] != " ":  
                    for j in range(len(conf_mat[i])):
                        testing = list(next_node)
                        testing[i] = conf_mat[i][j]
                        listostring = ""
                        for k in range(len(testing)):
                            listostring += testing[k]
                        listostringmin = ""    
                        for k in range(len(mintillnow)):
                            listostringmin += mintillnow[k]    
                        # print(listostring, " main string")  
                        if debug:
                            print((self.best_state), f" BEST {self.cost_fn(self.best_state)}")  
                            print((listostringmin), f" MIN {self.cost_fn(listostringmin)}")
                            print((listostring), f" CHKING {self.cost_fn(listostring)}")
                        if timeout > 0:
                            time.sleep(timeout)  
                        if self.cost_fn(listostring) < self.cost_fn(listostringmin):
                            chking = False
                            for y in range(len(tabulist)):
                                if tabulist[y] == listostring:
                                    chking = True
                            if chking == True:
                                pass
                            else:
                                peak = False
                               
                                if len(tabulist) < 100:
                                    mintillnow = testing
                                    tabulist.append(mintillnow)
                                else:
                                    tabulist.pop(0)
                                    mintillnow = testing
                                    tabulist.append(mintillnow)     
                            
                            result = ""
                            for k in range(0,len(mintillnow)):
                                result += mintillnow[k]  
                            if self.cost_fn(self.best_state) >= self.cost_fn(result):
                                self.best_state = result 
            if israndom:
                if peak:
                    if debug:
                        print("IT IS A PEAK, RANDOMIZING STRING")
                    next_node = ""
                    for itr in  range(0,len(self.best_state)):
                        if global_count <= itr and itr < end:
                            if self.best_state[itr] != " ":
                                randomnumber = random.randint(0,1000000)
                                randomnumber = randomnumber%len(conf_mat[itr])
                                next_node += conf_mat[itr][randomnumber]
                            else:
                                next_node += " "    
                        else:
                            next_node += self.best_state[itr]        
                    loopcount += 1        
                    if loopcount > loopcounts:   
                        print("HERE")   
                        global_count += segment_diff
                        loopcount = 0
                    next_node = self.best_state
                    if debug:
                        print("RUNNING LOCAL SEARCH ON SEGMENT : ", global_count, " This is loop count : ", loopcount)
                    if global_count >= len(lisnext):
                        break
                else:               
                    next_node = ""            
                    for k in range(len(mintillnow)):
                        next_node += mintillnow[k]
                    global_count += segment_diff    
                    if global_count >= len(lisnext):
                        break
            else:
                if peak:
                    if debug:
                        print("IT IS A PEAK ENDING LOCAL SEARCH")    
                    break   
                else:                
                    next_node = ""            
                    for k in range(len(mintillnow)):
                        next_node += mintillnow[k]
                    global_count += segment_diff    
                    if global_count >= len(lisnext):
                        break
                              
    def search(self, start_state):
        # self.local_search(string, left, right, segment_diff, random, debug, loopcounts, timeout)
        self.local_search(start_state, 0, len(start_state), 15, True, True, 1, 0)
        stry = self.best_state
        self.local_search(stry, 0, len(stry), 15, True, True, 1, 0)
        
        
        
        
    
        
                    
        
             
       
                
      
      
