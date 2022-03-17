[Lab Assignment 03.pdf](https://github.com/AhmedKamruddin/UCS411-Artificial-Intelligence/files/8288216/Lab.Assignment.03.pdf)
Q1 Distances.py
```
from cmath import sqrt

class MyEightPuzzle:
    def __init__(self, startState, goalState, startState2D, goalState2D):
        self.startState=startState
        self.goalState=goalState
        self.startState2D=startState2D
        self.goalState2D=goalState2D

    def euclidean(self):
        sum=0
        for i in range(0, 3):
            for j in range(0, 3):
                goalNode=self.goalState2D[i][j]
                if goalNode==0:
                    continue
                goalIndexX=i
                goalIndexY=j

                for k in range(0, 3):
                    for l in range(0, 3):
                        startNode=self.startState2D[k][l]
                        if startNode==goalNode:
                            startIndexX=k
                            startIndexY=l
                            break
                
                x=abs(goalIndexX-startIndexX)
                y=abs(goalIndexY-startIndexY)
                distance=sqrt( pow(x, 2) + pow(y, 2) )
                sum+=distance
                print(f"Euclidean distance for {goalNode} is {distance}")
        print(f"Heuristic function value for Euclidean distance={sum}")
        
    def manhattan(self):
        sum=0
        for i in range(0, 9):
            
            goalNode=self.goalState[i]
            if goalNode==0:
                continue
            goalIndex=i

            for j in range(0, 9):
                startNode=self.startState[j]
                if startNode==goalNode:
                    startIndex=j
                    break
            
            difference=abs(goalIndex-startIndex)
            if difference<3:
                moves=difference
            elif difference>=3 and difference<6:
                moves=difference%3 + 1
            elif difference>=6 and difference<8:
                moves=difference%3 + 2
            sum+=moves
            print(f"Manhattan distance for {self.goalState[i]} is {moves}")
        print(f"Heuristic function value for Manhattan distance={sum}")
            
    def minkowski(self):
        sum=0
        p=float(input("Enter p: "))

        for i in range(0, 3):
            for j in range(0, 3):
                goalNode=self.goalState2D[i][j]
                if goalNode==0:
                    continue
                goalIndexX=i
                goalIndexY=j

                for k in range(0, 3):
                    for l in range(0, 3):
                        startNode=self.startState2D[k][l]
                        if startNode==goalNode:
                            startIndexX=k
                            startIndexY=l
                            break
                
                x=abs(goalIndexX-startIndexX)
                y=abs(goalIndexY-startIndexY)
                distance=pow( pow(x, p) + pow(y, p), 1/p )
                sum+=distance
                print(f"Minkowski distance for {goalNode} is {distance}")
        print(f"Heuristic function value for Minkowski distance={sum}")
        

start=[2, 0, 3, 1, 8, 4, 7, 6, 5]
goal= [1, 2, 3, 8, 0, 4, 7, 6, 5]
start2D=[[2, 0, 3], [1, 8, 4], [7, 6, 5]]
goal2D= [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
problem=MyEightPuzzle(start, goal, start2D, goal2D)

problem.euclidean()
problem.manhattan()
problem.minkowski()
```
#
Q2 BestFirstSearch.py
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

def heuristic(self):
    count=0
    for i in range(0, 9):
        if self.goalState[i]!=self.currentState[i] and self.goalState[i]!=0:
            count=count+1
    return count

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

def BestFirstSearch(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)

    #Step 2
    while open:

        #Step 3
        thisState=open.pop(0)
        thisState.displayState()
        closed.append(thisState)

        #Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            constructPath(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                open.append(eachState)
                open.sort(key=heuristic)


start=[2, 0, 3, 1, 8, 4, 7, 6, 5]
goal= [1, 2, 3, 8, 0, 4, 7, 6, 5]
problem=MyEightPuzzle(start, goal)
BestFirstSearch(problem)
```
# 
Q3 HillClimbing.py
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

    def heuristic(self):
        count=0
        for i in range(0, 9):
            if self.goalState[i]!=self.currentState[i] and self.goalState[i]!=0:
                count=count+1
        return count

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

def HillClimbing(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)

    #Step 2
    while open:

        #
        thisState=open.pop(0)
        thisState.displayState()

        #Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            constructPath(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                #If next state is better than current state(lower heuristic value is better)
                if eachState.heuristic() < thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)

start=[2, 0, 3, 1, 8, 4, 7, 6, 5]
goal= [1, 2, 3, 8, 0, 4, 7, 6, 5]
problem=MyEightPuzzle(start, goal)
HillClimbing(problem)
```
#
Q4
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

def heuristic(self):
    sum=0
    for i in range(0, 9):
        
        goalNode=self.goalState[i]
        if goalNode==0:
            continue
        goalIndex=i

        for j in range(0, 9):
            currentNode=self.currentState[j]
            if currentNode==goalNode:
                currentIndex=j
                break
        
        difference=abs(goalIndex-currentIndex)
        if difference<3:
            moves=difference
        elif difference>=3 and difference<6:
            moves=difference%3 + 1
        elif difference>=6 and difference<8:
            moves=difference%3 + 2

        sum=sum+moves
        return sum

def constructPath(goalState):
    print("The solution path from Goal to Start")
    while goalState is not None:
        goalState.displayState()
        goalState=goalState.prevState

def BestFirstSearch(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)

    #Step 2
    while open:

        #Step 3
        thisState=open.pop(0)
        thisState.displayState()
        closed.append(thisState)

        #Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            constructPath(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                open.append(eachState)
                open.sort(key=heuristic)


start=[2, 0, 3, 1, 8, 4, 7, 6, 5]
goal= [1, 2, 3, 8, 0, 4, 7, 6, 5]
problem=MyEightPuzzle(start, goal)
BestFirstSearch(problem)
```
#
Q5 UCS.py
```
import copy

class MyShortestPath:
    def __init__(self, map, startCity, goalCity):
        MyShortestPath.map=map
        self.currentCity=startCity
        self.goalCity=goalCity
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
        if self.goalCity in self.visitedList:
            return True
        else:
            return False
            
    def move(self, city):
        if city!=self.currentCity and city not in self.visitedList and MyShortestPath.map[self.currentCity][city]!=0:
            print(f"Moving from city {self.currentCity} to {city}")
            self.cost+=MyShortestPath.map[self.currentCity][city]
            self.currentCity=city
            self.visitedList.append(self.currentCity)
            return True
        else:
            print("Already visited")
            return False

    def possibleNextStates(self):
        stateList=[]
        for i in range(0, len(MyShortestPath.map[0])):
            state=copy.deepcopy(self)
            if state.move(i):
                self.prevState=copy.deepcopy(self)
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

map=[[0, 1, 5, 15, 0], [1, 0, 0, 0, 10], [5, 0, 0, 0, 5], [15, 0, 0, 0, 5], [0, 10, 5, 5, 0]]
start=0
goal=4
problem=MyShortestPath(map, start, goal)
UCS(problem)
```
