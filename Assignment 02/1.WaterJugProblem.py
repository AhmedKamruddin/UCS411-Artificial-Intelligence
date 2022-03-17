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