# Options Pricing
* Part 1. Visualize Stock Price Movements - Monte Carlo
A stock that follows Geometric Brownian Motion has a dynamic below: 
<img src="http://latex.codecogs.com/svg.latex?S_t=S_0&space;e^{\sigma&space;W_t&plus;(r-\sigma^2/2)t}" title="http://latex.codecogs.com/svg.latex?S_t=S_0 e^{\sigma W_t+(r-\sigma^2/2)t}" />

where T = 10, r = 0.04, \sigma = 0.2, S<sub>0</sub>= $88 and W<sub>t</sub> is a Standard Brownian motion process.

By dividing up the time range T from [0,1000] into a greater number of equal steps, the simulations better represent the dynamic of stock price. In this figure, I compare expected stock price simulation when using 10 steps versus 1000 steps. I computed E[S<sub>n</sub>] for each step within [0,10] and plot all paths in one graph.

<img width=“964” src="https://github.com/MINAYUAN/Option-Pricing/blob/main/3.png">

I simulated 6 paths for the 1000 steps and 1 simualation path for the 10 steps. The path simulated using 10 steps does not capture the stock's volatility and represent the expected stock prices accurately.


* Part 2. Price European Call Option - Black-Scholes 
Given the same specification of stocks above, price a European call with strike price of 100 and T = 10. Substitue the information to the closed-form formula below to find the exact value of the option to be $18.2837.



* Part 3. Price European Call Option - Monte Carlo 
Monte Carlo Simulation is used to calculate the expected value of the option because the expectation value of a function of a random variable, e.g. stock prices  converges to its true expectation when the number of simulations is large enough, by the Law of Large Numbers. 

Generating 1,000,000 simualtion of stock price at time T following the Geometric Brownian Motion, then compute European call option payoff and discount the expected payoff, finally take expectation of the 1,000,000 discounted payoff value.

* Part 4. Price European Call Option - Monte Carlo with Variance Reduction Technique
Antithetic Variates is a widely used varaince reduction. The general idea is generating asquence of uniformly distribution vairables {U}, then using inverse-transformation method, Y1 = h(F<sup>-1</sup>(U)) and Y2 = h(F<sup>-1</sup>(1-U)), under some function h(.) will be negatively correlated. and the antithetic variates estimate using Y1 and Y2 will have lower variance than either one of Y1 or Y2 along.



Pricing lookback, barrier, and vanilla options on fixed income and equity securities with Binomial, Trinomial, Finite Difference, and Monte Carlo Simulation in Euler Scheme with variance reduction techniques.
