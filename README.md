# Options Pricing
## Part 1. Visualize Stock Price Movements - Geometric Brownian Motion with Monte Carlo <br/>
Given a stock of company ABC that follows the Geometric Brownian Motion, we are interested in visualizing its possible price paths over a period of 10 years.

A stock that follows the Geometric Brownian Motion has a dynamic (closed form solution to the Geometric Brownian Motion SDE) below: 
<img src="http://latex.codecogs.com/svg.latex?S_t=S_0&space;e^{\sigma&space;W_t&plus;(r-\sigma^2/2)t}" title="http://latex.codecogs.com/svg.latex?S_t=S_0 e^{\sigma W_t+(r-\sigma^2/2)t}" />

For our stock ABC, we have time T = 10 years, an annualized expected return of the stock r = 0.04 or 4%, an annulized expected volatility or standard deviation of the return &sigma = 0.18 or 18%, initial stock price of S<sub>0</sub>= $88, and a random variation W<sub>t</sub> is a Standard Brownian Motion process (following Normal distribution of mean 0 and variance 1).

By dividing up the time range of T = 10 days into into a greater number of equal steps ie. 1000 steps, the simulations better represent the dynamic of stock price. In this figure, I compare expected stock price simulation when using 10 steps versus 1000 steps. I computed E[S<sub>n</sub>] for each step within [0,10] and plot all paths in one graph.

<img width=“964” src="https://github.com/MINAYUAN/Option-Pricing/blob/main/3.png">

I simulated 6 paths for the 1000 steps and 1 simualation path for the 10 steps. The path simulated using 10 steps does not capture the stock's volatility and represent the expected stock prices accurately.


## Part 2. Price European Call Option <br/>
### Black-Scholes <br/>
Given the same specification of stocks above, price a European call with strike price of 100 and T = 10. 

Substitue the information to the closed-form formula below to find the exact value of the option to be **$18.2837**.
<img width=“400” src="https://github.com/MINAYUAN/Option-Pricing/blob/main/1*vA9Przj2ncqg5shwn4iBJQ.png">

### Monte Carlo <br/>
Monte Carlo Simulation is used to calculate the expected value of the option because the expectation value of a function of a random variable, e.g. stock prices  converges to its true expectation when the number of simulations is large enough, by the Law of Large Numbers. 

Generating 1,000,000 simualtion of stock price at time T following the Geometric Brownian Motion, then compute European call option payoff and discount the expected payoff, finally take expectation of the 1,000,000 discounted payoff value. 

The estimate price is **$18.2566** using Monte Carlo, which is **$0.0271** away from the Black-Scholes value. 

### Monte Carlo with Variance Reduction Technique <br/>
Antithetic Variates is a widely used varaince reduction technique. The general idea is generating asquence of uniformly distribution vairables {U}, then using inverse-transformation method, Y1 = h(F<sup>-1</sup>(U)) and Y2 = h(F<sup>-1</sup>(1-U)), under some function h(.) will be negatively correlated. and the antithetic variates estimate using Y1 and Y2 will have lower variance than either one of Y1 or Y2 along.

Using variance reduction technical , the difference between my estiamtion and the Black-Scholes value is reduced to **$0.010649**.


## Part 3. Does American Put Hold Higher Value Than European Put? 
### Feature: Binomial Method
American put has higher price than European put that shares the same characteristics in general. The higher prices is premium for additional option that comes with American option, where American put may be advantage to exercise early. The difference is greater when the put is in the money, and less when the put is out of the money. In this graph, the strike price for both option is \$100.Option price calculated using binomial tree method

<img width=“400” src="https://github.com/MINAYUAN/Option-Pricing/blob/main/q4p4.png">

Assume the risk-free rate is 5%, the volatility of the stock price is 30%. The plot shows estiamte of the prices of European and American Put options with current stock prices varying from $80 to $120 in increment of $5.
