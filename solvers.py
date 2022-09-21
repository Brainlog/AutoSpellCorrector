from decimal import ROUND_HALF_DOWN
import time
import random
from tracemalloc import start
class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far.
        self.best_state = None 
         

    def search(self, start_state):
        tabulist = []
        self.best_state = start_state
        curr = self.best_state
        next_node = curr
        count = 0
        conf_mat2 = []
        conf_mat=[]#actual
        dict = {}
        
        
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
            print(conf_mat2[i])
            dict[chr(97+i)]= conf_mat2[i]
                     
     
        
        
               
        for x in range(len(start_state)):
            conf_mat.append([])
        for x in range(len(start_state)):
            if (start_state[x]!=' '):
                conf_mat[x]=dict[start_state[x]]
                # conf_mat[x].append(start_state[x])
        # for x in range(len(start_state)):
        #     if (start_state[x]!=' '):
        #         conf_mat[x].append(start_state[x]) 
        print("----------------")
        print(conf_mat[0], start_state[0])
        print("---------------")
        global_count = 0
        loopcount = 0
        mintillnow = list(start_state)
        while True:   
            # print(next_node)
            print(self.cost_fn(self.best_state))
            # print(self.cost_fn("despite great potential developing economies ale still confronted by trade difficulties particularly debt he added "))
            print(self.cost_fn("minister"), " INPUT")
            print(self.cost_fn("miristeu"), " OUTPUT")
            print(count)
            
            count += 1
            curr = next_node        
            lisnext = list(next_node)
            mintillnow = lisnext
            peak = True
            # print(lisnext)
            end = min(global_count+15,len(lisnext))
            for i in range(global_count,end):
                
                if lisnext[i] != " ":
                    characterchange = lisnext[i]     
                    for j in range(len(conf_mat[i])):
                        # j = random.randint(0,len(conf_mat[i])-1)
                        testing = list(next_node)
                        testing[i] = conf_mat[i][j]
                        listostring = ""
                        for k in range(len(testing)):
                            listostring += testing[k]
                        listostringmin = ""    
                        for k in range(len(mintillnow)):
                            listostringmin += mintillnow[k]    
                        # print(listostring, " main string")  
                        print((self.best_state), " BEST")  
                        print((listostringmin), " MIN")
                        print((listostring), " CHKING")
                        
                        # time.sleep(0.1)  
                        # print(self.cost_fn(listostringmin))    
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
                                    
                                    # print(mintillnow)
                                    tabulist.append(mintillnow)
                                else:
                                    tabulist.pop(0)
                                    mintillnow = testing
                                    tabulist.append(mintillnow)     
                                    # print(mintillnow)   
                            
                            result = ""
                            # print(mintillnow)
                            for k in range(0,len(mintillnow)):
                                result += mintillnow[k]
                            # print(result, " ", i, " ", j, " ", self.cost_fn(result))    
                            if self.cost_fn(self.best_state) >= self.cost_fn(result):
                                self.best_state = result 
            # mintillnow = list(self.best_state)
            
            if peak:
                print("FLAG")
                
                next_node = ""
                for itr in  range(0,len(start_state)):
                    if global_count <= itr and itr < end:
                        if start_state[itr] != " ":
                            randomnumber = random.randint(0,len(conf_mat[itr])-1)
                            next_node += conf_mat[itr][randomnumber]
                        else:
                            next_node += " "    
                    else:
                        next_node += start_state[itr]        
                loopcount += 1        
                if loopcount > 3:        
                    global_count += 15
                    loopcount = 0
                    next_node = self.best_state
                print(global_count)
                if global_count >= len(lisnext):
                    break
                peak = False
                # print("THIS IS PEAK")
                # next_node = start_state
                # BFS
                # next_node = ""
                # print("hue")
                # for s in mintillnow:
                #     if s != " ":
                #         arr = []
                #         arr.append(s)
                #         for char  in self.conf_matrix[s]:
                #             arr.append(char)
                #         leng = len(arr)    
                #         p = random.randint(0,100000)
                #         p = p%(len(arr))
                #         next_node += arr[p]
                #     else:
                #         next_node += " "   
                # mintillnow = next_node        
                # print(next_node, " RANDOM NODE")        
                         
                pass
                            
                            
                            
            else:                
                next_node = ""            
                for k in range(len(mintillnow)):
                    next_node += mintillnow[k]
                print(self.best_state, "  ", self.cost_fn(self.best_state))

               
                                            
                        
                        
                    
                                
                    
                    
        
             
       
                
      
      
