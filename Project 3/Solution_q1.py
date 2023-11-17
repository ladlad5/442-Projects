import gymnasium as gym
from collections import defaultdict
env = gym.make("Blackjack-v1", render_mode="human") # Initializing environments
observation, info = env.reset()
learningRate = 0.95
gamma = 0.85
action = 0
reward = 0
prevObservation = None
prevAction = None
Q = defaultdict(int)
N = defaultdict(int)
sumReward = 0
roundNum = 100
interval = roundNum / 10
check = 0
#def qHelper()
for x in range(roundNum):
    current = x
    if current - interval >= check:
        check += interval
        learningRate -= 0.03
        print(f'{learningRate=}')
    N[(prevObservation, prevAction)] += 1
    Q[(prevObservation, prevAction)] += (learningRate*(N[(prevObservation, prevAction)]) * 
                                         (reward + (gamma * max(Q[(observation, 1)] - Q[(prevObservation, prevAction)], 
                                                                Q[(observation, 0)] - Q[(prevObservation, prevAction)]))))
    if (Q[(observation, 0)] * N[(observation, 0)] > Q[(observation, 1)] * N[(observation, 1)]): #call q learning helper function
        action = 0
    else:
        action = 1
    prevObservation = observation
    prevAction = action
    sumReward += reward
    avgReward = sumReward/(x+1)
    print(f'{avgReward=}')
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        observation, info = env.reset()
avgReward = sumReward/roundNum
print(f'{avgReward=}')
env.close()