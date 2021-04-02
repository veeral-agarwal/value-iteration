import numpy as np 
action= ["UP", "LEFT", "DOWN", "RIGHT", "STAY", "SHOOT", "HIT", "CRAFT", "GATHER", "NONE"] 
health=[0,25,50,75,100]
pos=["C","N","E","W","S"]
arrows=[0,1,2,3]
mat=[0,1,2]
mmstate=["D","R"] #can be D or R
#tuple such that , [ij actions ,[(prob ,destination),(prob,dest)]
#calculate all the utilites of state, use joint probability to find where its nexstate.(idk)
possibility={
    "C" : [["UP",[(0.85,"N"),(0.15,"E")]],["DOWN",[(0.85,"S"),(0.15,"E")]],["STAY",[(0.85,"C"),(0.15,"E")]],["RIGHT",[(1,"E")]],["LEFT",[(0.85,"W"),(0.15,"E")]],["SHOOT",[(0.5,25),(0.5,0)]],["HIT",[(0.1,50),(0.9,0)]]],
    "N" : [["DOWN",[(0.85,"C"),(0.15,"E")]],["STAY",[(0.85,"N"),(0.15,"E")]],["CRAFT",[(0.5,1),(0.35,2),(0.15,3)]]],
    "S" : [["UP",[(0.85,"C"),(0.15,"E")]],["STAY",[(0.85,"S"),(0.15,"E")]],["GATHER",[(0.75,1),(0.25,0)]]],
    "W" : [["RIGHT",[(1,"C")]],["STAY",[(1,"W")]],["SHOOT",[(0.25,25),(0.75,0)]]],
    "E" : [["LEFT",[(1,"C")]],["STAY",[(1,"E")]],["SHOOT",[(0.9,25),(0.1,0)]],["HIT",[(0.2,50),(0.8,0)]]]
}
stepcost=-20
delta=0.001
iterations=0
#600 possible combinations 
#for each comb calcualte util from bellman update eqn 
#probbabilites maynot be idependent in few cases
# for every iteration take all possible actions and all rewards u get 
# our step cost is -20
# gg dude.don't freak out its ok.
#write for one iteration
def updateutility(arr,count):
    #get all actions first, and for each action get rew, util, prob and use bellman update
    no_of_actions=len(possibility[arr[0]])
    for act in possibility[arr[0]]:
        
        







optimalactions=[0 for i in range(600)]#will be of latest gens 
allstates=[]
gen1utils=[0 for i in range(600)]
gen2utils=[]
count=0
for a1 in pos:
    for a2 in mat:
        for a3 in arrows:
            for a4 in mmstate:
                for a5 in health:
                    allstates.append([a1,a2,a3,a4,a5])
                    utility=updateutility([a1,a2,a3,a4,a5],count)
                    gen1utils[count]=utility
                    count+=1

#print(allstates)