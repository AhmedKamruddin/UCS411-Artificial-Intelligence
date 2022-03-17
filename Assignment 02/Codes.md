[Lab Assignment 02.pdf](https://github.com/AhmedKamruddin/UCS411-Artificial-Intelligence/files/8288176/Lab.Assignment.02.pdf)

Q1 WaterJugProblem.py
```
import copy

class MyWaterJug:
    def __init__(self, startState, goalState):
        self.currentState=startState
        self.goalState=goalState
        self.prevState=None

    def fillFirstJug(self):
        if self.currentState[0]<4:
            self.prevState=copy.deepcopy(self)

            self.currentState[0]=4
            print("fillFirstJug")
            return True
        else:
            #print("Cannot fill")
            return False

    def fillSecondJug(self):
        if self.currentState[1]<3:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=3
            print("fillSecondJug")
            return True
        else:
            #print("Cannot fill")
            return False

    def emptyFirstJug(self):
        if self.currentState[0]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=0
            print("emptyFirstJug")
            return True
        else:
            #print("Cannot empty")
            return False

    def emptySecondJug(self):
        if self.currentState[1]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=0
            print("emptySecondJug")
            return True
        else:
            #print("Cannot empty")
            return False

    def transferToFillFirst(self):
        sum=self.currentState[0]+self.currentState[1]
        if sum>0 and sum>=4 and self.currentState[1]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=self.currentState[1]-( 4-self.currentState[0] )
            self.currentState[0]=4
            print("transferToFillFirstJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def transferToFillSecond(self):
        sum=self.currentState[0]+self.currentState[1]
        if sum>0 and sum>=3 and self.currentState[0]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=self.currentState[0]-( 3-self.currentState[1] )
            self.currentState[1]=3
            print("transferToFillSecondJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def transferAllToFirst(self):
        sum=self.currentState[0]+self.currentState[1]
        if sum>0 and sum<=4 and self.currentState[1]>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=sum
            self.currentState[1]=0
            print("transferAllToFirstJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def transferAllToSecond(self):
        sum=self.currentState[0]+self.currentState[1]
        if sum>0 and sum<=3 and self.currentState[0]>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=0
            self.currentState[1]=sum
            print("transferAllToSecondJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def pourSomeOutOfFirst(self, d):
        if self.currentState[0]-d>0 and d>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=self.currentState[0]-d
            print("pourSomeOutOfFirstJug ", d)
            return True
        else:
            #print("Cannot pour out")
            return False

    def pourSomeOutOfSecond(self, d):
        if self.currentState[1]-d>0 and d>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=self.currentState[1]-d
            print("pourSomeOutOfSecondJug ", d)
            return True
        else:
            #print("Cannot pour out")
            return False

    def displayState(self):
        print("------------------------------------------")
        print(self.currentState)

    def isGoalReached(self):
        if self.currentState[0]==self.goalState:
            return True
        else:
            return False

    def _eq_(self, other):
        return self.currentState==other.currentState

    def possibleNextStates(self):
        stateList=[]
        
        fillFirstJug_state=copy.deepcopy(self)
        if fillFirstJug_state.fillFirstJug():
            stateList.append(fillFirstJug_state)

        fillSecondJug_state=copy.deepcopy(self)
        if fillSecondJug_state.fillSecondJug():
            stateList.append(fillSecondJug_state)

        emptyFirstJug_state=copy.deepcopy(self)
        if emptyFirstJug_state.emptyFirstJug():
            stateList.append(emptyFirstJug_state)

        emptySecondJug_state=copy.deepcopy(self)
        if emptySecondJug_state.emptySecondJug():
            stateList.append(emptySecondJug_state)

        transferToFillFirstJug_state=copy.deepcopy(self)
        if transferToFillFirstJug_state.transferToFillFirst():
            stateList.append(transferToFillFirstJug_state)

        transferToFillSecondJug_state=copy.deepcopy(self)
        if transferToFillSecondJug_state.transferToFillSecond():
            stateList.append(transferToFillSecondJug_state)

        transferAllToFirstJug_state=copy.deepcopy(self)
        if transferAllToFirstJug_state.transferAllToFirst():
            stateList.append(transferAllToFirstJug_state)

        transferAllToSecondJug_state=copy.deepcopy(self)
        if transferAllToSecondJug_state.transferAllToSecond():
            stateList.append(transferAllToSecondJug_state)

        for i in range (0, 5):
            pourSomeOutOfFirstJug_state=copy.deepcopy(self)
            if pourSomeOutOfFirstJug_state.pourSomeOutOfFirst(i):
                stateList.append(pourSomeOutOfFirstJug_state)

        for i in range (0, 4):
            pourSomeOutOfSecondJug_state=copy.deepcopy(self)
            if pourSomeOutOfSecondJug_state.pourSomeOutOfSecond(i):
                stateList.append(pourSomeOutOfSecondJug_state)

        return stateList

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

def BFS(startState):
    open=[]
    closed=[]
    open.append(startState)
    while open:
        print(len(open), len(closed))
        thisState=open.pop(0)
        #pop(0) -- queue for bfs
        #pop    -- stack for dfs
        thisState.displayState()
        if thisState not in closed:
            closed.append(thisState)
            if thisState.isGoalReached():
                print("Goal state found.. stopping search")
                constructPath(thisState)
                break
            nextStates=thisState.possibleNextStates()
            for eachState in nextStates:
                if eachState not in closed and eachState not in open:
                    open.append(eachState)

                    
start=[0, 0]
goal=2

problem=MyWaterJug(start, goal)
BFS(problem)
```
#
Q2 WaterJugProblem.py
```
import copy

class MyWaterJug:
    def __init__(self, startState, goalState):
        self.currentState=startState
        self.goalState=goalState
        self.prevState=None

    def B2A_transferToFillFirst(self):
        sum=self.currentState[0]+self.currentState[1]
        if sum>0 and sum>=12 and self.currentState[1]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=self.currentState[1]-( 12-self.currentState[0])
            self.currentState[0]=12
            print("B2A_transferToFillFirstJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def C2A_transferToFillFirst(self):
        sum=self.currentState[0]+self.currentState[2]
        if sum>0 and sum>=12 and self.currentState[2]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[2]=self.currentState[2]-( 12-self.currentState[0])
            self.currentState[0]=12
            print("C2A_transferToFillFirstJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def A2B_transferToFillSecond(self):
        sum=self.currentState[0]+self.currentState[1]
        if sum>0 and sum>=8 and self.currentState[0]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=self.currentState[0]-( 8-self.currentState[1] )
            self.currentState[1]=8
            print("A2B_transferToFillSecondJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def C2B_transferToFillSecond(self):
        sum=self.currentState[1]+self.currentState[2]
        if sum>0 and sum>=8 and self.currentState[2]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[2]=self.currentState[2]-( 8-self.currentState[1] )
            self.currentState[1]=8
            print("C2B_transferToFillSecondJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def A2C_transferToFillThird(self):
        sum=self.currentState[0]+self.currentState[2]
        if sum>0 and sum>=5 and self.currentState[0]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=self.currentState[0]-( 5-self.currentState[2] )
            self.currentState[2]=5
            print("A2C_transferToFillThirdJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def B2C_transferToFillThird(self):
        sum=self.currentState[1]+self.currentState[2]
        if sum>0 and sum>=5 and self.currentState[1]>0:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=self.currentState[1]-( 5-self.currentState[2] )
            self.currentState[2]=5
            print("B2C_transferToFillThirdJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def B2A_transferSomeToFirst(self, d):
        if d>0 and self.currentState[0]+d<=12 and self.currentState[1]-d>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=self.currentState[1]-d
            self.currentState[0]=self.currentState[0]+d
            print("B2A_transferToFillFirstJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def C2A_transferSomeToFirst(self, d):
        if d>0 and self.currentState[0]+d<=12 and self.currentState[2]-d>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[2]=self.currentState[2]-d
            self.currentState[0]=self.currentState[0]+d
            print("C2A_transferSomeToFirstJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def A2B_transferSomeToSecond(self, d):
        if d>0 and self.currentState[1]+d<=8 and self.currentState[0]-d>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=self.currentState[0]-d
            self.currentState[1]=self.currentState[1]+d
            print("A2B_transferSometoSecondJug")
            return True
        else:
            #print("Cannot transfer")
            return False
    
    def C2B_transferSomeToSecond(self, d):
        if d>0 and self.currentState[1]+d<=8 and self.currentState[2]-d>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[2]=self.currentState[2]-d
            self.currentState[1]=self.currentState[1]+d
            print("C2B_transferSometoSecondJug")
            return True
        else:
            #print("Cannot transfer")
            return False
        
    def A2C_transferSomeToThird(self, d):
        if d>0 and self.currentState[2]+d<=5 and self.currentState[0]-d>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=self.currentState[0]-d
            self.currentState[2]=self.currentState[2]+d
            print("A2C_transferSometoThirdJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    
    def B2C_transferSomeToThird(self, d):
        if d>0 and self.currentState[2]+d<=5 and self.currentState[1]-d>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[1]=self.currentState[1]-d
            self.currentState[2]=self.currentState[2]+d
            print("B2C_transferSometoThirdJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def transferAllToFirst(self):
        sum=self.currentState[0]+self.currentState[1]+self.currentState[2]
        if sum>0 and sum<=12 and self.currentState[1]>=0 and self.currentState[2]>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=sum
            self.currentState[1]=0
            self.currentState[2]=0
            print("transferAllToFirstJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def transferAllToSecond(self):
        sum=self.currentState[0]+self.currentState[1]+self.currentState[2]
        if sum>0 and sum<=8 and self.currentState[0]>=0 and self.currentState[2]>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=0
            self.currentState[1]=sum
            self.currentState[2]=0
            print("transferAllToSecondJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def transferAllToThird(self):
        sum=self.currentState[0]+self.currentState[1]+self.currentState[2]
        if sum>0 and sum<=5 and self.currentState[0]>=0 and self.currentState[1]>=0:
            self.prevState=copy.deepcopy(self)
            self.currentState[0]=0
            self.currentState[1]=0
            self.currentState[2]=sum
            print("transferAllToThirdJug")
            return True
        else:
            #print("Cannot transfer")
            return False

    def displayState(self):
        print("------------------------------------------")
        print(self.currentState)

    def isGoalReached(self):
        if self.currentState[0]==self.goalState and self.currentState[1]==self.goalState:
            return True
        else:
            return False

    def _eq_(self, other):
        return self.currentState==other.currentState

    def possibleNextStates(self):
        stateList=[]
        
        B2A_transferToFillFirstJug_state=copy.deepcopy(self)
        if B2A_transferToFillFirstJug_state.B2A_transferToFillFirst():
            stateList.append(B2A_transferToFillFirstJug_state)

        C2A_transferToFillFirstJug_state=copy.deepcopy(self)
        if C2A_transferToFillFirstJug_state.C2A_transferToFillFirst():
            stateList.append(C2A_transferToFillFirstJug_state)

        A2B_transferToFillSecondJug_state=copy.deepcopy(self)
        if A2B_transferToFillSecondJug_state.A2B_transferToFillSecond():
            stateList.append(A2B_transferToFillSecondJug_state)

        C2B_transferToFillSecondJug_state=copy.deepcopy(self)
        if C2B_transferToFillSecondJug_state.C2B_transferToFillSecond():
            stateList.append(C2B_transferToFillSecondJug_state)

        A2C_transferToFillThirdJug_state=copy.deepcopy(self)
        if A2C_transferToFillThirdJug_state.A2C_transferToFillThird():
            stateList.append(A2C_transferToFillThirdJug_state)

        B2C_transferToFillThirdJug_state=copy.deepcopy(self)
        if B2C_transferToFillThirdJug_state.B2C_transferToFillThird():
            stateList.append(B2C_transferToFillThirdJug_state)
            
        for d in range (0, 13):
            B2A_transferSomeToFillFirstJug_state=copy.deepcopy(self)
            if B2A_transferSomeToFillFirstJug_state.B2A_transferSomeToFirst(d):
                stateList.append(B2A_transferSomeToFillFirstJug_state)
            
            C2A_transferSomeToFillFirstJug_state=copy.deepcopy(self)
            if C2A_transferSomeToFillFirstJug_state.C2A_transferSomeToFirst(d):
                stateList.append(C2A_transferSomeToFillFirstJug_state)

            A2B_transferSomeToFillFirstJug_state=copy.deepcopy(self)
            if A2B_transferSomeToFillFirstJug_state.A2B_transferSomeToSecond(d):
                stateList.append(A2B_transferSomeToFillFirstJug_state)

            C2B_transferSomeToFillFirstJug_state=copy.deepcopy(self)
            if C2B_transferSomeToFillFirstJug_state.C2B_transferSomeToSecond(d):
                stateList.append(C2B_transferSomeToFillFirstJug_state)

            A2C_transferSomeToFillFirstJug_state=copy.deepcopy(self)
            if A2C_transferSomeToFillFirstJug_state.A2C_transferSomeToThird(d):
                stateList.append(A2C_transferSomeToFillFirstJug_state)
        
            B2C_transferSomeToFillFirstJug_state=copy.deepcopy(self)
            if B2C_transferSomeToFillFirstJug_state.B2C_transferSomeToThird(d):
                stateList.append(B2C_transferSomeToFillFirstJug_state)

        transferAllToFirstJug_state=copy.deepcopy(self)
        if transferAllToFirstJug_state.transferAllToFirst():
            stateList.append(transferAllToFirstJug_state)

        transferAllToSecondJug_state=copy.deepcopy(self)
        if transferAllToSecondJug_state.transferAllToSecond():
            stateList.append(transferAllToSecondJug_state)

        transferAllToThirdJug_state=copy.deepcopy(self)
        if transferAllToThirdJug_state.transferAllToThird():
            stateList.append(transferAllToThirdJug_state)

        return stateList

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

def BFS(startState):
    open=[]
    closed=[]
    open.append(startState)
    while open:
        print(len(open), len(closed))
        thisState=open.pop(0)
        #pop(0) -- queue for bfs
        #pop    -- stack for dfs
        thisState.displayState()
        if thisState not in closed:
            closed.append(thisState)
            if thisState.isGoalReached():
                print("Goal state found.. stopping search")
                constructPath(thisState)
                break
            nextStates=thisState.possibleNextStates()
            for eachState in nextStates:
                if eachState not in closed and eachState not in open:
                    open.append(eachState)

                    
start=[12, 0, 0]
goal=6

problem=MyWaterJug(start, goal)
BFS(problem)
```
#
Q3 8PuzzleProblem.py
```
import copy

class MyEightPuzzle:
    def __init__(self, startState, goalState):
        self.currentState=startState
        self.goalState=goalState
        self.emptyIndex=self.emptyTileIndex()
        self.prevState=None

    def up(self):
        if self.emptyIndex==6 or self.emptyIndex==7 or self.emptyIndex==8:
            #print("Cannot move")
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex+3]
            self.currentState[self.emptyIndex+3]=0
            self.emptyIndex=self.emptyIndex+3
            #print("Action : UP")
            return True

    def down(self):
        if self.emptyIndex==0 or self.emptyIndex==1 or self.emptyIndex==2:
            #print("Cannot move")
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex-3]
            self.currentState[self.emptyIndex-3]=0
            self.emptyIndex=self.emptyIndex-3
            #print("Action : DOWN")
            return True
            
    def left(self):
        if self.emptyIndex==2 or self.emptyIndex==5 or self.emptyIndex==8:
            #print("Cannot move")
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex+1]
            self.currentState[self.emptyIndex+1]=0
            self.emptyIndex=self.emptyIndex+1
            #print("Action : LEFT")
            return True

    def right(self):
        if self.emptyIndex==0 or self.emptyIndex==3 or self.emptyIndex==6:
            #print("Cannot move")
            return False
        else:
            self.prevState=copy.deepcopy(self)
            self.currentState[self.emptyIndex]=self.currentState[self.emptyIndex-1]
            self.currentState[self.emptyIndex-1]=0
            self.emptyIndex=self.emptyIndex-1
            #print("Action : RIGHT")
            return True

    def displayState(self):
        print("-------------------------------------")
        for i in range(0, 8, 3):
            print(self.currentState[i], self.currentState[i+1], self.currentState[i+2])
        
    def emptyTileIndex(self):
        for i in range(0, 9):
            if self.currentState[i]==0:
                return i
    
    def isGoalReached(self):
        if self.currentState==self.goalState:
            return True
        else:
            return False

    def _eq_(self, other):
        return self.currentState==other.currentState

    def possibleNextStates(self):
        stateList=[]
        
        up_state=copy.deepcopy(self)
        if up_state.up():
            stateList.append(up_state)

        down_state=copy.deepcopy(self)
        if down_state.down():
            stateList.append(down_state)
            
        left_state=copy.deepcopy(self)
        if left_state.left():
            stateList.append(left_state)

        right_state=copy.deepcopy(self)
        if right_state.right():
            stateList.append(right_state)

        return stateList

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

def BFS(startState):
    open=[]
    closed=[]
    open.append(startState)
    while open:
        print(len(open), len(closed))
        thisState=open.pop(0)
        #pop(0) -- queue for bfs
        #pop    -- stack for dfs
        thisState.displayState()
        if thisState not in closed:
            closed.append(thisState)
            if thisState.isGoalReached():
                print("Goal state found.. stopping search")
                constructPath(thisState)
                break
            nextStates=thisState.possibleNextStates()
            for eachState in nextStates:
                if eachState not in closed and eachState not in open:
                    open.append(eachState)



#start=[7, 2, 4, 5, 0, 6, 8, 3, 1]
#goal=[0, 1, 2, 3, 4, 5, 6, 7, 8]


start=  [2, 8, 1, 0, 4, 3, 7, 6, 5]
goal=   [1, 2, 3, 8, 0, 4, 7, 6, 5]
problem=MyEightPuzzle(start, goal)
BFS(problem)
```
#
Q4 TSPProblem.py
```
import copy
class TSP:
    def __init__(self, map, startCity):
        TSP.map=map
        self.startCity=startCity
        self.currentCity=startCity
        self.cost=0
        self.visitedList=[]
        self.visitedList.append(self.currentCity)
        self.prevState=None

    def displayState(self):
        print("--------------------------------")
        print(f"Current city:{self.currentCity}     Visited cities={self.visitedList}     Cost={self.cost}")

    def __gt__(self, other):
        return self.cost>other.cost

    def __lt__(self, other):
        return self.cost<other.cost

    def __eq__(self, other):
        return self.visitedList==other.visitedList

    def isGoalReached(self):
        if len(TSP.map[0])+1==len(self.visitedList):
            return True
        else:
            return False

    def move(self, city):
        if city!=self.currentCity and city not in self.visitedList:
            print(f"Moving from city {self.currentCity} to {city}")
            self.cost+=TSP.map[self.currentCity][city]
            self.currentCity=city
            self.visitedList.append(self.currentCity)
            return True
        elif len(self.visitedList)==len(TSP.map[0]):
            print(f"Moving from city {self.currentCity} to {self.startCity}")
            self.cost+=TSP.map[self.currentCity][self.startCity]
            self.currentCity=self.startCity
            self.visitedList.append(self.startCity)
            return True
        else:
            print("Already visited")
            return False

    def possibleNextStates(self):
        stateList=[]
        for i in range(0, len(TSP.map[0])):
            state=copy.deepcopy(self)
            self.prevState=copy.deepcopy(self)
            if state.move(i):
                stateList.append(state)
        return stateList

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

open=[]
closed=[]
def UCS(state):
    open.append(state)
    while(open):
        thisState=open.pop(0)
        thisState.displayState()
        if thisState not in closed:
            closed.append(thisState)
            if thisState.isGoalReached():
                print("Goal state found.. stopping search")
                constructPath(thisState)
                break   
            else:
                nextStates=thisState.possibleNextStates()
                for eachState in nextStates:
                    if eachState not in open and eachState not in closed:
                        open.append(eachState)
                        open.sort()
                    elif eachState in open:
                        index=open.index(eachState)
                        if open[index].cost>eachState.cost:
                            open.pop(index)
                            open.append(eachState)
                            open.sort()
                    elif eachState in closed:
                        index=closed.index(eachState)
                        if closed[index].cost>eachState.cost:
                            closed.pop(index)
                            closed.append(eachState)
                            propogateImprovement(eachState)

def propogateImprovement(state):
    nextStates=state.possibleNextStates()
    for eachState in nextStates:
        if eachState in open:
            index=open.index[eachState]
            if open[index].cost>eachState.cost:
                open.pop(index)
                open.append(eachState)
                open.sort()
            if eachState in closed:
                index=closed.index(eachState)
                if closed[index].cost>eachState.cost:
                    closed.pop(index)
                    closed.append(eachState)
                    propogateImprovement(eachState)

map=[[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
start=int(input("Enter the start city "))
problem=TSP(map, start)
UCS(problem)
```
