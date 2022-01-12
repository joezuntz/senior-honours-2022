
Background Reading
------------------

This is the paper that inspired this project:
    https://arxiv.org/pdf/2109.09636.pdf

A nice intro to autoencoders:
https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73


Installing Software
-------------------


Create the environment you need like this:

    conda create -y -p ./env -c conda-forge python=3.9 cosmosis cosmosis-build-standard-library jupyter tensorflow jupyter ipython
    conda activate ./env
    source cosmosis-configure
    cosmosis-build-standard-library


Now when you start a new work session, do this:

    conda activate ./env



Part 1
------

Make sure you can run the notebook "Likelihood-Example", which shows how to compute likelihoods, load our n(z), split it into bins, and plot it.

- write a function to compute the mean redshift of a single bin n(z)

- write a function to compute equation 2 of the hyperrank paper, assuming all the w_i values are equal

- get the d value for every realization

- take the range of d values (min and max) and construct the linear mapping from (0, 1) to (dmin, dmax) and from there to a choice of a realization with the nearest (or floor) d value

- find a way to validate that randomly choosing a number from 0 to 1 gives you a random choice from the realizations

- make a plot of the likelihood of different d values, like figure 2 in the paper


Part 2
------

This is the much harder part, and it almost certainly won't be possible to finish completely in the allotted time, so just making a good start is the goal. The method might not even work; in that case you can do a great project just by demonstrating this. 

The jupyter notebook "Keras" shows an example of a Variational Auto-encdoer (VAE), using the Tensorflow library. The code here is very complicated, but what it's doing is building a neural network that compresses the data into a small number of parameters.

The goal of this second part is to do the same for the n(z) realizations that we have - to modify this VAE so that we can train it to generate new n(z) realizations.

This will involve:
- modifying the "layers" in the VAE to make them match the shape of our data
- loading and reshaping the input data
- running the training process with our realizations
- generating new realizations and checking if they look reasonable. If not, try modifying the sizes in the layers.
- taking some lines through the new compressed parameters, generating realizations for them, and checking if the likelihood of these is smooth.

