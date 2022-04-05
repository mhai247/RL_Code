import gym
#create a simulation instance
env = gym.make('CartPole-v0')
#initialize the environment
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
    