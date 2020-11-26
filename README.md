# Introduction

Reinforcement learning algorithms have been used to discover policies that maximuze reward.  They have been heavily used in robotics as a way to mimic the human brain such that the agent can learn to find the best possible set of actions based on the given state it is in.  However, the current reinforcement learning algorithms do not gurantee safety during the learning or execution phases.  For example, training an autonomous drone to avoid obstacles would possible involve the physical collision between the drone and the object in order to receive a negative reward for it's action.  We can already observe that such process could lead to damaging the onboard components, which is not sustainable and economically efficient for the researcher. In this project, I am using the robosuite simulator to integrate reinforcement learning algorithms with saftey gurantee.  I will also be providing resources for those interested in reinforcement learning and control theory, as well as papers related to this specific topic.

## Installing Ubuntu dependencies
Before installing CUDA and other packages, we need to install development tools, image and video I/O libraries, GUI packages, optimization libraries, and other packages. 

First, update your system: <br />
$ sudo apt-get update  <br />
$ sudo apt-get upgrade

Then, install the tools, libraries, and other packages: <br />
$ sudo apt-get install build-essential cmake unzip pkg-config <br />
$ sudo apt-get install libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev <br />
$ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev <br />
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev <br />
$ sudo apt-get install libxvidcore-dev libx264-dev <br />
$ sudo apt-get install libgtk-3-dev <br />
$ sudo apt-get install libopenblas-dev libatlas-base-dev liblapack-dev gfortran <br />
$ sudo apt-get install libhdf5-serial-dev <br />
$ sudo apt-get install python3-dev python3-tk python-imaging-tk <br />


## Installing Cuda
I've come across many tutorials for installing CUDA and CUDANN for Ubuntu 18.04.  The tutorial below has made it easy to install cuda and cudnn for GPU acceleration. <br />
https://medium.com/@stephengregory_69986/installing-cuda-10-1-on-ubuntu-20-04-e562a5e724a0

## Installing Virtual Environment
Python virtual environments are great for creating an isolated environment for Python projects.  If you have two separate Python projects that require the same Python library, but different versions, then creating an isolated environment would solve this issue without having to change the version in the system.  

First, install pip: <br />
$ wget https://bootstrap.pypa.io/get-pip.py <br />
$ sudo python3 get-pip.py

Install virtualenv and virtualenvwrapper: <br /> 
$ sudo pip install virtualenv virtualenvwrapper <br />
$ sudo rm -rf ~/get-pip.py ~/.cache/pip

Copy and paste the following text below to the ~/.bashrc file.  You can open the ~/.bashrc file with your favorite text editor. In here, I use vim: <br />

sudo vim ~/.bashrc

#virtualenv and virtualenvwrapper 
export WORKON_HOME=$HOME/.virtualenvs <br />
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 <br />
source /usr/local/bin/virtualenvwrapper.sh

Then, source your ~/.bashrc: <br />
$ source ~/.bashrc

## Installing Robosuite 





