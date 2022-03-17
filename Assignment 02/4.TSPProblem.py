import copy
class TSP:
    def __init__(self, map, startCity):
        TSP.map=map
        self.startCity=startCity
        self.currentCity=startCity
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
        if len(TSP.map[0])+1==len(self.visitedList):
            return True
        else:
            return False

    def move(self, city):
        if city!=self.currentCity and city not in self.visitedList:
            print(f"Moving from city {self.currentCity} to {city}")
            self.cost+=TSP.map[self.currentCity][city]
            self.currentCity=city
            self.visitedList.append(self.currentCity)
            return True
        elif len(self.visitedList)==len(TSP.map[0]):
            print(f"Moving from city {self.currentCity} to {self.startCity}")
            self.cost+=TSP.map[self.currentCity][self.startCity]
            self.currentCity=self.startCity
            self.visitedList.append(self.startCity)
            return True
        else:
            print("Already visited")
            return False

    def possibleNextStates(self):
        stateList=[]
        for i in range(0, len(TSP.map[0])):
            state=copy.deepcopy(self)
            self.prevState=copy.deepcopy(self)
            if state.move(i):
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

map=[[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
start=int(input("Enter the start city "))
problem=TSP(map, start)
UCS(problem)
        


        