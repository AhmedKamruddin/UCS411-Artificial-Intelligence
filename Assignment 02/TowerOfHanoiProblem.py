from tracemalloc import start


class MyTowerOfHanoi:
    def __init__(self, startState, goalState):
        self.currentState=startState
        self.goalState=goalState

    def a2b(self):
        for i in range (2, -1, -1):
            buf=self.currentState[0][i]
            if buf!=0:
                break
            if i==0:
                print("Not present")
                return
    
        for j in range (0,3):
            if self.currentState[1][j]>buf:
                print("Cannot move")
                return

            if self.currentState[1][j]==0:
                self.currentState[1][j]=buf
                self.currentState[0][i]=0
                break

    def a2c(self):
        for i in range (2, -1, -1):
            buf=self.currentState[0][i]
            if buf!=0:
                break
            if i==0:
                print("Not present")
                return
    
        for j in range (0,3):
            if self.currentState[2][j]>buf:
                print("Cannot move")
                return
                
            if self.currentState[2][j]==0:
                self.currentState[2][j]=buf
                self.currentState[0][i]=0
                break
            
    def b2a(self):
        for i in range (2, -1, -1):
            buf=self.currentState[1][i]
            if buf!=0:
                break
            if i==0:
                print("Not present")
                return
    
        for j in range (0,3):
            if self.currentState[0][j]>buf:
                print("Cannot move")
                return

            if self.currentState[0][j]==0:
                self.currentState[0][j]=buf
                self.currentState[1][i]=0
                break
    
    def b2c(self):
        for i in range (2, -1, -1):
            buf=self.currentState[1][i]
            if buf!=0:
                break
            if i==0:
                print("Not present")
                return
    
        for j in range (0,3):
            if self.currentState[2][j]>buf:
                print("Cannot move")
                return

            if self.currentState[2][j]==0:
                self.currentState[2][j]=buf
                self.currentState[1][i]=0
                break


    def c2a(self):
        for i in range (2, -1, -1):
            buf=self.currentState[2][i]
            if buf!=0:
                break
            if i==0:
                print("Not present")
                return
    
        for j in range (0,3):
            if self.currentState[0][j]>buf:
                print("Cannot move")
                return

            if self.currentState[0][j]==0:
                self.currentState[0][j]=buf
                self.currentState[2][i]=0
                break

    def c2b(self):
        for i in range (2, -1, -1):
            buf=self.currentState[2][i]
            if buf!=0:
                break
            if i==0:
                print("Not present")
                return
    
        for j in range (0,3):
            if self.currentState[1][j]>buf:
                print("Cannot move")
                return

            if self.currentState[1][j]==0:
                self.currentState[1][j]=buf
                self.currentState[2][i]=0
                break
            
    def displayState(self):
        print("-------------------------------------")
        print(self.currentState)

    def isGoalReached(self):
        if self.currentState==self.goalState:
            return True
        else:
            return False

start=[[1,2,3], [0,0,0], [0,0,0]]
goal=[[0,0,0], [0,0,0], [1,2,3]]
problem=MyTowerOfHanoi(start, goal)
problem.displayState()
problem.a2b()
problem.displayState()
problem.a2c()
problem.displayState()
problem.c2b()
problem.displayState()
problem.a2b()
problem.displayState()