import gym
import time 

#env = gym.make('CartPole-v0')
#env.reset()
#for _ in range(1000):
#    env.render()
#    env.step(env.action_space.sample())
#env.close()

env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()


