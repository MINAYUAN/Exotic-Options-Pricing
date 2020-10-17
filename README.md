# Options Pricing
*uncompleted*
Pricing lookback, barrier, and vanilla options on fixed income and equity securities with Binomial, Trinomial, Finite Difference, and Monte Carlo Simulation in Euler Scheme with variance reduction techniques.

* Past 0. Visualize what stock price looks like when it follows Geometric Brownian Motion (GBM)  
A stock following GBM has a formula of this: 
<img src="http://latex.codecogs.com/svg.latex?S_t=S_0&space;e^{\sigma&space;W_t&plus;(r-\sigma^2/2)t}" title="http://latex.codecogs.com/svg.latex?S_t=S_0 e^{\sigma W_t+(r-\sigma^2/2)t}" />

* Part 1. Price European Call Option on a stock following GBM through Monte Carlo Simulation   
Generate 1,000,000 simualtion of stock price at time T following GBM. Take expectation of the European call option payoff from stock price simulations and discount the expected payoff.



