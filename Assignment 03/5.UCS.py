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
