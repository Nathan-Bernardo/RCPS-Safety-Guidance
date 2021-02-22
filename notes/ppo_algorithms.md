# Proximal Policy Optimization Algorithms 
*February 2021*

**Overal Impression** <br>
PPO algorithm is much easier to implement compared to  Trust Region Policy Optimization (TRPO).  Not only is it much simpler to implement, but the algorithm  provides
stability and reliability compared to TRPO.  Performance overall is better, and this is shown through a few experiments using OpenAI's Gym environment.

**Key Ideas** <br>
* The paper implements PPO in an Actor-Critic Style. Actor-Critic takes advantage of the features integrated in valued-based and policy-based learning while eliminating
their drawbacks.  An actor decides which action to take while the critic tells the actor how good that action was. [Policy Gradient Algorithms](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html#actor-critic)[The idea behind Actor-Critics and how A2C and A3C improve them](https://theaisummer.com/Actor_critics/)
