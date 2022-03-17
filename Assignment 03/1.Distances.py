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