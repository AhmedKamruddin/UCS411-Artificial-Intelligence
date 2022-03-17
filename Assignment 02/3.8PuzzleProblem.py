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