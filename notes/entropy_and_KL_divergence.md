* Cross-entropy commonly used as a cost function for training classifiers.
* Entropy neasures how uncertain the events are.
* Cross-entropy measures the average message length.
* Cross-entropy is a function of both the true probability distribution p and the predictected probability distribution and the predicted probability distribution q.
* The amount at which the cross-entropy exceeds the entropy by some number of bits is called the relative entropy, or the Kullback-Leibler Divergence. D_kl (p|| q) = H(p,q) - H(p).
* Cross-entropy loss, or log loss, can be used as a cost function for a supervised learning problem (e.g. image classifier) to compare the two distributions.  H(p, q) = -sum(p x log(q)) summed over i iterations/samples.
* Discovered by Claude Shannon who developed the field Information Theory.
