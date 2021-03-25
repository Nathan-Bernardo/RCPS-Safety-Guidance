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

* How
  - Using the standard GYM API for RL environments provide in the Safety Gym environment to generate random actions, make environments, and etc..
  - Environments are instantiated using the OpenAI Gym *make* function.
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_021.png)
  - The full set of environments:
  - ![alt text](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/images/Selection_021.png)
  
  
  
