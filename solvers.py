import time
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
        while True:   
            # print(next_node)
            print(self.cost_fn(self.best_state))
            # print(self.cost_fn("despite great potential developing economies ale still confronted by trade difficulties particularly debt he added "))
            print(self.cost_fn("decpite great potential developing iconomies ele still confronted by grane difficulties particularly debt he added"), " INPUT")
            print(self.cost_fn("despite great potential developing economies are still confronted by grave difficulties particularly debt he added"), " OUTPUT")
            print(count)
            count += 1
            curr = next_node        
            lisnext = list(next_node)
            mintillnow = lisnext
            # print(lisnext)
            for i in range(len(lisnext)):
                if lisnext[i] != " ":
                    characterchange = lisnext[i]     
                    for j in range(len(self.conf_matrix[characterchange])):
                        testing = list(next_node)
                        testing[i] = self.conf_matrix[characterchange][j]
                        listostring = ""
                        for k in range(len(testing)):
                            listostring += testing[k]
                        listostringmin = ""    
                        for k in range(len(mintillnow)):
                            listostringmin += mintillnow[k]    
                        # print(self.cost_fn(listostring))
                        # print(self.cost_fn(listostringmin))    
                        if self.cost_fn(listostring) <= self.cost_fn(listostringmin):
                            chking = False
                            for y in range(len(tabulist)):
                                if tabulist[y] == listostring:
                                    chking = True
                            if chking == True:
                                pass
                            else:
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
            # time.sleep(2)    
                            
                            
                            
                            
            next_node = ""            
            for k in range(len(mintillnow)):
                next_node += mintillnow[k]
            # self.best_state = next_node
            print(self.best_state, "  ", self.cost_fn(self.best_state))
            # time.sleep(2)
        return next_node        
                                            
                        
                        
                    
                                
                    
                    
        
             
       
                
      
      
