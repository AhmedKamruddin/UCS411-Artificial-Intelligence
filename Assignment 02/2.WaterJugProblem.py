import copy

class MyWaterJug():
    def __init__(self, maxCapacity, startState, goalState):
        self.maxCapacity=maxCapacity
        self.currentState=startState
        self.goalState=goalState
        self.prevState=None

    def isGoalReached(self):
        for i in range(0, len(self.currentState)):
            if self.goalState[i]!=-1 and self.currentState[i]!=self.goalState[i]:
                return False
        
        return True

    def displayState(self):
        print(self.currentState)
        print("*******************************")

    def fillSomeJugXFromTap(self, x, d):
        if self.currentState[x]+d<=self.maxCapacity[x]:
            print(f"Jug {x+1} current capacity={self.currentState[x]}. Filling {d} litres from tap")
            self.prevState=copy.deepcopy(self)
            self.currentState[x]=self.currentState[x]+d
            return True
        else:
            return False

    def pourSomeFromJugXtoJugY(self, x, y, d):
        if self.currentState[x]>0 and self.currentState[x]-d>=0 and self.currentState[y]+d<=self.maxCapacity[y]:
            print(f"Jug {x+1} current capacity={self.currentState[x]}. Jug {y+1} current capacity={self.currentState[y]}. Pouring {d} litre from Jug {x+1} to Jug {y+1}")
            self.prevState=copy.deepcopy(self)
            self.currentState[y]=self.currentState[y]+d
            self.currentState[x]=self.currentState[x]-d
            return True
        else:
            return False

    def emptySomeJugX(self, x, d):
        if self.currentState[x]-d>=0:
            print(f"Jug {x+1} current capacity={self.currentState[x]}. Emptying {d} litre from it")
            self.prevState=copy.deepcopy(self)
            self.currentState[x]=self.currentState[x]-d
            return True
        else:
            return False

    def possibleNextStates(self):
        stateList=[]

        """
        for x in range(0, len(self.currentState)):
            for d in range(1, self.maxCapacity[x]+1):
                stateCopy=copy.deepcopy(self)
                if stateCopy.fillSomeJugXFromTap(x, d):
                    stateList.append(stateCopy)
        """
        
        for x in range(0, len(self.currentState)):
            for y in range(0, len(self.currentState)):
                if x!=y:
                    for d in range(1, maxCapacity[y]+1):
                        stateCopy=copy.deepcopy(self)
                        if stateCopy.pourSomeFromJugXtoJugY(x, y, d):
                            stateList.append(stateCopy)

        for x in range(0, len(self.currentState)):
            for d in range(1, self.maxCapacity[x]+1):
                stateCopy=copy.deepcopy(self)
                if stateCopy.emptySomeJugX(x, d):
                    stateList.append(stateCopy)

        return stateList

def constructGoalPath(goalState):
    print("Printing path from start to goal")
    while goalState:
        goalState.displayState()
        goalState=goalState.prevState

def BFS(startState):
    open=[]
    closed=[]

    open.append(startState)
    
    while open:

        thisState=open.pop(0)
        thisState.displayState()

        if thisState not in closed:
            
            closed.append(thisState)

            if thisState.isGoalReached():
                print("Goal found..")
                constructGoalPath(thisState)
                break

            nextStates=thisState.possibleNextStates()
            for eachState in nextStates:
                if eachState not in open and eachState not in closed:
                    open.append(eachState)

maxCapacity=[]
start=[]
goal=[]
n=int(input("Enter no of Jugs: "))
for i in range(0, n):
    temp1, temp2, temp3=input(f"Enter max capacity, current capacity and goal capacity(-1 for don't care) of Jug {i+1}: ").split()
    maxCapacity.append(int(temp1))
    start.append(int(temp2))
    goal.append(int(temp3))

problem=MyWaterJug(maxCapacity, start, goal)
problem.displayState()
BFS(problem)
