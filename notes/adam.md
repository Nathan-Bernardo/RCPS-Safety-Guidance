# Adam: A Method For Stochastic Optimization 
*Feb. 2020*

**Overall Impression** <br>
As mentioned in the abstract, this algorithm is straightforward to implement and performs very well as stochastic optimizer.  I have used
the Adam optimizer for training neural networks for reinforcement learning and computer vision tasks that implement a neural network
architecture, and the convergence rate is noticeably high.

**Key Ideas** <br>
* In general, Adam is:
  - simplme to implement
  - computational efficient
  - has little memory requirements
  - invariant to diagonal rescaling of the gradients
  - and well suited for problems with large data and/or parameters 

**Technical Details** <br>
* The algorithm for implementing Adam is in pg. 2.
* Without the bias correction, beta2 (in RMSProp and AdaGrad) being infinitsimally close to 1 would lead to large bias and infinitely large parameter updates.
