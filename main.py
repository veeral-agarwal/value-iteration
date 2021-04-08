import numpy as np 
import copy
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
    "N" : [["CRAFT",[(0.5,1),(0.35,2),(0.15,3)]],["STAY",[(0.85,"N"),(0.15,"E")]],["DOWN",[(0.85,"C"),(0.15,"E")]]],
    "S" : [["GATHER",[(0.75,1),(0.25,0)]],["UP",[(0.85,"C"),(0.15,"E")]],["STAY",[(0.85,"S"),(0.15,"E")]]],
    "W" : [["SHOOT",[(0.25,25),(0.75,0)]],["RIGHT",[(1,"C")]],["STAY",[(1,"W")]]],
    "E" : [["SHOOT",[(0.9,25),(0.1,0)]],["HIT",[(0.2,50),(0.8,0)]],["LEFT",[(1,"C")]],["STAY",[(1,"E")]]],
    "D" : [[0.2,"R"],[0.8,"D"]],
    "R" : [[0.5,"D"],[0.5,"R"]] #this combination of RnD is shoot spot where you have to change ur reward function.
}
possibilitynew={         #for case1 task2
    "C" : [["UP",[(0.85,"N"),(0.15,"E")]],["DOWN",[(0.85,"S"),(0.15,"E")]],["STAY",[(0.85,"C"),(0.15,"E")]],["RIGHT",[(1,"E")]],["LEFT",[(0.85,"W"),(0.15,"E")]],["SHOOT",[(0.5,25),(0.5,0)]],["HIT",[(0.1,50),(0.9,0)]]],
    "N" : [["CRAFT",[(0.5,1),(0.35,2),(0.15,3)]],["STAY",[(0.85,"N"),(0.15,"E")]],["DOWN",[(0.85,"C"),(0.15,"E")]]],
    "S" : [["GATHER",[(0.75,1),(0.25,0)]],["UP",[(0.85,"C"),(0.15,"E")]],["STAY",[(0.85,"S"),(0.15,"E")]]],
    "W" : [["SHOOT",[(0.25,25),(0.75,0)]],["RIGHT",[(1,"C")]],["STAY",[(1,"W")]]],
    "E" : [["SHOOT",[(0.9,25),(0.1,0)]],["HIT",[(0.2,50),(0.8,0)]],["LEFT",[(1,"W")]],["STAY",[(1,"E")]]],
    "D" : [[0.2,"R"],[0.8,"D"]],
    "R" : [[0.5,"D"],[0.5,"R"]] #this combination of RnD is shoot spot where you have to change ur reward function.
}
stepcost=-10
delta=0.001
iterations=0
#600 possible combinations 
#for each comb calcualte util from bellman update eqn 
#probbabilites maynot be idependent in few cases
# for every iteration take all possible actions and all rewards u get 
# our step cost is -10

def getutility(arr):
    #print(arr, "is array passed")
    match=0
    ind=-1
    for j in juststates:
        match=0
        for i in range(len(arr)):
            if j[i]==arr[i]:
                match+=1
        if match==5:
            #print(j)
            ind=juststates.index(j)
            return gen2utils[ind]   
    print(arr,"is not found")
    return 0
    

def getmax(arr,count):
    temparr=[]
    for i in arr:
        temparr.append(i[0])
    ind = temparr.index(max(temparr))
    optimalvalues[count]=arr[ind][0]
    return arr[ind][1]

