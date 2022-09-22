import time
import random
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
    
    def local_search(self, str, left, right, segment_diff,israndom, debug, loopcounts, timeout, dfs, dfsfactor):
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
                    loopcount += 1        
                    if loopcount > loopcounts:     
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
    
    
    
    def local_beam_search(self, str, left, right, segment_diff,israndom, debug, loopcounts, timeout, dfs, dfsfactor, n):
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
        store = []
        resultbeam = [curr]
        while True:
            for hue in range(0,len(resultbeam)):  
                count += 1
                if debug:
                    print(f"Loop number : {count}")
                curr = resultbeam[hue]
                lisnext = list(resultbeam[hue])
                mintillnow = lisnext
                end = min(global_count+segment_diff,right)
                peak = True         
                for i in range(global_count,end):                
                    if lisnext[i] != " ":  
                        for j in range(len(conf_mat[i])):
                            testing = list(resultbeam[hue])
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
                            chk = False   
                            for hu2 in range(0,len(store)):
                                if listostring == store[hu2]:  
                                    chk = True
                            if chk == False:        
                                store.append([self.cost_fn(listostring),listostring])       
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
            store.sort()
            # store.reverse()
            resultbeam = []
            for hue3 in range(0,n):
                resultbeam.append(store[hue3][1])

            store = []    
            # print(resultbeam)
                              
                                
                                
            if israndom:
                if peak:
                    if debug:
                        print("IT IS A PEAK, RANDOMIZING STRING")
                     
                    next_node = ""      
                    loopcount += 1        
                    if loopcount > loopcounts:     
                        global_count += segment_diff
                        loopcount = 0
                    next_node = self.best_state        
                    
                    if debug:
                        print("RUNNING LOCAL SEARCH ON SEGMENT : ", global_count, " This is loop count : ", loopcount)
                    if global_count >= len(lisnext):
                        break
                else:               
                    # next_node = ""            
                    # for k in range(len(mintillnow)):
                        # next_node += mintillnow[k]
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
    def dfs(self, stry, left, right, dfsfactor):
             # print(next_node, "INITIAL ", self.cost_fn(next_node))
                        # next_node = self.best_state
                        conf_mat = self.whole_string_substituter(stry)
                        if right - left <= dfsfactor:
                            stack=[]
                            stack.append((self.best_state,left))
                            print(left, " ", right)
                            while(len(stack)>0):
                                (node,ind) = stack.pop()
                                print(f'NODE RECIEVED: {node}')
                                if(self.cost_fn(node)<self.cost_fn(self.best_state)):
                                    self.best_state=node
                                if(node[ind]!=' '):
                                    for q_i in range(len(conf_mat[ind])):
                                        strnew = ''
                                        for d in range(len(node)):
                                            if(ind!=d):
                                                strnew+=node[d]
                                            else:
                                                strnew+=conf_mat[ind][q_i]
                                        if(ind+1<right):
                                            stack.append((strnew,ind+1))
                                else:
                                    if(ind+1<right):
                                        stack.append((node,ind+1))             
                              
    def search(self, start_state):
        # self.local_search(string, left, right, segment_diff, random, debug, loopcounts, timeout, dfs, dfsfactor, beamfacotr)
        # self.local_search(start_state, 0, len(start_state), 15, True, False, 1, 0, False, 5)
        # stry = self.best_state
        # self.local_search(stry, 0, len(stry), 15, True, False, 1, 0, False, 5)
        # stry = self.best_state
        # self.local_beam_search(stry, 0, len(stry), 15, True, False,1, 0, False, 5, 16)
        # # stry = self.best_state
        # # self.local_search(stry, 0, len(stry), len(stry), 15, True, 1, 0, False, 5)
        # # stry = self.best_state
        # # self.local_search(stry, 0, len(stry), len(stry), 15, True, 1, 0, False, 5)
        # # stry = self.best_state
        # # self.local_search(stry, 0, len(stry), len(stry), 15, True, 1, 0, False, 5)
        
        # print("khtm")
        wordlim = []
        init = 0
        end = 0
        count = 0
        for i in range(len(start_state)):
            if(start_state[i]==' '):
                if(count>4):
                    end = i
                    wordlim.append((init,end+1))
                    init = i+1
                    count = 0
                    
            count+=1

        # # print("khtm")
        l = len(start_state)
        i=0
        t = len(wordlim)
        while(i<t):
            tup=(wordlim[i][0], wordlim[i][1])
            print(f'COST FUN OF SEGMENT {start_state[tup[0]:tup[1]]}: {self.cost_fn(start_state[tup[0]:tup[1]])}')
            i+=1
        print(f'COST FUN OF SENTENCE {start_state}: {self.cost_fn(start_state)}')
        
        
        
        
    
        
                    
        
             
       
                
      
      
