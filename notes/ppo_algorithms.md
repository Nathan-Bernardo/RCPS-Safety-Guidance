# Proximal Policy Optimization Algorithms 
*February 2021*

**Overal Impression** <br>
PPO algorithm is much easier to implement compared to  Trust Region Policy Optimization (TRPO).  Not only is it much simpler to implement, but the algorithm  provides
stability and reliability compared to TRPO.  Performance overall is better, and this is shown through a few experiments using OpenAI's Gym environment.

**Key Ideas** <br>
* The paper implements PPO in an Actor-Critic Style. Actor-Critic takes advantage of the features integrated in valued-based and policy-based learning while eliminating
their drawbacks.  An actor decides which action to take while the critic tells the actor how good that action was. [[Policy Gradient Algorithms](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html#actor-critic)][[The idea behind Actor-Critics and how A2C and A3C improve them](https://theaisummer.com/Actor_critics/)]
* For implementing a neural network architecture that shares parameters between the policy and value function,
  - Loss function used is in page 9, which uses an entrop bonus to ensure sufficient exploration and combines both the policy surrogate and a value function error term.
  - A fully connected multi-percepton layer (MLP) with two hidden layers of 64 units, and tanh nonlinearities, are used to represent the policy. (pg. 5)
* Tested on 7 simulated robotic tasks implemented in OpenAI Gym.
  - Regarding the continous domain on different Mujoco environments, PPO outperforms both the A2C, A2C with Trust Region, and A3C.
* Results 
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_023.png)
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_024.png)

**Technical Details** <br>
* The paper implements an ibjective function that uses clipping, which clips the probability ratio.  This removes the motivation for moving the probability ratio outside of the interval [1 - eps, 1 + eps]. (pg. 3)
