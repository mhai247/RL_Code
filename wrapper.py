import gym
import random

class RandomACtionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.1):
        super(RandomACtionWrapper, self).__init__(env)
        self.epsilon = epsilon
    
    def action(self, action):
        if random.random() < self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
        return action

if __name__ == "__main__":
    env = RandomACtionWrapper(gym.make("CartPole-v0"))
    obs = env.reset()
    total_rewards = 0.0


    while True:
        action = env.action(0)
        obs, reward, done, _ = env.step(0)
        total_rewards += reward
        if done:
            break
    
    print("Reward got: {:.2f}".format(total_rewards))