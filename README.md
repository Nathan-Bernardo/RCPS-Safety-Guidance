# Introduction

Reinforcement learning (RL) algorithms have been used to discover policies that maximize reward.  They have been heavily used in robotics as a way to mimic the human brain such that the agent can learn to find the best possible set of actions based on the given state it is in.  However, the current reinforcement learning algorithms do not gurantee safety during the learning or execution phases.  For example, training an autonomous drone to avoid obstacles would possible involve the physical collision between the drone and the object in order to receive a negative reward for it's action.  We can already observe that such process could lead to damaging the onboard components, which is not sustainable and economically efficient for the researcher. <br/>

To help improve this situation, I am researching RL algorithms that gurantee safety (i.e. Safety Reinforcement Learning) for the agent. I am working as a Machine Learning Researcher for the Resilient Cyber-Physical Systems ([RCPS](https://rcpsl.eng.uci.edu/yshoukry/)) under Yasser Shoukry.  Since Summer of 2020, I have been understanding RL algorithms with an emphasis on policy gradient methods with added constraints. My responsibility is to apply policy gradient algorithms (e.g. Proximal Policy Optimization) to prove safety gurantee for the agent during the training and execution phase.  The main tool I am using to help faciliate the research process is OpenAI's Gym and Safety Gym simulator. <br/>

Aside from my research goal, I will be sharing resources and paper notes that could possibly help students, hobbyists, and researcher develop a better understanding of Safe Reinforcement Learning.

# Resources
Lil'Log is a great resource for understanding RL.  The first article helped me comprehend with the key concepts and terminology in RL, and the common approaches taken to solving problems in RL. The second article summarizes the different policy gradient methods in RL, which is essential for my research. <br/>
* [A (Long) Peek into Reinforcement Learning](https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html) <br/>
* [Policy Gradient Algorithms](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html#reinforce)

Another great resource is Spinning Up in Deep RL, which was developed by OpenAI. Provides an introduction to RL as well as other valuable resources such as key papers in RL.  OpenAI was nice enough to provide extra sources on getting the right background (e.g. math, deep learning, terminology), and how you can learn by doing. <br/>
* [Spinning Up in Deep RL](https://spinningup.openai.com/en/latest/)

To understand how simulators work in general, Tucker Mclure provides a great explanation on simulators and how we can develop quality simulations.
* [How Simulations Work](http://www.anuncommonlab.com/articles/how-simulations-work/)

**Other Resources** <br>
<details>
 <summary>Books</summary>
 
 + [Deep Learning Book by Goodfellow](https://www.deeplearningbook.org/)
 + [Reinforcement Learning: An Introduction by Sutton and Barto](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)
 + [Optimizin Expectations: From Deep Reinforcement Learning to Stochastic Computation Graphs by Schulman](http://joschu.net/docs/thesis.pdf) 
 </details>

 
 <details>
 <summary>Sources on Policy Gradient methods</summary>
 
 + [Policy Gradient Algorithms](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html)
 + [An Intuitive Explanation of Policy Gradient](https://towardsdatascience.com/an-intuitive-explanation-of-policy-gradient-part-1-reinforce-aa4392cbfd3c)
 </details>
 
<details>
 <summary>Deep Learning</summary>
 
 + [Backpropagation calculus by 3Blue1Brown](https://www.youtube.com/watch?v=tIeHLnjs5U8)
</details>

<details>
 <summary>Concepts on Loss Functions and Entropy</summary>
 
 + [Entropy, Cross-Entropy, & KL-Divergence](https://www.youtube.com/watch?v=ErfnhcEV1O8)
 + [Loss Functions and Optimization by Stanford](https://www.youtube.com/watch?v=h7iBpEHGVNc)
 
 </details>
 
 <details>
 <summary>Online Journal and Research Databases</summary>
 
 + [arxiv sanity preserver](http://www.arxiv-sanity.com/) [[Github](https://github.com/karpathy/arxiv-sanity-preserver)] - Developed by Andrej Karpathy.  A web interface that allows researchers to keep track of relevant papers and store papers in their own personal library.  
 
 </details>

# Getting Set Up
## Installing Ubuntu dependencies
Before installing CUDA and other packages, we need to install development tools, image and video I/O libraries, GUI packages, optimization libraries, and other packages. 

First, update your system: <br />
```
$ sudo apt-get update 
$ sudo apt-get upgrade
```

Then, install the tools, libraries, and other packages: <br />
```
$ sudo apt-get install build-essential cmake unzip pkg-config
$ sudo apt-get install libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
$ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libopenblas-dev libatlas-base-dev liblapack-dev gfortran
$ sudo apt-get install libhdf5-serial-dev
$ sudo apt-get install python3-dev python3-tk python-imaging-tk
```

## Installing Cuda
I've come across many tutorials for installing CUDA and CUDANN for Ubuntu 18.04.  The tutorial I followed for installing CUDA 10.1 is from Tensorflow, and their procedure for installing Cuda, CUDNN, and TensorRT is great. Here is the link: <br />
https://www.tensorflow.org/install/gpu.

For Ubuntu 20.04, I simply installed CUDA Toolkit through their documentation. [CUDA Toolkit 11.0 Download](https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=2004&target_type=deblocal)

After installing CUDA, CUDNN, and TensorRT, paste the following text to your ~/.bashrc file: <br />
```
export PATH=/usr/local/cuda-<VERSION>/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-<VERSION>/lib64 
```

Replace <VERSION> with the CUDA version you installed. For me, it would be 11.0. Tensorflow has this nice piece of code to check whether Tensorflow is using the GPU or not.  First, reboot your system and run the code below in your terminal: <br />
 
```
tf.config.list_physical_devices('GPU')
```


## Installing Virtual Environment
Python virtual environments are great for creating an isolated environment for Python projects.  If you have two separate Python projects that require the same Python library, but different versions, then creating an isolated environment would solve this issue without having to change the version in the system.  

First, install pip: <br />
```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
```

Install virtualenv and virtualenvwrapper: <br /> 
```
$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/get-pip.py ~/.cache/pip
```
Copy and paste the following text below to the ~/.bashrc file.  You can open the ~/.bashrc file with your favorite text editor. In here, I use vim: <br />

`$ sudo vim ~/.bashrc`

```
#virtualenv and virtualenvwrapper 
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

Then, source your ~/.bashrc: <br />
`$ source ~/.bashrc`

## Installing Safety Gym
Safety Gym both run under the MuJoCo physics engine, which helps facilitate research and development in robotics and other areas that require reachers to scale up computationally intensive techniques. However, MuJoCo is not free. They only provided a 30-day free trial, or a 1-year free trial if your are a college student.  OpenAI recently passed on Gym to a new maintainer. The maintainer is planneing to substitute MuJoCo with PyBullet.  See this [post](https://github.com/openai/gym/issues/2259) for more information. <br>

Website: [MuJoCo](http://www.mujoco.org/#:~:text=MuJoCo%20is%20a%20physics%20engine,not%20merely%20a%20better%20simulator.) <br/>
Source: [mujoco-py](https://github.com/openai/mujoco-py)
### Installing mujoco_py 
```
$ git clone https://github.com/openai/mujoco-py.git
$ cd mujoco-py
$ python3 setup.py install
```

Before importing mujoco_py, make sure to past the text below to your ~/.bashrc file: <br />
`export LD_LIBRARY_PATH=$HOME/.mujoco/mujoco200/bin`

### Installing Safety Gym
Source: [Safety Gym](https://github.com/openai/safety-gym)
```
$ git clone https://github.com/openai/safety-gym.git
$ cd safety-gym
$ pip install -e .
```

## Other Simulators
###CoppeliaSim
 [Website](https://www.coppeliarobotics.com/)
To install CoppeliaSim, downloaded the software from this [source](https://www.coppeliarobotics.com/downloads) and extract the files to your desired folder. Find the folder containing CoppeliaSim and run the .sh file. In Linux:
 ```
 cd <path/to/CoppeliaSim_Edu_V4_2_0_Ubuntu20_04>
 ./coppeliaSim.sh
 ```
 
### Installing robosuite from source
To install robosuite, I folowed the documenation from the research group's docs.  It would be best to install from source.
https://robosuite.ai/docs/installation.html

When you run a demo or project with robosuite, you will get the following error: <br />
`ERROR: GLEW initalization error: Missing GL version`

Before running any project or demos with robosuite, you must export the text below to your ~/.bashrc file: <br />
`export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so`
 


# Paper Notes
<details>
 <summary>2021-03</summary>
 
 + [Benchmarking Safe Exploration in Deep Reinforcement Learning](https://cdn.openai.com/safexp-short.pdf)[[Notes](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/benchmark_safexp_deep_RL.md)]
</details>

<details>
 <summary>2021-02</summary>
 
 + [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)[[Notes](https://github.com/Nathan-Bernardo/RCPS-Safety-Guidance/blob/master/notes/ppo_algorithms.md)]
 + [ADAM: A METHOD FOR STOCHASTIC OPTIMIZATION](https://arxiv.org/pdf/1412.6980.pdf)
 + [Revisiting Design Choices in Proximal Policy Optimization](https://arxiv.org/pdf/2009.10897.pdf)
 + [Policy Gradient Methods for Reinforcement Learning with Function Approximation](https://papers.nips.cc/paper/1999/file/464d828b85b0bed98e80ade0a5c43b0f-Paper.pdf)
 + [Benchmarking Deep Reinforcement Learning for Continuous Control](https://arxiv.org/abs/1604.06778)
 + [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438)
 + [Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477)
 + [Safe Reinforcement Learning via Shielding](https://arxiv.org/abs/1708.08611)
 + [ART: Abstraction Refinement-Guided Training for Provably Correct Neural Networks](https://arxiv.org/abs/1907.10662)
 + [Uncertainty-Aware Reinforcement Learning for Collision Avoidance](https://arxiv.org/abs/1702.01182)
 + [Safety-Guided Deep Reinforcement Learning via Online Gaussian Process Estimation](https://arxiv.org/abs/1903.02526)
 + [Reinforcement Learning in Robotics: A Survey](https://www.ias.informatik.tu-darmstadt.de/uploads/Publications/Kober_IJRR_2013.pdf)
 
 </details>



