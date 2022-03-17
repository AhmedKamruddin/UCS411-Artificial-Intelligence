[Lab Assignment 04.pdf](https://github.com/AhmedKamruddin/UCS411-Artificial-Intelligence/files/8288253/Lab.Assignment.04.pdf)

Q1 HillClimbing.py
```
import copy

class MyBlockProblem:
    def __init__(self, start, goal):
        self.currentState=start
        self.goalState=goal
        self.prevState=None

    def isGoalReached(self):
        #print("In isGoalReached()")
        for i in range(0, 4):
            #print("Printing self.currentState[i]")
            #print(self.currentState[i])
            if self.currentState[i]==goal:
                return True
        
        return False

    def displayState(self):
        for i in range(0, 4):
            if self.currentState[i]!=[]:
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("------------------")
        print("******************************************")

    def _eq_(self, other):
        return self.currentState==other.currentState

    def movefromStackXtoStackY(self, x, y):
        if self.currentState[x]!=[] and len(self.currentState[y])!=4:
            self.prevState=copy.deepcopy(self)
            block=self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):
        #print("Over here")
        stateList=[]
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state=copy.deepcopy(self)
                if i!=j and copy_state.movefromStackXtoStackY(i, j):
                    #copy_state.displayState()
                    stateList.append(copy_state)
                    #print("Appending to stateList ")
                    
        return stateList

    def heuristic(self):
        value=0

        for i in range(0, 4):
            if self.currentState[i]!=[]:
                if self.currentState[i][0]==self.goalState[0]:
                    value+=1
                    #print("First block +1")
                else:
                    #print("First block -1")
                    value-=1

        
        for i in range(0, 4):
            goalBlock=self.goalState[i]
            goalBlockIndex=i
            for j in range(0, 4):
                flag=0
                for k in range(0, len(self.currentState[j])):
                    if self.currentState[j]!=[]: 
                        if self.currentState[j][k]==goalBlock:
                            currentBlockIndexX=j
                            currentBlockIndexY=k
                            flag=1
                            break
                if flag==1:
                    flag=0
                    break
            
            if self.currentState[currentBlockIndexX][currentBlockIndexY-1]==self.goalState[goalBlockIndex-1] and currentBlockIndexY!=0 and goalBlockIndex!=0:
                #print(f"{self.currentState[currentBlockIndexX][currentBlockIndexY]} rests on {self.goalState[goalBlockIndex-1]}")
                value+=1
            else:
                if currentBlockIndexY!=0:
                    #print(f"{self.currentState[currentBlockIndexX][currentBlockIndexY]} shouldn't rest on {self.currentState[currentBlockIndexX][currentBlockIndexY-1]}") 
                    value-=1
                
        return value

def constructPath(goalState):
    print("Displaying path from start to goal")
    while goalState:
        goalState.displayState()
        goalState=goalState.prevState
    
    return 1

def HillClimbing(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)


    #Step 2
    returnVal=0
    while open:

        #
        thisState=open.pop(0)
        #print("Printing thisState")
        thisState.displayState()

        #Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            returnVal=constructPath(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                #If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)
                    
    
    if returnVal!=1:
        print("Error: Local Maxima")

                
start=[[2, 3, 4, 1], [], [], []]
goal=[1, 2, 3, 4]
problem=MyBlockProblem(start, goal)
#print(problem.heuristic())
HillClimbing(problem)
```
#
Q2 HillClimbing.py
```
import copy

class MyBlockProblem:
    def __init__(self, start, goal):
        self.currentState=start
        self.goalState=goal
        self.prevState=None

    def isGoalReached(self):
        #print("In isGoalReached()")
        for i in range(0, 4):
            #print("Printing self.currentState[i]")
            #print(self.currentState[i])
            if self.currentState[i]==goal:
                return True
        
        return False

    def displayState(self):
        for i in range(0, 4):
            if self.currentState[i]!=[]:
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("------------------")
        print("******************************************")

    def _eq_(self, other):
        return self.currentState==other.currentState

    def movefromStackXtoStackY(self, x, y):
        if self.currentState[x]!=[] and len(self.currentState[y])!=4:
            self.prevState=copy.deepcopy(self)
            block=self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):
        #print("Over here")
        stateList=[]
        for i in range(0, 4):
            for j in range(0, 4):
                copy_state=copy.deepcopy(self)
                if i!=j and copy_state.movefromStackXtoStackY(i, j):
                    #copy_state.displayState()
                    stateList.append(copy_state)
                    #print("Appending to stateList ")
                    
        return stateList

    def heuristic(self):
        value=0

        for i in range(0, 4):
            goalBlock=self.goalState[i]
            goalBlockIndex=i

            for j in range(0, 4):
                flag=0
                if self.currentState[j]!=[]:
                    for k in range(0, len(self.currentState[j])):
                        if self.currentState[j][k]==goalBlock:
                            currentBlockIndexX=j
                            currentBlockIndexY=k
                            flag=1
                            break

                if flag==1:
                    flag=0
                    break
            
            if currentBlockIndexY!=goalBlockIndex:
                #print(f"-{currentBlockIndexY}({self.currentState[currentBlockIndexX][currentBlockIndexY]})")
                value-=currentBlockIndexY
            else:
                #print(f"+{currentBlockIndexY}({self.currentState[currentBlockIndexX][currentBlockIndexY]})")  
                #print(f"{value}={value}+{currentBlockIndexY}")
                value+=currentBlockIndexY


                
        return value

def constructPath(goalState):
    print("Displaying path from start to goal")
    while goalState:
        goalState.displayState()
        goalState=goalState.prevState
    
    return 1

def HillClimbing(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)


    #Step 2
    returnVal=0
    while open:

        #
        thisState=open.pop(0)
        #print("Printing thisState")
        thisState.displayState()

        #Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            returnVal=constructPath(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                #If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)
    
    if returnVal!=1:
        print("Error: Local Maxima")

                
start=[[2, 3, 4, 1], [], [], []]
goal=[1, 2, 3, 4]
problem=MyBlockProblem(start, goal)
#print(problem.heuristic())
HillClimbing(problem)
```
# 
Q3 SteepestHillClimbing.py
```
import copy

class MyBlockProblem:
    def __init__(self, start, goal):
        self.currentState=start
        self.goalState=goal
        self.prevState=None

    def isGoalReached(self):
        #print("In isGoalReached()")
        for i in range(0, 3):
            #print("Printing self.currentState[i]")
            #print(self.currentState[i])
            if self.currentState[i]==goal:
                return True
        
        return False

    def displayState(self):
        for i in range(0, 3):
            if self.currentState[i]!=[]:
                print(f"Stack {i}:")
                print(self.currentState[i])
                print("------------------")
        print("******************************************")

    def __gt__(self, other):
        return self.heuristic()>other.heuristic()

    def __lt__(self, other):
        return self.heuristic()<other.heuristic()

    def _eq_(self, other):
        return self.currentState==other.currentState

    def movefromStackXtoStackY(self, x, y):
        if self.currentState[x]!=[] and len(self.currentState[y])!=3:
            self.prevState=copy.deepcopy(self)
            block=self.currentState[x].pop()
            self.currentState[y].append(block)
            return True
        else:
            return False

    def possibleNextStates(self):
        #print("Over here")
        stateList=[]
        for i in range(0, 3):
            for j in range(0, 3):
                copy_state=copy.deepcopy(self)
                if i!=j and copy_state.movefromStackXtoStackY(i, j):
                    #copy_state.displayState()
                    stateList.append(copy_state)
                    #print("Appending to stateList ")
                    
        return stateList

    def heuristic(self):
        value=0

        for i in range(0, 3):
            goalBlock=self.goalState[i]
            goalBlockIndex=i

            for j in range(0, 3):
                flag=0
                if self.currentState[j]!=[]:
                    for k in range(0, len(self.currentState[j])):
                        if self.currentState[j][k]==goalBlock:
                            currentBlockIndexX=j
                            currentBlockIndexY=k
                            flag=1
                            break

                if flag==1:
                    flag=0
                    break
            
            if currentBlockIndexY!=goalBlockIndex:
                #print(f"-{currentBlockIndexY}({self.currentState[currentBlockIndexX][currentBlockIndexY]})")
                value-=currentBlockIndexY
            else:
                #print(f"+{currentBlockIndexY}({self.currentState[currentBlockIndexX][currentBlockIndexY]})")  
                #print(f"{value}={value}+{currentBlockIndexY}")
                value+=currentBlockIndexY


                
        return value

def constructPath(goalState):
    print("Displaying path from start to goal")
    while goalState:
        goalState.displayState()
        goalState=goalState.prevState
    
    return 1

def SteepestHillClimbing(startState):
    open=[]
    closed=[]
    
    #Step 1
    open.append(startState)


    #Step 2
    returnVal=0
    while open:

        #
        thisState=open.pop(0)
        #print("Printing thisState")
        thisState.displayState()

        #Step 4
        if thisState.isGoalReached():
            print("Goal state found.. stopping search")
            returnVal=constructPath(thisState)
            break

        #Step 5
        nextStates=thisState.possibleNextStates()

        #Step 6
        for eachState in nextStates:
            if eachState not in open and eachState not in closed:
                #If next state is better than current state(higher heuristic value is better)
                if eachState.heuristic() > thisState.heuristic():
                    open.append(eachState)
                    closed.append(thisState)
        
        #Step 7
        #Sort in descending order
        open.sort(reverse=True)
    
    if returnVal!=1:
        print("Error: Local Maxima")

                
start=[[3, 1], [2], []]
goal=[1, 2, 3]
problem=MyBlockProblem(start, goal)
#print(problem.heuristic())
SteepestHillClimbing(problem)
```
#
Q4 BeamSearch.py
```
import copy
class MyGraphProblem:
     def __init__(self, map):
          MyGraphProblem.map=map
          self.currentNode=0
          self.goalNode=6
          self.heuristic=0
          self.visitedList=[]
          self.visitedList.append(self.currentNode)
          self.prevState=None

     def displayState(self):
          print("--------------------------------")
          print(f"Current node:{self.currentNode}     Visited nodes={self.visitedList}")

     def __gt__(self, other):
          return self.heuristic>other.heuristic

     def __lt__(self, other):
          return self.heuristic<other.heuristic

     def __eq__(self, other):
          return self.visitedList==other.visitedList

     def isGoalReached(self):
          if self.goalNode in self.visitedList:
               return True
          else:
               return False

     def move(self, node):
          if node!=self.currentNode and node not in self.visitedList and MyGraphProblem.map[self.currentNode][node]!=-1:
               print(f"Moving from node {self.currentNode} to {node}")
               self.heuristic=MyGraphProblem.map[self.currentNode][node]
               self.currentNode=node
               self.visitedList.append(self.currentNode)
               return True
          else:
               #print("Already visited")
               return False

     def possibleNextStates(self):
          stateList=[]
          for i in range(0, len(MyGraphProblem.map[0])):
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

def BeamSearch(startState, beta):
     open=[]
     closed=[]
     flag=0
     B=beta

     open.append(startState)
     
     while(open):

          thisState=open.pop(0)
          thisState.displayState()

          if thisState not in closed:
               closed.append(thisState)

               if thisState.isGoalReached():
                    print("Goal state found.. stopping search")
                    constructPath(thisState)
                    flag=1
                    break

               nextStates=thisState.possibleNextStates()
               for eachState in nextStates:
                    open.append(eachState)
               
               open.sort()

               if len(open)>B:
                    while len(open)!=B:
                         open.pop()

     if flag!=1:
          print("Error, can't reach goal node")

map=[[-1,  1,  3, -1, -1, -1, -1], [-1, -1, -1,  2,  2, -1, -1],[-1, -1, -1, -1, -1,  3,  0], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1]]
beta=int(input("Enter B (2/3): "))
problem=MyGraphProblem(map)
BeamSearch(problem, beta)
```
