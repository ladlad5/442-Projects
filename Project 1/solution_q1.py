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
    def solverDFS(self, node, visitedStates=[]):
        possibleMoves = self.possibleMoves[node.blankLocation]
        aux = []
        for x in range(len(node.state)):
            aux.append([])
            for h in range(len(node.state[x])):
                aux[x].append(node.state[x][h])
        newMove = Node(aux.copy())
        newMove.parent = node
        if self.isSolved(node,self.goalState):
            return []
        if node.state in visitedStates:
            return None
        else:
            visitedStates.append(node.state)
        if 'D' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])]
            node.move = str(moveNumber)+'U'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])] = newMove.state[int(node.blankLocation[0])+1][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove,visitedStates)
            if result is not None:
                return result.append(node.move)
        if 'R' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1]
            node.move = str(moveNumber)+'L'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1] = newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])+1], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove,visitedStates)
            if result is not None:
                return result.append(node.move)
        if 'L' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1]
            node.move = str(moveNumber)+'R'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1] = newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])-1], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove,visitedStates)
            if result is not None:
                return result.append(node.move)
        if 'U' in possibleMoves:
            moveNumber = node.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])]
            node.move = str(moveNumber)+'D'
            newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])] = newMove.state[int(node.blankLocation[0])-1][int(node.blankLocation[1])], newMove.state[int(node.blankLocation[0])][int(node.blankLocation[1])]
            newMove.blankLocation=newMove.findBlank(newMove.state)
            result = self.solverDFS(newMove,visitedStates)
            if result is not None:
                return result.append(node.move)
        

    def isSolved(self, current, goal):
        return current.state == goal
    
scramble = Node([[7,2,4],[5,'_',6],[8,3,1]])
solve = puzzleSolver()
print(solve.solverDFS(scramble))
