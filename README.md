# Explore the Use of Matplotlib

This is very similar to Matlab.

I found that the plotting was not working on MacOSX.
I solved this in the following way.

## solution
1. go to ~/.matplotlib  
    `cd ~/.matplotlib`
2. create a file called matplotlibrc  
    `touch matplotlibrc`
3. inside this file put the following code:  
    `backend: TkAgg`  
    I used nano, but any text editor will do.

Types of Graphs/Charts covered:
1. Line Graph -- also smoothed
2. Bar Charts -- NB bars can be stacked as well.
3. Histograms
4. Scatter Plots
5. Stack Plots
6. Pie Charts