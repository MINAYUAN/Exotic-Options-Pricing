# Options Pricing
Pricing lookback, barrier, and vanilla options on fixed income and equity securities with Binomial, Trinomial, Finite Difference, and Monte Carlo Simulation in Euler Scheme with variance reduction techniques.

* Past 0. Visualize what stock price looks like when it follows Geometric Brownian Motion (GBM)  
A stock following GBM has a formula of this: 
![\Large S_t=S_0 \exp{\sigmaW_t+(r-\frac{\sigma^2}{2})t}](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)

* Part 1. Price European Call Option on a stock following GBM through Monte Carlo Simulation   
Generate 1,000,000 simualtion of stock price at time T following GBM. Take expectation of the European call option payoff from stock price simulations and discount the expected payoff.