def updateutility(arr,count,gamma,run):
    #get all actions first, and for each action get rew, util, prob and use bellman update
    #no_of_actions=len(possibility[arr[0]]) #matches with position here  , not using now
    allaction_utils=[]
    if arr[4]==0:
        optimalactions[count]="NONE"
        optimalvalues[count]=0
    else:
        if run==1 and arr[0]=="E":        #case1 task 2
            possibility1=possibilitynew
        else:
            possibility1=possibility    
        for act in possibility1[arr[0]]:
            if act[0]=="UP" or act[0]=="DOWN" or act[0]=="RIGHT" or act[0]=="LEFT" or act[0]=="STAY" :  
                util=0
                if run==2 and act[0]=="STAY":    #case2 task2
                    step_cost=0
                else:
                    step_cost=stepcost    
                if arr[3] == "D":         #move and D
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            nextstate=[indi[1],arr[1],arr[2],mm[1],arr[4]]
                            util+=indi[0]*mm[0]*(step_cost + gamma*getutility(nextstate))
                elif arr[3]=="R":
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            if mm[1]=="D" and (arr[0]=="E" or arr[0]=="C"):
                                nextstate=[arr[0],arr[1],0,mm[1],min(arr[4]+25,100)]
                                util+=indi[0]*mm[0]*(step_cost - 40 + gamma*getutility(nextstate))    #indiana got hit 
                            else:
                                nextstate=[indi[1],arr[1],arr[2],mm[1],arr[4]]
                                util+=indi[0]*mm[0]*(step_cost + gamma*getutility(nextstate))
                allaction_utils.append([util,act[0]])

            elif act[0]=="GATHER":
                util=0
                if arr[3] == "D":         #move and D
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            nextstate=[arr[0],min(arr[1]+indi[1],2),arr[2],mm[1],arr[4]]
                            util+=indi[0]*mm[0]*(stepcost + gamma*getutility(nextstate))
                elif arr[3]=="R":
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            if mm[1]=="D" and (arr[0]=="E" or arr[0]=="C"):
                                nextstate=[arr[0],arr[1],0,mm[1],min(arr[4]+25,100)]
                                util+=indi[0]*mm[0]*(stepcost- 40 + gamma*getutility(nextstate))    #indiana got hit 
                            else:
                                nextstate=[arr[0],min(arr[1]+indi[1],2),arr[2],mm[1],arr[4]]
                                util+=indi[0]*mm[0]*(stepcost + gamma*getutility(nextstate))
                allaction_utils.append([util,act[0]]) 

            elif act[0] == "CRAFT" and arr[1]!=0:
                util=0
                if arr[3] == "D":         #move and D
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            nextstate=[arr[0],arr[1]-1,min(arr[2]+indi[1],3),mm[1],arr[4]]
                            util+=indi[0]*mm[0]*(stepcost + gamma*getutility(nextstate))
                elif arr[3]=="R":
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            if mm[1]=="D" and (arr[0]=="E" or arr[0]=="C"): #never reachess here 
                                nextstate=[arr[0],arr[1],0,mm[1],min(arr[4]+25,100)]
                                util+=indi[0]*mm[0]*(stepcost- 40 + gamma*getutility(nextstate))    #indiana got hit 
                            else:
                                nextstate=[arr[0],arr[1]-1,min(arr[2]+indi[1],3),mm[1],arr[4]]
                                util+=indi[0]*mm[0]*(stepcost + gamma*getutility(nextstate))
                allaction_utils.append([util,act[0]])    

            elif act[0] == "HIT": #hit  is possible
                util=0
                if arr[3] == "D":         #move and D
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            nextstate=[arr[0],arr[1],arr[2],mm[1],max(arr[4]-indi[1],0)]
                            if indi[1]>=arr[4]: #if game is over then you get reward 50
                                rew=50
                            else:
                                rew=0    
                            util+=indi[0]*mm[0]*(stepcost+ rew + gamma*getutility(nextstate))

                elif arr[3]=="R":
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            if mm[1]=="D" and (arr[0]=="E" or arr[0]=="C"):
                                nextstate=[arr[0],arr[1],0,mm[1],min(arr[4]+25,100)]
                                util+=indi[0]*mm[0]*(stepcost - 40 + gamma*getutility(nextstate))    #indiana got hit 
                        
                            else:
                                nextstate=[arr[0],arr[1],arr[2],mm[1],max(arr[4]-indi[1] ,0)]
                                if indi[1]>=arr[4]: #if game is over then you get reward 50, and action is possible when mm doesn't shoot at me.
                                    rew=50
                                else:
                                    rew=0 
                                util+=indi[0]*mm[0]*(stepcost + rew+ gamma*getutility(nextstate))
                allaction_utils.append([util,act[0]])

            elif act[0] == "SHOOT" and arr[2] != 0:
                util=0
                if arr[3] == "D":         #move and D
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            nextstate=[arr[0],arr[1],arr[2]-1,mm[1],max(arr[4]-indi[1],0)]
                            if indi[1]>=arr[4]: #if game is over then you get reward 50
                                rew=50
                            else:
                                rew=0    
                            util+=indi[0]*mm[0]*(stepcost+ rew + gamma*getutility(nextstate))

                elif arr[3]=="R":
                    for mm in possibility[arr[3]]: 
                        for indi in act[1]:
                            if mm[1]=="D" and (arr[0]=="E" or arr[0]=="C"):
                                nextstate=[arr[0],arr[1],0,mm[1],min(arr[4]+25,100)]
                                util+=indi[0]*mm[0]*(-40 + stepcost + gamma*getutility(nextstate))    #indiana got hit 
                        
                            else:
                                nextstate=[arr[0],arr[1],arr[2]-1,mm[1],max(arr[4]-indi[1],0)]
                                if indi[1]>=arr[4]: #if game is over then you get reward 50, and action is possible when mm doesn't shoot at me.
                                    rew=50
                                else:
                                    rew=0 
                                util+=indi[0]*mm[0]*(stepcost + rew + gamma*getutility(nextstate))
                allaction_utils.append([util,act[0]])

        optimalactions[count]=getmax(allaction_utils,count)     
    return optimalvalues[count]

