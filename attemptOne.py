import gym
env = gym.make('BipedalWalker-v3')
env.reset()
print("Action Space: ", env.action_space)
print("\nAction Space Bounds: (high, low) (", env.action_space.high, ", ", env.action_space.low, ")")
print("\nObservation Space: ", env.observation_space)
"""
Action 0: hip speed
Action 1: knee speed
Action 2: hip speed
Action 3: knee speed
"""
for _ in range(500):
    env.render()
    env.step([-.2, .1, .3, .4])
env.close()
