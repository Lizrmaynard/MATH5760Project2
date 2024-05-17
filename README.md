# MATH5760Project2
Mathematical Finance Project regarding stock market volatility

The Project summary is as follows:
We started off question one with choosing our call and put options for 1 month and 3 months. Since we had an S_0 of $4655.27, we chose options ranging from $4450-$4750 for a variety of calls and puts. Having those chosen, we then decided to use MATLAB. This is because in MATLAB, there exists a function that calculates the Black-Scholes Implied Volatility. The function, Volatility = blsimpv(Price,Strike,Rate,Time,Value) can be given the values of the option, then given a limit for which the implied volatility should be calculated for (i.e. if the Limit =  .5, then the function will give an output for the implied volatility if it is less than 50%). We can also declare whether it is a call or put option as well. For example, one of our options for Call for one month looks like this: 
Pa4 = blsimpv(4655.27, 4700, 0.0, 1/12, 54.70, 'Limit',12,'Yield',0,'Class', {'Call'})
Where S_0 = $4655.27, K = $4700, r = 0% (as in the problem we were not told to consider a risk-free interest rate), T = 1/12, and Value = $54.70. We set the limit to be 12 (which would be a 1200% volatility) mostly to be safe that we would always get an output from the function. We did not need to consider Yield either (as per the question), and finally we tell the function that it is a call option. Once this is done for 10 1-month call options, 10 1-month put options, 10 3-month call options, and 10 3-month put options, we move on to plotting the data.
	To plot the data, we first calculate K/S_0 for each call and put option. This was then visualized in tables for each set of datapoints (where K/S_0 corresponded to its implied volatility, sigma). This was done purely to visualize the values of each datapoint. Next, we finally plotted the data where K/S_0 sits on the x-axis and sigma sits on the y-axis. We plotted the 1-month call and put options together, then the 3-month call and put options together. This resulted in a notable negative linear relationship for the 1-month call and put options, while the data for the 3-month call and put options was a little more scattered (though a slight negative linear relationship can still be noted). We then discussed our results at the end of the MATLAB code and considered why those relationships were found and concluded the problem.

	Next, for question two, we decided to use python and the pandas library to do our data analysis on SPY (and then comparing it to VIX). To do this, we first import all of the necessary functions and libraries needed to analyze the data (i.e. numpy, matplotlib, pandas, scipy, math, etc.) then import the SPY and VIX data using a pandas dataframe (we print them out to show they successfully imported and uploaded correctly). Next, we isolate the variable we want to run our calculations on, the Adj Close for SPY. Using the isolated variable, we begin our calculations to find the moving average return volatility by first finding the percentage change using the log method we used in project one, then finding the moving average volatility following the function provided (taking the square root, multiplying by 252/29, and also multiplying by 100, etc.). Then, using pandas’ ability to run a rolling average on a set of datapoints, we declare that we want a 30-day window to get the 30 day moving average. 
	For visualization purposes, we next plot the resulting 30-day window so we can see the range of the results. We also plot the Adj Close of the VIX data so we can visualize what the range of results it provides. Doing this, we plot them together to finally closely compare the results of the VIX data to the moving average return volatility. We note that the results are within a similar range, where the VIX data ranges from about 15-29, where the moving average ranges from about 20-28. Seeing the similar ranges for the two, we conclude that our moving average is in the desired range in relation to the VIX data (i.e. our moving average return volatility is not wildly spiking and hitting numbers like 60% or 5%, as it is stays within 5% of the VIX data). With the differences between the two, as they do not line up exactly, we then discuss the discrepancies in why they might be different. We discuss the Omicron variant of COVID-19 and how it affects the moving average volatility as that dataset is based on historical data while the VIX data is based on the expected volatility, which concludes our work for question two.

	Ending with question three, we start by downloading the data for Starbucks, Microsoft, Target, General Motors, and Boeing to an excel sheet. First, we note that each section of calculations or related data are within colored cells to delineate between the calculations, data, portfolios, analyzed data, and so on. We cut out the data we did not want to focus on, leaving us with the Adj Close for each stock. Once we had the desired data for calculations, we begin by finding the Daily Returns for each stock (this is done by using the equation:
Daily Return = (S_n-S_(n-1))/S_(n-1) 
Which we then run for each line of the excel data. This leaves us with the daily returns for Starbucks, Microsoft, Target, General Motors, and Boeing. After we got our daily returns, we then found the average daily return by simply taking the average of each stock’s daily returns. We then annualized this by multiplying the daily average by 252, leaving us with our mu values for each stock. Then, using the covariance function built into excel, we found our covariance matrix (which we use to declare the annualized variance for each stock).
	Next, we build our different portfolios starting with the Global Minimum Variance Portfolio, we find our A, B, and C values that are associated with the equations:
A=e^T V^(-1) e>0
B= μ^T V^(-1) e
C= μ^T V^(-1) μ>0
AC-B^2>0
	Where e is the transposed vector consisting of 1’s, µ is the transposed vector of expected returns, and V is the covariance matrix. Using these equations with our A, B, and C, we calculate the value of w_G:
w_G=(V^(-1) e)/A
	Having all of these calculations, we find our μ_p (w)  &〖 σ〗_p (w), and compare those values to the w_G for each stock. Then, we finally calculate the Sharpe Ratio for the portfolio through the equation:
S=((μ-r))/σ
	Where our r = 0%, thus S= μ/σ, which we use to calculate the Sharpe Ratio for the Global Minimum Variance Portfolio and conclude our analysis for that portfolio.
	Next, we move on to our Market Portfolio (where we assume r = 1%), we start off by calculating our α_μ through the equation:
α_μ=A(C-rB)(1/(AC-B^2 ))
	And then we go on to find our w_M using the equation:
w_M=  1/(B-Ar)(V^(-1) (μ-r))
	We also find our annualized μ-r vector values to be able to use in the above equations. We next, similarly to the Global Minimum Variance Portfolio, find our μ_p (w)  &〖 σ〗_p (w), and compare our w_D to w_μ for each of the stocks. We then conclude by finding our Sharpe Ratio (using the equation declared in the Global Minimum Variance Portfolio), which concludes our analysis of the Market Portfolio.
	This leaves us with our final portfolio, the Diversified Portfolio, by staring with finding μ_p (w)=w_D μ^T and σ_p (w)= √((w_D^T V) w_D ) , where  w_D=  (V^(-1) μ)/B (and we also include alternate ways to calculate μ_p (w) and σ_p (w) where μ_p (w)=C/B and σ_p (w)= √(C/B^2 ) ), then we calculate the w_D for each of the stocks. Then we finally calculate the Sharpe Ratio (where r = 0). Doing so gives us our best Sharpe Ratio, meaning that the Diversified Portfolio is the best Portfolio given our chosen stocks.
	We compare all of our Sharpe Ratios to those of the individual stocks, concluding that any of the portfolios are better than simply investing in any individual stock.