#for 4 cases, first is normal 
for run in range(4):
    if run==3:
        gamma=0.25 #case3 task2
    else:
        gamma=0.999    

    if run==0:
        f = open("./outputs/part_2_trace.txt", "w") 
    elif run==1:
        f = open("./outputs/part_2_task_2.1_trace.txt", "w")
    elif run==2:
        f = open("./outputs/part_2_task_2.2_trace.txt", "w") 
    elif run==3:
        f = open("./outputs/part_2_task_2.3_trace.txt", "w")
    else:
        print("wrong run") 
    optimalactions=[0 for i in range(600)]#will be of latest gens 
    optimalvalues=[0 for i in range(600)]
    gen1utils=[0 for i in range(600)]
    gen2utils=[]
    over=1
    iterations=0
    juststates=[]
    for a1 in pos:
            for a2 in mat:
                for a3 in arrows:
                    for a4 in mmstate:
                        for a5 in health:
                            juststates.append([a1,a2,a3,a4,a5])

    while(over):
        allstates=[]
        gen2utils=copy.deepcopy(gen1utils)
        count=0
        for a1 in pos:
            for a2 in mat:
                for a3 in arrows:
                    for a4 in mmstate:
                        for a5 in health:
                            allstates.append([a1,a2,a3,a4,a5])
                            utility=updateutility([a1,a2,a3,a4,a5],count,gamma,run)
                            gen1utils[count]=utility
                            count+=1
        yeet=0
       
        for ok in range(count):
            if (gen2utils[ok]-gen1utils[ok]) <= delta:
                yeet+=1 
                
        if yeet==600:
            over=0
        # for co in range(count):
        #     print(allstates[co],optimalactions[co],optimalvalues[co])
        f.write("{}{}\n".format("iteration = ",iterations))    
        for co in range(count):
            f.write("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format('(',allstates[co][0],',',allstates[co][1],',',allstates[co][2],',',allstates[co][3],',',allstates[co][4],')',':',optimalactions[co],'=','[',round(optimalvalues[co],3),']'))   
        if iterations >150: #just a stop point in case
            over=0  
        iterations+=1  
    print(iterations)    
    f.close()       
    # for i in range(10):
    #     print(gen2utils[i], gen1utils[i])
       