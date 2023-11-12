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
            newMoveD = Node([x[:] for x in aux])
            newMoveD.parent = node
            newMoveD.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMoveD.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])] = newMoveD.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])], newMoveD.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMoveD.blankLocation=newMoveD.findBlank(newMoveD.state)
            self.solverDFS(newMoveD)
        if 'R' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1]
            node.move = str(moveNumber)+'L'
            newMoveR = Node([x[:] for x in aux])
            newMoveR.parent = node
            newMoveR.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMoveR.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1] = newMoveR.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1], newMoveR.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMoveR.blankLocation=newMoveR.findBlank(newMoveR.state)
            self.solverDFS(newMoveR)
        if 'L' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1]
            node.move = str(moveNumber)+'R'
            newMoveL = Node([x[:] for x in aux])
            newMoveL.parent = node
            newMoveL.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMoveL.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1] = newMoveL.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1], newMoveL.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMoveL.blankLocation=newMoveL.findBlank(newMoveL.state)
            self.solverDFS(newMoveL)

        if 'U' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])]
            node.move = str(moveNumber)+'D'
            newMoveU = Node([x[:] for x in aux])
            newMoveU.parent = node
            newMoveU.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMoveU.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])] = newMoveU.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])], newMoveU.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMoveU.blankLocation=newMoveU.findBlank(newMoveU.state)
            self.solverDFS(newMoveU)
        

    def isSolved(self, current, goal):
        return current.state == goal'''

class puzzleSolver:
    def __init__(self):
        self.goalState = [['_', 1, 2], [3, 4, 5], [6, 7, 8]]
        self.possibleMoves = {
            "00": ['D', 'R'],
            "01": ['D', 'R', 'L'],
            "02": ['D', 'L'],
            "10": ['D', 'R', 'U'],
            "11": ['D', 'R', 'L', 'U'],
            "12": ['D', 'L', 'U'],
            "20": ['R', 'U'],
            "21": ['R', 'L', 'U'],
            "22": ['L', 'U']
        }

    def solver(self, node):
        visitedStates = []
        path = self.solver_recursive(node, visitedStates)
        return path

    def solver_recursive(self, node, visitedStates):
        print(node.state)
        possibleMoves = self.possibleMoves[node.blankLocation]

        if node.state in visitedStates:
            return None

        visitedStates.append(node.state)
        print("NEW STATE" + str(node.state))

        if self.isSolved(node, self.goalState):
            return None

        for move_direction in possibleMoves:
            aux = [x[:] for x in node.state]
            if move_direction == 'D':
                moveNumber = node.state[int(node.blankLocation[0]) + 1][int(node.blankLocation[1])]
                new_move = Node([x[:] for x in aux])
                new_move.parent = node
                new_move.move = str(moveNumber) + 'U'
                new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])], new_move.state[int(node.blankLocation[0]) + 1][int(node.blankLocation[1])] = new_move.state[int(node.blankLocation[0]) + 1][int(node.blankLocation[1])], new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
                new_move.blankLocation = new_move.findBlank(new_move.state)
                path = self.solver_recursive(new_move, visitedStates)
                if path is not None:
                    path.insert(0, new_move.move)
                    return path
            if move_direction == 'R':
                moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1]
                new_move = Node([x[:] for x in aux])
                new_move.parent = node
                new_move.move = str(moveNumber) + 'L'
                new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])], new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1] = new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1], new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
                new_move.blankLocation = new_move.findBlank(new_move.state)
                path = self.solver_recursive(new_move, visitedStates)
                if path is not None:
                    path.insert(0, new_move.move)
                    return path
            if move_direction == 'L':
                moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1]
                new_move = Node([x[:] for x in aux])
                new_move.parent = node
                new_move.move = str(moveNumber) + 'R'
                new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])], new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1] = new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1], new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
                new_move.blankLocation = new_move.findBlank(new_move.state)
                path = self.solver_recursive(new_move, visitedStates)
                if path is not None:
                    path.insert(0, new_move.move)
                    return path
            if move_direction == 'U':
                moveNumber = node.state[int(node.blankLocation[0]) - 1][int(node.blankLocation[1])]
                new_move = Node([x[:] for x in aux])
                new_move.parent = node
                new_move.move = str(moveNumber) + 'D'
                new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])], new_move.state[int(node.blankLocation[0]) - 1][int(node.blankLocation[1])] = new_move.state[int(node.blankLocation[0]) - 1][int(node.blankLocation[1])], new_move.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
                new_move.blankLocation = new_move.findBlank(new_move.state)
                path = self.solver_recursive(new_move, visitedStates)
                if path is not None:
                    path.insert(0, new_move.move)
                    return path

    def isSolved(self, current_state, goal_state):
        return current_state == goal_state
    
scramble = Node([[7,2,4],[5,'_',6],[8,3,1]])
#scramble = Node([[2,1,'_'],[3,4,5],[6,7,8]])
solve = puzzleSolver()
print(solve.solver(scramble))
