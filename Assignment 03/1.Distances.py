from cmath import sqrt

class Heuristic:
    def __init__(self, start, goal):
        self.startState=start
        self.goalState=goal

    def Euclidean(self):
        sum=0
        for i in range(0, 9):
            if self.goalState[i]!=0:
                goalBlockX=int(i/3)
                goalBlockY=i%3     

                for j in range(0, 9):
                    if self.goalState[i]==self.startState[j]:
                        startBlockX=int(j/3)
                        startBlockY=j%3
                        break
                distance=sqrt( pow(goalBlockX-startBlockX, 2) + pow(goalBlockY-startBlockY, 2) )
                print(f"Euclidean distance for {self.goalState[i]} is {distance}")
                sum+=distance
        
        print(f"Heuristic function value for Euclidean distance={sum}")

    def Manhattan(self):
        sum=0

        for i in range(0, 9):
            if self.goalState[i]!=0:
                goalBlockIndex=i
                for j in range(0, 9):
                    if self.goalState[i]==self.startState[j]:
                        startBlockIndex=j
                        break
                
                difference=abs(goalBlockIndex-startBlockIndex)
                if difference in [0, 1, 2]:
                    moves=difference
                elif difference in [3, 4, 5]:
                    moves=difference%3+1
                elif difference in [6, 7, 8]:
                    moves=difference%3+2
                
                sum+=moves
                print(f"Manhattan distance for {self.goalState[i]} is {moves}")
        print(f"Heuristic function value for Manhattan distance={sum}")

    def Minkowski(self):
        p=float(input("Enter value of p: "))
        sum=0

        for i in range(0, 9):
            if self.goalState[i]!=0:
                goalBlockX=int(i/3)
                goalBlockY=i%3     

                for j in range(0, 9):
                    if self.goalState[i]==self.startState[j]:
                        startBlockX=int(j/3)
                        startBlockY=j%3
                        break
                distance=pow( pow(goalBlockX-startBlockX, p) + pow(goalBlockY-startBlockY, p) , 1/p)
                print(f"Minkowski distance for {self.goalState[i]} is {distance}")
                sum+=distance
        
        print(f"Heuristic function value for Minkowski distance={sum}")
                

start=[2, 0, 3, 1, 8, 4, 7, 6, 5]
goal= [1, 2, 3, 8, 0, 4, 7, 6, 5]
problem=Heuristic(start, goal)
problem.Euclidean()
problem.Manhattan()
problem.Minkowski()
