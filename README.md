# household electricity consumption

Develop, test, and document a program for analysis of household electricity consumption.

With error handeling, visualisation, main script and more...

# Functions

* Data load function:
  *  Read the data from the data filefilename
*  Data aggregation function
  * The function takes as input a matrix of time vectorstvec,  a matrix of measurementsdata, and a stringperiodthat determines how to aggregate1the measurements
* Statistics function
 *  Computes and shows statistics..
* Main scipt:
```python
=============================================================================
Author:
    Kristian Sørensen
=============================================================================
    This is an interactive program that gives the user the options of analysing electricity consumption in a househould by different means.
    The household is diveded into four zones. Each zone represent different hoursehold articles.
    Zone 1 is the kitched consisting of dishwasher, oven, microwave and more.
    Zone 2 is the laundry room with the washing machine, tumble-drier, a light and a refrigerator.
    Zone 3 is the clectric water-heater and an air-conditioner.
    Zone 4 contains all electrical equipment not given by Zone 1-Zone 3. 
    
    The user must enter a number corresponding to the options followed by Enter to use the program.
    If the user prompt a wrong input, a message is given. 
    
    If the user want to go back to the 5 original options from a new menu (as seen below in the Introduction varible), just press the Enter key (no other input in console.)
    
    The program is made in such a way, that it is possible to fully operate it in the python console using only the keybord. Hence, no figures ect. are popping op.
    
"""
```
