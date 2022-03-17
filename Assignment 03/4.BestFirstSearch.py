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