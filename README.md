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

