import gym


if __name__ == "__main__":
    #create a simulation instance
    env = gym.make('CartPole-v0')
    #initialize the environment
    total_reward = 0.0
    total_steps = 0
    env.reset()

    while True:
        action = env.action_space.sample()
        env.render()
        env.step(env.action_space.sample())
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break
    print("Episode done in %d steps, total reward %.2f" %(total_steps, total_reward))
    