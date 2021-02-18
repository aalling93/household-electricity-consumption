"""
=============================================================================
INTRODUCTION TO PROGRAMMING - PYTHON: EXAM PROJECT.
Author:
    Kristian Sørensen
    s154443
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
#Used to import functions.
import os.path
from pathlib import Path
#Importing functions to main script. This improves readability in the main script.
exec(open("print_statistics.py").read());exec(open("load_measurements.py").read());exec(open("dataPlot.py").read())
exec(open("aggregate_measurements.py").read());exec(open("dataCheck.py").read());
#User-friendly strings used for options ect.
Introduction = "=============================================================================\nProgram to analyse household electrivcity consumption:\
                \n=============================================================================\
                \n\nThis program uses data on electricity consumptions from 4 different zones at different times for a household. It is possible for the user to anaylyse this data using the following options: \
                \n1. Load data. \
                \n2. Aggregate data.\
                \n3. Display statistics. \
                \n4. visualize electricity consumption.\
                \n5. Quit.\
                \n \nFor more information on these options, see the function descriptions.\n"
Options= "\n=============================================================================\nYou got the following options. \n1) Load data. \n2) Aggregate data. \n3) Display statistics. \n4) Visualize electricity consumption.\n5) Quit. \nPick wisely.\n=============================================================================\n";
print(Introduction);
input("Press Enter to continue...\n=============================================================================\n")
print(Options);
# =============================================================================
# Entering while loop to repeat options until program is terminated.
# =============================================================================
while True:
    try:
        Choice = int(input("Make your choice.\n"));
        #Loading dataset into time- and data vector using load_measurements() function. This MUST be done before (2-4).
        if (Choice==1):
            tvec,data = load_measurements();
            dataOriginal = data;
            tvecOriginal = tvec;
            print(Options);     
        #Aggregate data using aggregate_measurements() function.
        elif (Choice==2):
            try:
                data
            #If data isn't defined, repeat loop (i.e no time or data vectors.)
            except NameError:
                print("No data to aggregate. Load data first (option 1).\n");
                print(Options);
            else:              
                #For simplicity, the original data is used to calculate aggregated data that is used as "new" data. Done in steps for readability.
                #If this function is run, the output will be used for the later analysis (statistics, visualization ect.) 
                #This can always be cancelled by eiher loading the data again(option 1) og aggregating data again (option 2).
                #period = "This will be changed in the function.";
                tvec,data = aggregate_measurements(tvecOriginal,dataOriginal);
                print(Options);
        #Display statiscs in a table (no output) using print_statistics() function.
        elif (Choice==3):
            try:
                data
            except NameError:
                print("No statistics can be calculated without any data. Load data first (option 1) .\n");
                print(Options);
            else:
                print_statistics(tvec, data)
                print(Options);
        # Plotting data by given the user options on how-to plot using the dataPlot() function.
        elif (Choice==4):
            try:
                data
            except NameError:
                print("Can't viasualize, if no data is given. Load data first (option 1).\n")
                print(Options);
            else:
                dataPlot(data,tvec);
                print(Options);
        # Exit program. 
        elif (Choice==5):
            print("Exiting program.");
            #Clearing all non-essential varibles.
            del Introduction
            del Options
            del Choice
            #Quit.
            break   
        # If a number is given, but a wrong one, an error is given.
        elif (Choice>=6) or (Choice<=0):
            print("Not a valid number. Please answer 1-5 (followed by Enter):\n");
        #If Choice isn't a number, an error is given.
    except ValueError:
            print("\n \nNot a valid answer. The answer MUST be a number.\nReturning to start screen.\n")            
            print(Options);
#Final statement of the program...            
print("=============================================================================\nProgram is now terminated.");