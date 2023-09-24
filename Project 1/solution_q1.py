#create node system that saves each state to track the path from the initial to the goal state
import copy
class Node:
    def __init__(self, state):
        def findBlank(matrix):
            for x in range(len(matrix)):
                for h in range(len(matrix[x])):
                    if matrix[x][h] == "_":
                        return str(x)+str(h)
        self.state = state
        self.parent = None
        self.move = None
        self.blankLocation = findBlank(state) #get matrix coordinates of the blank location
        self.level = 0
    def findBlank(self, matrix):
            for x in range(len(matrix)):
                for h in range(len(matrix[x])):
                    if matrix[x][h] == "_":
                        return str(x)+str(h)
    def getState(self):
        tups = tuple([tuple(x) for x in self.state])
        return tups

'''class puzzleSolver:
    #create a dictionary of possible moves for each coordinate. This helps prevent the program from giving indexErrors when checking for possible moves by blocking out of index moves before they happen
    goalState = [['_',1,2],[3,4,5],[6,7,8]]
    possibleMoves = {
        "00": ['D','R'],
        "01": ['D','R','L'],
        "02": ['D','L'],
        "10": ['D','R','U'],
        "11": ['D','R','L','U'],
        "12": ['D','L','U'],
        "20": ['R','U'],
        "21": ['R','L','U'],
        "22": ['L','U']
    }
    visitedStates = []
    def solverDFS(self, node):
        #print(node.state)
        possibleMoves = self.possibleMoves[node.blankLocation]
        aux = []
        for x in range(len(node.state)):
            aux.append([])
            for h in range(len(node.state[x])):
                aux[x].append(node.state[x][h])
        newMove = Node(aux.copy())
        newMove.parent = node
        if self.isSolved(node,self.goalState):
            print("found")
            return []
        if node.state in self.visitedStates:
            return None
        else:
            self.visitedStates.append(node.state)
            x = open("log.txt", 'a')
            x.write(str(node.state))
            x.write("\n")
            x.close()
        #print("states" + str(self.visitedStates[-1]))
        if 'D' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])]
            node.move = str(moveNumber)+'U'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])] = newMove.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove)
            if result is not None:
                return result.append(node.move)
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])] = newMove.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
        if 'R' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1]
            node.move = str(moveNumber)+'L'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1] = newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove)
            if result is not None:
                return result.append(node.move)
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1] = newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
        if 'L' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1]
            node.move = str(moveNumber)+'R'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1] = newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove)
            if result is not None:
                return result.append(node.move)
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1] = newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
        if 'U' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])]
            node.move = str(moveNumber)+'D'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])] = newMove.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove)
            if result is not None:
                return result.append(node.move)
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])] = newMove.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
        

    def isSolved(self, current, goal):
        return current.state == goal
    
#scramble = Node([[7,2,4],[5,'_',6],[8,3,1]])
scramble = Node([[2,1,'_'],[3,4,5],[6,7,8]])
solve = puzzleSolver()
print(solve.solverDFS(scramble))
'''
class puzzleSolver:
    #create a dictionary of possible moves for each coordinate. This helps prevent the program from giving indexErrors when checking for possible moves by blocking out of index moves before they happen
    goalState = (('_',1,2),(3,4,5),(6,7,8))
    possibleMoves = {
        "00": ['D','R'],
        "01": ['D','R','L'],
        "02": ['D','L'],
        "10": ['D','R','U'],
        "11": ['D','R','L','U'],
        "12": ['D','L','U'],
        "20": ['R','U'],
        "21": ['R','L','U'],
        "22": ['L','U']
    }
    move = {
        'D' : (1,0),
        'U' : (-1,0),
        'L' : (0,-1),
        'R' : (0,1)
    }
    opposites = {
        'U': 'D',
        'D': 'U',
        'L': 'R',
        'R': 'L'
    }
    def successors(self, parent):
            newMove = None
            possibleMoves = self.possibleMoves[parent.blankLocation]
            children = []
            for x in possibleMoves:
                swapCoordinate = self.move[x]
                print(f"{swapCoordinate=}")
                '''moveNumber = parent.state[int(parent.blankLocation[0])+1][int(parent.blankLocation[1])]
                parent.move = str(moveNumber)+ self.opposites[x]'''
                newMove = Node([x[:] for x in parent.state])
                newMove.parent = parent
                parent.blankLocation = parent.findBlank(parent.state)
                print(f"{parent.blankLocation=}")
                blankRow = int(parent.blankLocation[0])
                print(f"{blankRow=}")
                blankCol = int(parent.blankLocation[1])
                print(f"{blankCol=}")
                newMove.state[blankRow][blankCol] = newMove.state[blankRow+swapCoordinate[0]][blankCol+swapCoordinate[1]]
                newMove.state[blankRow+swapCoordinate[0]][blankCol+swapCoordinate[1]] = '_'
                '''(newMove.state[int(parent.blankLocation[0])+swapCoordinate[0]][int(parent.blankLocation[1])], 
                 newMove.state[int(parent.blankLocation[0])][int(parent.blankLocation[1])]) = (
                      newMove.state[int(parent.blankLocation[0])][int(parent.blankLocation[1])], 
                      newMove.state[int(parent.blankLocation[0])+swapCoordinate[0]][int(parent.blankLocation[1])+swapCoordinate[1]])'''
                newMove.blankLocation=newMove.findBlank(newMove.state)
                newMove.level = parent.level+1
                children.append(newMove)
            return children

    def solver(self, node):
        visitedStates = []
        stack = []
        stack.append(node)
        visitedStates = []
        counter = 0
        path =[]
        traceMap = {}
        while True:
            state = stack.pop(-1)
            print(state.state)
            possibleMoves = self.possibleMoves[state.blankLocation]
            aux = []
            if state.state in visitedStates:
                continue
            else:
                visitedStates.append(state.state)
                print("NEW STATE" + str(state.state))
            for x in range(len(state.state)):
                aux.append([])
                for h in range(len(state.state[x])):
                    aux[x].append(state.state[x][h])
            if self.isSolved(state,self.goalState):
                return traceMap, state.parent
            #if self.isSolved(state,self.goalState):
                #return state
            for child in children:
                traceMap[child] = state #this line was added
            counter += 1
            print(counter)
    
    
    def solverBFS(self, node):
        frontier = [node]
        reached = set()
        solution = None
        numExpanded = 0
        while frontier:
            parent = frontier.pop(0)
            numExpanded += 1
            print(f"{parent.state=}")
            print(f"{reached=}")
            for child in self.successors(parent):
                state = child.getState()
                print(f"{state=}")
                if self.isSolved(state):
                    return child
                elif state not in reached:
                    reached.add((state),)
                    frontier.append(child)
            print(f"{numExpanded=}")
        return solution


            
    def isSolved(self, current):
        return current == self.goalState
    
scramble = Node([[7,2,4],[5,'_',6],[8,3,1]])
solve = puzzleSolver()
result = solve.solverBFS(scramble)
print(result)
'''moves = []
levels = []
curr = result[1]
result = result[0]
while curr is not None:
    moves.append(curr.move)
    curr = curr.parent
print(len(moves))
while (curr != None):
    if curr.level not in levels:
        moves.append(curr.move)
        levels.append(curr.level)
    if curr.parent is not None:
        curr = curr.parent
    else:
        curr = None
opposite = {
    'U' : 'D',
    'D': 'U',
    'L': 'R',
    'R':'L'
    }
new = []
for x in range(len(moves)):
    new.append
print(moves)'''
