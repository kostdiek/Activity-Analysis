# Activity-Analysis

There are Mathematica codes here (.nb) which are the ones I used for my analysis. I also started to play around with making a Python code (.py). The Mathematica code is based on the sigma of a fitted Gaussian peak. The background subtraction is done with +/- the sigma value. The Python code finds the max of the peak of interest and the background subtraction is based on +/- 1.5 keV and +/- 3 keV from the max value. I can not guarantee the validity of the Python codes as I just started working on them.


PeakInfoCout.nb:
PeakInfoCout will print to screen all of the information about the 
peak such as counts, minus, left and right averages and standard 
deviations, live time, 
etc. This doesn' t not include the half life. 
Make sure to check the widths of the peak and background 
subtraction regions.
The following is the analysis of the peaks of interest. 
The function is called PeakInfo and will output various numbers of \
use, listed toward the bottom. These numbers are exported to a file. 
DOUBLE CHECK THE FILE PATH!!! Or you can comment out that part and \
just have it output to the screen instead. 
Anything not listed in the Module part will be available after the \
function is used.

PeakGraph.nb:
PeakGraph will give you the centroid of the peak based on an initial guess.
The following is the analysis of the peaks of interest. The function is 
called PeakGraph and will output the background line that is computed.
Anything not listed in the Module part will be available after the function
is used.

Outputs.nb:
This will output to the screen the values calcuated from the other notebooks.

EvaluateRuns_v8.nb:
The eighth version that I wrote and am currently using. This will compile 
the data (it will added together multiple runs especially helpful for 
sample and background runs). There are separate sections in the code for 
efficiency runs, background runs, and samples runs. 

Background.py:
Calculates values for the background runs.

Efficiency.py:
Calculates values for the efficiency runs.

Sample.py:
Calculated values for the sample runs.

I have also included some example plots made, which will be in the final peer-reviewed paper.
