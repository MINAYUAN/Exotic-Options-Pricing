# Options Pricing
Pricing lookback, barrier, and vanilla options on fixed income and equity securities with Binomial, Trinomial, Finite Difference, and Monte Carlo Simulation in Euler Scheme with variance reduction techniques.

* Past 1. Visualize stock price movements with Geometric Brownian Motion using Monte Carlo
A stock that follows Geometric Brownian Motion has a dynamic below: 
<img src="http://latex.codecogs.com/svg.latex?S_t=S_0&space;e^{\sigma&space;W_t&plus;(r-\sigma^2/2)t}" title="http://latex.codecogs.com/svg.latex?S_t=S_0 e^{\sigma W_t+(r-\sigma^2/2)t}" />

where T = 10, r = 0.04, \sigma = 0.2, S<sub>0</sub>= $88 and W<sub>t</sub> is a Standard Brownian motion process.

By dividing up the time range T into a greater number of steps, the simulations can better represent the dynamic of stock price. In this figure, I compare expected stock price simulation using 10 steps versus 1000 steps, where each expected stock price is the mean from 1000 simulations. I ran 6 simulations path for the 1000 steps and 1 simualation path for the 10 step to show the difference.


<img width=“964” src="https://github.com/MINAYUAN/Option-Pricing/blob/main/3.png">


* Part 1. Price European Call Option on a stock following GBM through Monte Carlo Simulation   
Generate 1,000,000 simualtion of stock price at time T following GBM. Take expectation of the European call option payoff from stock price simulations and discount the expected payoff.



