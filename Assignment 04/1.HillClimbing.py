import copy

class MyBlockProblem:
    def __init__(self, start, goal):
        self.currentState=start
        self.goalState=goal
        self.prevState=None

    def isGoalReached(self):
        for i in range(0, 4):
            if self.currentState[i]==goal:
                return True
        
        return False

    def displayState(self):
        for i in range(0, 4):
            if self.currentState[i]!=[]:
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("------------------")
        print("******************************************")

    def movefromStackXtoStackY(self, x, y):
        if self.currentState[x]!=[] and len(self.currentState[y])!=4:
            self.prevState=copy.deepcopy(self)
            block=self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):
        stateList=[]
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state=copy.deepcopy(self)
                if i!=j and copy_state.movefromStackXtoStackY(i, j):
                    stateList.append(copy_state)
                    
        return stateList

    def heuristic(self):
        value=0

        for i in range(0, 4):
            if self.currentState[i]!=[]:
                if self.currentState[i][0]==self.goalState[0]:
                    value+=1
                else:
                    value-=1

        
        for i in range(0, 4):
            goalBlock=self.goalState[i]
            goalBlockIndex=i
            for j in range(0, 4):
                flag=0
                for k in range(0, len(self.currentState[j])):
                    if self.currentState[j]!=[]: 
                        if self.currentState[j][k]==goalBlock:
                            currentBlockIndexX=j
                            currentBlockIndexY=k
                            flag=1
                            break
                if flag==1:
                    flag=0
                    break
            
            if self.currentState[currentBlockIndexX][currentBlockIndexY-1]==self.goalState[goalBlockIndex-1] and currentBlockIndexY!=0 and goalBlockIndex!=0:
                value+=1
            else:
                if currentBlockIndexY!=0:
                    value-=1
                
        return value

def constructPath(goalState):
    print("Displaying path from start to goal")
    while goalState:
        goalState.displayState()
        goalState=goalState.prevState
    
    return 1

def HillClimbing(startState):
    open=[]
    closed=[]
    
    open.append(startState)

    returnVal=0
    while open:

        thisState=open.pop(0)
        thisState.displayState()

        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            returnVal=constructPath(thisState)
            break
        
        nextStates=thisState.possibleNextStates()

        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)
                    break
                    
    
    if returnVal!=1:
        print("Error: Local Maxima")

                
start=[[2, 3, 4, 1], [], [], []]
goal=[1, 2, 3, 4]
problem=MyBlockProblem(start, goal)
HillClimbing(problem)
