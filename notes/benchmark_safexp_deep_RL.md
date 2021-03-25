# Paper 
* **Title**: Benchmarking Safe Exploration Reinforcement Learning 
* **Authors**: Alex Ray, Joshua Achiam, Dario Amodei
* **Tags**: Safe RL, Simulation
* **Year**: 2019

# Summary 
* What
  - Safety Gym is a simulator meant for testing the effectiveness of constrained reinforcement learning (RL) algorithms.
  - Contains a benchmark of 18 high-dimensional continous controll environments for safe exploration.
  - Contains 9 additional environments for debugging task perofrmance separatel from safety requirements.
  - Allows for customizable environments.
  - Contains 3 different agents: Point, Car, and Doggo. Point is constrained in 2D-plane, car resides in 2D-plane, and doggo is a quadripedal robot.
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_015.png)
  - Contains 3 different tasks: Goal, Button, and Push.
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_016.png)
  - Contains 5 constrained elements.
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_022.png)
  - Users can configure options for observation space components.

* How
  - Using the standard GYM API for RL environments provide in the Safety Gym environment to generate random actions, make environments, and etc..
  - Environments are instantiated using the OpenAI Gym *make* function.
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_021.png)
  - The full set of environments:
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_020.png)
  - For experimentation, the metrics taken into account where:
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/metrics_constrainedRL.png)

* Results 
  - Different constrained and unconstrained policy gradient methods were tested, namely: TRPO (unconstrained) and PPO (unconstrained), TRPO-Lagrangian (constrained) and PPO-Lagrangian (constrained), and CPO (constrained).
  - Lagrangian methods use adaptive penalty coefficients to apply constraints.
  -  ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/lagrangian.png)
  -  Unconstrained RL algorithms generated high returns, but took unsafe actions as measured by the cost function. However, constrained RL algorithms attain lower levels of return, but maintain desired levels of costs.
  -  Lagrangian methods enforce the constraints more-or-less reliabily compared to CPO, despite approximation errors.
  -  Lagrangian methods are able to find satifisying policies that enforce constraints.  These nontrivial results allow progression in robot locomotion when using constrained RL.  However, constrained RL struggled to learn safe locomotion policies as compared to standard RL that is more reliable in acquring locomotion behavior with higher returns.
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_017.png)
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_018.png)
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_019.png)
  
  
  
