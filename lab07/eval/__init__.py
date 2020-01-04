def buildTree():
    x = BinaryTree('+')
    insertLeft(x,'a')
    insertRight(x,'/')
    insertLeft(getRightChild(x),'b')
    insertRight(getRightChild(x),'c')
    return x
    
def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

#gets the num from envoriment dictionary
def envVal(rootVal,env):
    if env.get(rootVal) != None:
        return env.get(rootVal)
    else:
        return None

def eval(rootVal,left_eval,right_eval):
    if rootVal  == '+': 
        return left_eval + right_eval 
      
    elif rootVal == '-': 
        return left_eval - right_eval 
      
    elif rootVal  == '*': 
        return left_eval * right_eval 
      
    elif rootVal == '/': 
        if right_eval != 0:
            return left_eval / right_eval
        else: 
            return None #if dividing by zero it will return 0 
    else:
        return 0
    
    

def evalTree(tree, env):
    if getRootVal(tree) == []:
        return 0
    #base case end of tree
    if getLeftChild(tree) == [] and getRightChild(tree) == []:
        return envVal(getRootVal(tree),env) #gets the num from envoriment dic
    #evaluate both sides
    left_eval = evalTree(getLeftChild(tree),env)
    right_eval = evalTree(getRightChild(tree),env)
    #helper method evaulates left and right sides
    print(left_eval,getRootVal(tree),right_eval)
    if left_eval != None and right_eval != None:
        return eval(getRootVal(tree),left_eval,right_eval)
    else:
        return None
    

  

env = {
    'a': 10,
    'b': 30,
    'c': 30,
}

#test stuff
#r = buildTree()
#l = getRightChild(r)
#c = getRightChild(getRightChild(getRightChild(r)))
#print(r)
#print(l)
#print(c)
#print(env.get('a'))
#print(evalTree(r, env))
