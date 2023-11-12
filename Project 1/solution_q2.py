#create node system that saves each state to track the path from the initial to the goal state
import copy
import heapq
import math
class Node:
    def __init__(self, state):
        def findBlank(matrix):
            for x in range(len(matrix)):
                for h in range(len(matrix[x])):
                    if matrix[x][h] == '_':
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
                newMove = Node([x[:] for x in parent.state])
                newMove.parent = parent
                parent.blankLocation = parent.findBlank(parent.state)
                blankRow = int(parent.blankLocation[0])
                blankCol = int(parent.blankLocation[1])
                getSwapNum = parent.state[blankRow+swapCoordinate[0]][blankCol+swapCoordinate[1]]
                currentMove = str(getSwapNum)+str(self.opposites[x])
                newMove.move = currentMove
                newMove.state[blankRow][blankCol] = newMove.state[blankRow+swapCoordinate[0]][blankCol+swapCoordinate[1]]
                newMove.state[blankRow+swapCoordinate[0]][blankCol+swapCoordinate[1]] = '_'
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
            for child in self.successors(parent):
                state = child.getState()
                if self.isSolved(state):
                    print(f"{numExpanded=}")
                    return child
                elif state not in reached:
                    reached.add((state),)
                    frontier.append(child)
        print(f"DFS {numExpanded=}")
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
                    print(f"BFS {numExpanded=}")
                    return child
                elif state not in reached:
                    reached.add((state),)
                    frontier.append(child)
        print(f"BFS {numExpanded=}")
        return solution
    
    def solverUCS(self, node):
        tiebreaker = 0
        frontier = [(len(self.getMoves(node)),tiebreaker,node)]
        reached = {}
        solution = None
        numexpanded = 0
        while frontier and (solution is None or frontier[0][0] < len(self.getMoves(solution))):
            numexpanded += 1
            cost, _, parent = heapq.heappop(frontier)
            for child in self.successors(parent):
                state = child.getState()
                if state not in reached or cost + 1 < len(self.getMoves(reached[state])):
                    reached[state] = child
                    tiebreaker += 1
                    heapq.heappush(frontier, (cost + 1, tiebreaker, child))
                    if self.isSolved(state) and (solution is None or cost+1 < len(self.getMoves(solution))):
                        solution = child
        print(f"UCS {numexpanded=}")
        return solution


    def sumHeuristic(self, state, heuristic):
        goalCoords = {
            '_': (0,0),
            1: (0,1),
            2: (0,2),
            3: (1,0),
            4: (1,1),
            5: (1,2),
            6: (2,0),
            7: (2,1),
            8: (2,2),
        }
        total = 0
        for rowId, row in enumerate(state):
            for colId, num in enumerate(row):
                total += heuristic(goalCoords[num], rowId, colId)
        return total

    def manhattan(self, state):
        return self.sumHeuristic(state, self.manhattanHelper)
    
    def manhattanHelper(self, goal, row, col):
        return sum([abs(goal[0]-row), abs(goal[1]-col)])
    
    def straightLine(self, state):
        return self.sumHeuristic(state, self.straightLineHelper)
    
    def straightLineHelper(self, goal, row, col):
        return math.sqrt(sum([abs(goal[0]-row)**2, abs(goal[1]-col)**2]))
    
    def solverAStar(self, node, heuristic=lambda state: 0):
        tiebreaker = 0
        frontier = [(len(self.getMoves(node))+heuristic(node.getState()),tiebreaker,node)]
        reached = {}
        solution = None
        numExpanded = 0
        while frontier and (solution is None or frontier[0][0] < len(self.getMoves(solution))):
            numExpanded += 1
            cost, _, parent = heapq.heappop(frontier)
            for child in self.successors(parent):
                state = child.getState()
                if state not in reached or cost + 1 < len(self.getMoves(reached[state])):
                    reached[state] = child
                    tiebreaker += 1
                    heapq.heappush(frontier, (cost + 1 + heuristic(state), tiebreaker, child))
                    if self.isSolved(state) and (solution is None or cost+1 < len(self.getMoves(solution))):
                        solution = child
        print(f"A* {numExpanded=}")
        return solution   


    def isSolved(self, current):
        values = []
        for x in current[0]:
            if isinstance(x, int):
                values.append(x)
        rowSum = sum(values)
        return rowSum == 11
    
solve = puzzleSolver()
with open('input.txt') as f:
    puzzle = f.readlines()
puzzle = str(puzzle[0]).split(',')
for x in range(len(puzzle)):
    if puzzle[x].isnumeric():
        puzzle[x] = int(puzzle[x])
scramble = Node([puzzle[0:3], puzzle[3:6], puzzle[6:]])
result = solve.solverDFS(scramble)
moves = solve.getMoves(result)
print(f"The solution of q2.1 is: \n{moves}")
result = solve.solverBFS(scramble)
moves = solve.getMoves(result)
print(f"The solution of q2.2 is: \n{moves}")
result = solve.solverUCS(scramble)
moves = solve.getMoves(result)
print(f"The solution of q2.3 is: \n{moves}")
result = solve.solverAStar(scramble, solve.manhattan)
moves = solve.getMoves(result)
print(f"The solution of q2.4 is: \n{moves}")
result = solve.solverAStar(scramble, solve.straightLine)
moves = solve.getMoves(result)
print(f"The solution of q2.5 is: \n{moves}")

