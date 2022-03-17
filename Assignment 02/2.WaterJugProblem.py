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