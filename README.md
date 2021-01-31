# Introduction

Reinforcement learning (RL) algorithms have been used to discover policies that maximize reward.  They have been heavily used in robotics as a way to mimic the human brain such that the agent can learn to find the best possible set of actions based on the given state it is in.  However, the current reinforcement learning algorithms do not gurantee safety during the learning or execution phases.  For example, training an autonomous drone to avoid obstacles would possible involve the physical collision between the drone and the object in order to receive a negative reward for it's action.  We can already observe that such process could lead to damaging the onboard components, which is not sustainable and economically efficient for the researcher. <br/>

To help improve this situation, I am researching RL algorithms that gurantee safety (i.e. Safety Reinforcement Learning) for the agent. I am working as a Machine Learning Researcher for the Resilient Cyber-Physical Systems ([RCPS](https://rcpsl.eng.uci.edu/yshoukry/)) under Yasser Shoukry.  Since Summer of 2020, I have been understanding RL algorithms with an emphasis on policy gradient methods with added constraints. My responsibility is to apply policy gradient algorithms (e.g. Proximal Policy Optimization) to prove safety gurantee for the agent during the training and execution phase.  The main tool I am using to help faciliate the research process is OpenAI's Gym and Safety Gym simulator. <br/>

Aside from my research goal, I will be sharing resources and paper notes that could possibly help students, hobbyists, and researcher develop a better understanding of Safe Reinforcement Learning.


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

After installing CUDA, CUDNN, and TensorRT, paste the following text to your ~/.bashrc file: <br />
```
export PATH=/usr/local/cuda-10.1/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64 
```

Tensorflow has this nice piece of code to check whether Tensorflow is using the GPU or not.  First, reboot your system and run the code below in your terminal: <br />
 
```
tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None)
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

## Installing Gym and Safety Gym
Gym and Safety Gym both run under the MuJoCo physics engine, which helps facilitate research and development in robotics and other areas that require reachers to scale up computationally intensive techniques. <br>

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

### Installing Gym
Source: [OpenAI Gym](https://github.com/openai/gym) <br/>
Paper: [OpenAI Gym](https://arxiv.org/abs/1606.01540)
```
$ git clone https://github.com/openai/gym.git
$ cd gym
$ pip install -e .
```

### Installing Safety Gym
Source: [Safety Gym](https://github.com/openai/safety-gym)
```
$ git clone https://github.com/openai/safety-gym.git
$ cd safety-gym
$ pip install -e .
```

## Other Simulators
### Installing robosuite from source
To install robosuite, I folowed the documenation from the research grooup's docs.  It would be best to isntall from source.
https://robosuite.ai/docs/installation.html

When you run a demo or project with robosuite, you will get the following error: <br />
`ERROR: GLEW initalization error: Missing GL version`

Before running any project or demos with robosuite, you must export the text below to your ~/.bashrc file: <br />
`export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so`

# Paper Notes
<details>
 <summary>2021-02</summary>
 
 + [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
 + [Safe Reinforcement Learning via Shielding](https://arxiv.org/abs/1708.08611)
 + [ART: Abstraction Refinement-Guided Training for Provably Correct Neural Networks](https://arxiv.org/abs/1907.10662)
 + [Uncertainty-Aware Reinforcement Learning for Collision Avoidance](https://arxiv.org/abs/1702.01182)
 + [Safety-Guided Deep Reinforcement Learning via Online Gaussian Process Estimation](https://arxiv.org/abs/1903.02526)
 
 </details>



