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
                #print(f"{swapCoordinate=}")
                '''moveNumber = parent.state[int(parent.blankLocation[0])+1][int(parent.blankLocation[1])]
                parent.move = str(moveNumber)+ self.opposites[x]'''
                newMove = Node([x[:] for x in parent.state])
                newMove.parent = parent
                parent.blankLocation = parent.findBlank(parent.state)
                #print(f"{parent.blankLocation=}")
                blankRow = int(parent.blankLocation[0])
                #print(f"{blankRow=}")
                blankCol = int(parent.blankLocation[1])
                #print(f"{blankCol=}")
                getSwapNum = parent.state[blankRow+swapCoordinate[0]][blankCol+swapCoordinate[1]]
                currentMove = str(getSwapNum)+str(self.opposites[x])
                newMove.move = currentMove
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
    
    def getMoves(self, node):
        moves = []
        while node:
            moves.append(node.move)
            node = node.parent
        return list(reversed(moves[:-1]))

    def solverDFS(self, node):
        frontier = [node]
        reached = set()
        reached.add(node.getState())
        solution = None
        numExpanded = 0
        while frontier:
            parent = frontier.pop(-1)
            numExpanded += 1
            #print(f"{numExpanded=}")
            #print(f"{parent.state=}")
            #print(f"{reached=}")
            for child in self.successors(parent):
                state = child.getState()
                #print(f"{state=}")
                if self.isSolved(state):
                    print(f"{numExpanded=}")
                    return child
                elif state not in reached:
                    reached.add((state),)
                    frontier.append(child)
        print(f"{numExpanded=}")
        return solution
    
    
    def solverBFS(self, node):
        frontier = [node]
        reached = set()
        reached.add(node.getState())
        solution = None
        numExpanded = 0
        while frontier:
            parent = frontier.pop(0)
            numExpanded += 1
            #print(f"{numExpanded=}")
            #print(f"{parent.state=}")
            #print(f"{reached=}")
            for child in self.successors(parent):
                state = child.getState()
                #print(f"{state=}")
                if self.isSolved(state):
                    print(f"{numExpanded=}")
                    return child
                elif state not in reached:
                    reached.add((state),)
                    frontier.append(child)
        print(f"{numExpanded=}")
        return solution


            
    def isSolved(self, current):
        values = []
        for x in current[0]:
            if isinstance(x, int):
                values.append(x)
        rowSum = sum(values)
        return rowSum == 11
    
scramble = Node([[1,2,5],[3,4,'_'],[6,7,8]])
#scramble = Node([[7,2,4],[5,'_',6],[8,3,1]])
#scramble = Node([[1,4,2],[3,'_',5],[6,7,8]])
solve = puzzleSolver()
#result = solve.solverBFS(scramble)
result = solve.solverBFS(scramble)
moves = solve.getMoves(result)
print(moves)