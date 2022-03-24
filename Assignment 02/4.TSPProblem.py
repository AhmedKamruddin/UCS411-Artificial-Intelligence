import copy

class TSP():
    def __init__(self, map, startCity):
        TSP.map=map
        self.startCity=startCity
        self.currentCity=startCity
        self.visitedList=[]
        self.visitedList.append(self.currentCity)
        self.cost=0
        self.prevState=None

    def displayState(self):
        print(f"Current city={self.currentCity} Visited cities={self.visitedList} Cost={self.cost}")
        print("********************************")

    def isGoalReached(self):
        if len(self.visitedList)==len(TSP.map[0])+1:
            return True
        else:
            return False

    def __gt__(self, other):
        return self.cost>other.cost

    def __lt__(self, other):
        return self.cost<other.cost

    def move(self, city):
        if TSP.map[self.currentCity][city]!=0 and city not in self.visitedList:
            print(f"Moving from city {self.currentCity} to {city}.")
            self.prevState=copy.deepcopy(self)
            self.cost=self.cost+TSP.map[self.currentCity][city]
            self.currentCity=city
            self.visitedList.append(self.currentCity)
            return True
        elif len(self.visitedList)==len(TSP.map[0]) and TSP.map[self.currentCity][city]!=0:
            print(f"Moving from city {self.currentCity} to {city}.")
            self.prevState=copy.deepcopy(self)
            self.cost=self.cost+TSP.map[self.currentCity][city]
            self.currentCity=city
            self.visitedList.append(self.currentCity)
            return True
        else:
            return False
    
    def possibleNextStates(self):
        stateList=[]

        for i in range(0, len(TSP.map[0])):
            stateCopy=copy.deepcopy(self)
            if stateCopy.move(i):
                stateList.append(stateCopy)
        
        return stateList

def constructGoalPath(goalState):
    print("Displaying path from goal to start")
    while goalState:
        goalState.displayState()
        goalState=goalState.prevState

open=[]
closed=[]
def UCS(startState):
    open.append(startState)

    while open:
        thisState=open.pop(0)
        thisState.displayState()

        closed.append(thisState)

        if thisState.isGoalReached():
            print("Goal found..")
            constructGoalPath(thisState)
            break
        else:
            nextStates=thisState.possibleNextStates()
            for eachState in nextStates:
                
                #Case 1
                if eachState not in open and eachState not in closed:
                    open.append(eachState)
                    open.sort()

                #Case 2
                elif eachState in open:
                    index=open.index(eachState)
                    if eachState<open[index]:
                        open.append(eachState)
                        open.sort()

                #Case 3
                elif eachState in closed:
                    index=closed.index(eachState)
                    if eachState<closed[index]:
                        closed.append(eachState)
                        closed.sort()
                        propogateImprovement(eachState)

def propogateImprovement(thisState):
    nextStates=thisState.nextPossibleStates()
    for eachState in nextStates:
        if eachState in open:
            index=open.index(eachState)
            if eachState<open[index]:
                open.append(eachState)
                open.sort()
        
        if eachState in closed:
            index=closed.index(eachState)
            if eachState<closed[index]:
                closed.append(eachState)
                closed.sort()
                propogateImprovement(eachState)

    
map=[[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
startCity=0
problem=TSP(map, startCity)
UCS(problem)
