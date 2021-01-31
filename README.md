# Introduction

Reinforcement learning algorithms have been used to discover policies that maximize reward.  They have been heavily used in robotics as a way to mimic the human brain such that the agent can learn to find the best possible set of actions based on the given state it is in.  However, the current reinforcement learning algorithms do not gurantee safety during the learning or execution phases.  For example, training an autonomous drone to avoid obstacles would possible involve the physical collision between the drone and the object in order to receive a negative reward for it's action.  We can already observe that such process could lead to damaging the onboard components, which is not sustainable and economically efficient for the researcher. In this project, I am using OpenAI's Gym and Safety Gym simulator to integrate reinforcement learning algorithms for saftey gurantee.  I will also be providing resources for those interested in reinforcement learning and control theory, as well as papers related to this specific topic.

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

## Installing OpenAI and Robosuite 
### Installing OpenAI
```
git clone https://github.com/openai/gym.git
cd gym` <br />
pip install -e .
```

### Installing Mujoco

### Installing mujoco_py
```
$ git clone https://github.com/openai/mujoco-py.git
$ cd mujoco-py
$ python3 setup.py install
```

Before importing mujoco_py, make sure to past the text below to your ~/.bashrc file: <br />
`export LD_LIBRARY_PATH=$HOME/.mujoco/mujoco200/bin`

### Installing robosuite from source
To install robosuite, I folowed the documenation from the research grooup's docs.  It would be best to isntall from source.
https://robosuite.ai/docs/installation.html

When you run a demo or project with robosuite, you will get the following error: <br />
`ERROR: GLEW initalization error: Missing GL version`

Before running any project or demos with robosuite, you must export the text below to your ~/.bashrc file: <br />
`export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so`


