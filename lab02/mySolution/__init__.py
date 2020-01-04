import timeit
import matplotlib.pyplot as plt

#a test to verify that get item and update item are O(1) for dictionaries
def experimentGet():
    graphx = []
    graphy = []
    counter = 0
    diction01 = {
        "A" : "1",
        "B" : "2",
        "C" : "3",
        "D" : "4",
        "E" : "5",
        "F" : "6",
        "G" : "7",
        "H" : "8",
        "I" : "9",
        "J" : "10",
    }
    #print(diction01)
    for y in range(5):
            
        for x in diction01:
            graphy.append(timeit.timeit(diction01.get(x)))
            graphx.append(counter)
            counter = counter + 1
    #graph
    plt.title("Get")
    plt.scatter(graphx,graphy)
    plt.xlabel("Runs")
    plt.ylabel("Time in seconds")
    plt.show()
    
def experimentUpdate():
    graphx = []
    graphy = []  
    for x in range(50):
        graphy.append(timeit.timeit("d1.update({1'3})", "d1 ={'1':3}"))

        graphx.append(x)
    #graph
    plt.title("Update")
    plt.scatter(graphx,graphy)
    plt.xlabel("Runs")
    plt.ylabel("Time in seconds")
    plt.show()

def experimentDel():
    graphyD = []
    graphx = []
    graphyL = []
    l = list([1,2,3,])
    d = {1 : 'one', 2: 'two', 3 : 'three'}    
    for y in range(20):
        for x in range(3):   
            graphyL.append(timeit.timeit(l.remove(x)))
            graphyD.append(timeit.timeit(del d(d.key(x))))
            

    #graph
    plt.title("Update")
    plt.scatter(graphx,graphyL)
    plt.scatter(graphx,graphyD)
    plt.xlabel("Runs")
    plt.ylabel("Time in seconds")
    plt.show()
