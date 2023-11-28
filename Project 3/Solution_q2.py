import gymnasium as gym
from collections import defaultdict
import random
env = gym.make("FrozenLake-v1", desc=None, map_name="4x4", render_mode="human", is_slippery=True, ) #initialization
observation, info = env.reset()
class MDP:
    def __init__(self, gamma):
        self.C = defaultdict(int)
        self.N = defaultdict(lambda: defaultdict(int))
        self.R = defaultdict(int)
        self.gamma = gamma
        self.policy = {}
    def T(self, prevObservation, action, observation):
        return self.N[(prevObservation, action)][observation]/self.C[(prevObservation, action)]
    
    def observe(self, prevObservation, action, observation, reward):
        self.C[(prevObservation, action)] += 1
        self.N[(prevObservation, action)][observation] += 1
        self.R[(prevObservation,action,observation)] = reward

    def spaces(self):
        self.possibleStates = defaultdict(int)
        self.possibleActions = defaultdict(list)
        for state, action in self.N:
            self.possibleStates[state] = 0
            self.possibleActions[state].append(action)
        return (self.possibleStates, self.possibleActions)
    
    def QValue(self, s, a, U):
        total = 0
        for nextState in self.N[(s,a)]:
            total += (self.T(s,a,nextState)*(self.R[(s, a, nextState)] + self.gamma * U[nextState]))
        return total
    
    def bestAction(self, utility, state):
        if state in self.policy:
            return self.policy[state]
        assert self.possibleActions
        actionUtility = defaultdict(int)
        for nextAction in self.possibleActions[state]:
            for nextState in self.N[(state, nextAction)]:
                actionUtility[nextAction] += (utility[nextState] * self.T(state, nextAction, nextState))/len(self.N[(state, nextAction)])
        maxUtility = None
        maxAction = None
        for action in actionUtility:
            if maxUtility is None or maxUtility < actionUtility[action]:
                maxUtility = actionUtility[action]
                maxAction = action
        if maxAction is None:
            maxAction = env.action_space.sample()
        self.policy[state] = maxAction
        return maxAction






mdp = MDP(0.9)
for _ in range(1000):
    randnum = random.randint(1,20)
    prevObservation = observation
    action = env.action_space.sample() # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    mdp.observe(prevObservation, action, observation, reward)
    if terminated or truncated:
        observation, info = env.reset()



#gamma = 0.9
epsilon = 0.001
Utility = defaultdict(int)
prevUtility = {}
possibleActions = defaultdict(list)
delta = 0

Utility, possibleActions = mdp.spaces()
while delta >= epsilon*(1-mdp.gamma)/mdp.gamma:
    prevUtility = Utility.copy()
    delta = 0
    for state in Utility:
        maxList = []
        for action in possibleActions[state]:
            maxList.append(mdp.QValue(state, action, prevUtility))
        Utility[state] = max(maxList)
        if abs(prevUtility[state] - Utility[state]) > delta:
            delta = abs(prevUtility[state] - Utility[state])

avgReward = 0
cycleCount = 1
for _ in range(cycleCount):
    observation, info = env.reset()
    while not terminated and not truncated:
        action = mdp.bestAction(Utility, observation)
        observation, reward, terminated, truncated, info = env.step(action)
    print(f'{reward=}')
    avgReward += reward
avgReward = avgReward/cycleCount
print(f'{avgReward=}')


env.close()