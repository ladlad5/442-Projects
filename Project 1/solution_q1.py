#create node system that saves each state to track the path from the initial to the goal state
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
    def findBlank(self, matrix):
            for x in range(len(matrix)):
                for h in range(len(matrix[x])):
                    if matrix[x][h] == "_":
                        return str(x)+str(h)

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
    def solver(self, node):
        visitedStates = []
        stack = []
        stack.append(node)
        visitedStates = []
        counter = 0
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
            newMove = Node(aux.copy())
            newMove.parent = state
            if self.isSolved(state,self.goalState):
                return state
            if 'D' in possibleMoves:
                moveNumber = state.state[int(state.blankLocation[0])+1][int(state.blankLocation[1])]
                state.move = str(moveNumber)+'U'
                newMoveD = Node([x[:] for x in aux])
                newMoveD.parent = state
                newMoveD.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMoveD.state[int(state.blankLocation[0])+1][int(state.blankLocation[1])] = newMoveD.state[int(state.blankLocation[0])+1][int(state.blankLocation[1])], newMoveD.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                newMoveD.blankLocation=newMoveD.findBlank(newMoveD.state)
                stack.append(newMoveD)
                #newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMove.state[int(state.blankLocation[0])+1][int(state.blankLocation[1])] = newMove.state[int(state.blankLocation[0])+1][int(state.blankLocation[1])], newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                #newMove.blankLocation=newMove.findBlank(newMove.state)
            if 'R' in possibleMoves:
                moveNumber = state.state[int(state.blankLocation[0])][int(state.blankLocation[1])+1]
                state.move = str(moveNumber)+'L'
                newMoveR = Node([x[:] for x in aux])
                newMoveR.parent = state
                newMoveR.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMoveR.state[int(state.blankLocation[0])][int(state.blankLocation[1])+1] = newMoveR.state[int(state.blankLocation[0])][int(state.blankLocation[1])+1], newMoveR.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                newMoveR.blankLocation=newMoveR.findBlank(newMoveR.state)
                stack.append(newMoveR)
                #newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])+1] = newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])+1], newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                #newMove.blankLocation=newMove.findBlank(newMove.state)
            if 'L' in possibleMoves:
                moveNumber = state.state[int(state.blankLocation[0])][int(state.blankLocation[1])-1]
                state.move = str(moveNumber)+'R'
                newMoveL = Node([x[:] for x in aux])
                newMoveL.parent = state
                newMoveL.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMoveL.state[int(state.blankLocation[0])][int(state.blankLocation[1])-1] = newMoveL.state[int(state.blankLocation[0])][int(state.blankLocation[1])-1], newMoveL.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                newMoveL.blankLocation=newMoveL.findBlank(newMoveL.state)
                stack.append(newMoveL)
                #newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])-1] = newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])-1], newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                #newMove.blankLocation=newMove.findBlank(newMove.state)
            if 'U' in possibleMoves:
                moveNumber = state.state[int(state.blankLocation[0])-1][int(state.blankLocation[1])]
                state.move = str(moveNumber)+'D'
                newMoveU = Node([x[:] for x in aux])
                newMoveU.parent = state
                newMoveU.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMoveU.state[int(state.blankLocation[0])-1][int(state.blankLocation[1])] = newMoveU.state[int(state.blankLocation[0])-1][int(state.blankLocation[1])], newMoveU.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                newMoveU.blankLocation=newMoveU.findBlank(newMoveU.state)
                stack.append(newMoveU)
                #newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])], newMove.state[int(state.blankLocation[0])-1][int(state.blankLocation[1])] = newMove.state[int(state.blankLocation[0])-1][int(state.blankLocation[1])], newMove.state[int(state.blankLocation[0])][int(state.blankLocation[1])]
                #newMove.blankLocation=newMove.findBlank(newMove.state)
            counter += 1
            print(counter)
            
    def isSolved(self, current, goal):
        return current.state == goal
    
scramble = Node([[7,2,4],[5,'_',6],[8,3,1]])
solve = puzzleSolver()
result = solve.solver(scramble)
moves = []
while (result is not None):
    moves.append(result.move)
    result = result.parent
print(moves)
print(len(moves))
