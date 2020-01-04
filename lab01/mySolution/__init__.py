import matplotlib.pyplot as plt
import random as ran

#will return a str with the passed len
def generate(srtlen):
    alpha = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(srtlen):
        res += alpha[(ran.randint(0,26))]
    return res

#compares passed str and target str characters then will return
#a percent of how correct the passed str is to the target   
def calculateScore(ranstr,goal):
    score = 0
    for i in range(len(goal)):
        if goal[i] == ranstr[i]:
            score = score + 1
    score = (score/len(goal))*100
    
    return score

#compares passed str and target str characters until it finds
#
def replaceOne(rstr, goal):
    for i in range(len(goal)):
        if goal[i] != rstr[i]:
           rstr[i] = generate(1)
           return rstr
    return rstr

#main program
#Loops until target str is made
#stores data to be printed and also used in graph
def monkeyTypist():
    goal = list("methinks it is like a weasel")#can be changed
    ranstr = list(generate(28))
    x = []
    y = []
    graphx = []
    graphy = []
    bestScore = 0
    run = 1
    while bestScore !=  100: 
        ranstr = replaceOne(ranstr,goal)
        run=(run+1)
        if calculateScore(ranstr,goal) > bestScore:
            bestScore = calculateScore(ranstr,goal)
            y.append(calculateScore(ranstr,goal))
            
        if (run%100) == 0:
            print ("String", run, ":","".join(ranstr)," Score:", calculateScore(ranstr,goal))
            graphx.append(run)
            graphy.append(bestScore)
        
    
    print ("String", run, ":","".join(ranstr)," Score:", calculateScore(ranstr,goal)) #final print for score = 100
    graphx.append(run)
    graphy.append(bestScore)
    
    #graph
    plt.scatter(graphx,graphy)
    plt.xlabel("Runs")
    plt.ylabel("Score")
    plt.show()