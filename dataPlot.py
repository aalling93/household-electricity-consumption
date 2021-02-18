import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.style.use('classic')

def dataPlot(data,tvec):
    """
    %--------------------------------------------------
    % Description:
    
    The following function takes a dataset as input
    It then plots the data as a bar or line plot. 
    If the dataset contains more than 24 datapoints, a lineplot is used.
    If the dataset contains 24 or less datapoint, a bar plot is given.
    
    The user may choose to show the consumption combined, of diveded into the 4 different zones.
    
    The function automatically saves the current plot as a .png file.
    NOTE: The  saved plot overrides previously saved plots, i.e you're not suddly having 30 .png files in your directory.. 
    
    NORE: The aggregate_measurements() function aggregate the data. The output is a data matrix and a time matrix. The time matrix has 1 non-zero colum.
          All the other colums are zero. For this reason, the user may NOT decide on a time.  The time used is the only non-zero colum in the time matrix.
          
          If the user want to see different plots, either use option(1): load data or option (2) aggregate data.
          
    
    
    Analysis using plot:
        With the plots, is easy to analyse the consumption of different zones at different times. 
        Knowing the charecteristics of the zones (as explained in mainScript.py), a good conclusion can be made.
        For instance.  It is excpected that the combines consumption is less in the August (month 8) as compared to december (month 12).
        The same hypothesis can be made for other zones and other times. 
        - less power used during the night vs. day
        - Zone 1 and zone 2 is used all yeah and should be somewhat constant during one year
        - Zone 4 contains lights and whould be less during night and summer.
        ect ect.
        
    %---------------------------------------------------
    %Input:
        data = dataset. 
    %---------------------------------------------------
    %Output:
        .png file containg the latest plots made (line or bar plot)
    
    %---------------------------------------------------
    % Author:
        Kristian Aalling Sørensen.
        s154443.
        August 2018.
    %-------------------------------------------------------
    """
    #seaborn plotting type. 
    sns.set()
    #tcev and data MUST be imported beforhand by using load_measurements() function.
    combined = np.hstack((tvec, data))
    #Combinging into dataFrame (to sum later)
    df = pd.DataFrame(combined,columns = ["year","month","day","hour","minute","second","zone1","zone2","zone3","zone4"])       
    #Ask for plot.
    
    while True:
        plotType = int(input("What type of plot do you wanna see?\n1. Plot consumption in each zone.\n2. Combines plot.\n"));
        try:
            if (plotType==1):
                print("You have selected consumption in each zone.");
                break;                    
            elif (plotType==2):
                print("You have selected combined consumption.\n");
                break;       
            else:
                print("sorry. Not a valid numer.")
        except ValueError:
            print("\nNot a valid answer. \nPlease answer a numer(1-3).\n")              
    # As for grouping.
    while True:
        groupType = int(input("How do you wanna group it??\n1. Hour.\n2. Day.\n3. Month.\n"));
        try:
            if (groupType==1):
                print("\n Grouping by hour.\n");
                #groupmode to sum dataFrame
                Groupmode = 'hour';
                #x_label to use as string varible when plotting.
                x_label ="Time (hour of day)";
                break;                    
            elif (groupType==2):
                print("Grouping by day.\n");
                Groupmode = 'day'
                x_label ="Time (day of month)";
                break;
            elif (groupType==3):
                print("Grouping by month.\n")
                Groupmode = 'month'
                x_label ="Time (month of yeah)";
                break;  
            else:
                print("sorry. Not a valid numer.")
        except ValueError:
            print("\nNot a valid answer. \nPlease answer a numer(1-3).\n") 
            
    # If aggregated data is used, there is a possible error for the choice of illustrataion.
    # For this reason, the aggregated data is automatticaly used for plotting.
    # If one wanna plot something else, the user have to either aggregate new data, or load a new dataset.
    
    #Calculating the number of non-zero colums.
    
    indexNo = np.nonzero(np.any(tvec != 0, axis=0))[0];
    #If the amout of non-zero colums is 1, plotting type is pre-defined.    
    if (len(indexNo)==1):
        print("     Warning. \nYou have aggregated your data. For this reason, only the aggregated data is plotted.\nIf you want to plot different data, you need to either aggregated anew, or load a new dataset.")
        if (indexNo[0]==1):
            Groupmode = 'month';
            x_label ="Time (month of yeah)";
            #print("Month is used.\n")
        elif (indexNo[0]==2):
            Groupmode = 'day';
            x_label ="Time (day of month)";
            #print("Day is used.\n")
        elif (indexNo[0]==3):
            Groupmode = 'hour';
            x_label ="Time (hour of day)";
            #print("Hour is used.\n");
        elif (indexNo[0]==4):
            print("Minute is chosen.\n");
            Groupmode = 'minute';
            x_label ="Minute (Min of hour)";

                                
# =============================================================================
# Plotting
# If there is more than 24 datapoints, a scatter plots i made, else a bar plot.
#  This is done in different if loops. 
# =============================================================================
    print("=============================================================================\nPlotting data.\n");   
    #Grouping the data according to input
    grouping = (df.groupby(Groupmode).sum());
    index = (list(grouping.index));
    #AFTER indexing, making it into an array. 
    groupingdata = np.array(grouping);

    #Show each zone, Line plot
    if (plotType==1) and (len(data)>=25):
        figure = plt.figure();
        plt.plot(index,groupingdata[:,5],"b*",linestyle='-',label='Zone 1')
        plt.plot(index,groupingdata[:,6],"k*",linestyle='-',label='Zone 2')
        plt.plot(index,groupingdata[:,7],"r*",linestyle='-',label='Zone 3')
        plt.plot(index,groupingdata[:,8],"g*",linestyle='-',label='Zone 4')
        plt.title("Consumption of all zones.", fontsize=20) # Set the title of the graph
        plt.xlabel(x_label, fontsize=16) # Set the x-axis label
        plt.ylabel("Consumption (Watt-hour)", fontsize=16) # Set the y-axis label
        plt.grid()
        plt.legend()
        plt.show()
        #Saving as .png. No reduction as compared to .jpg
        figure.savefig('eachZoneLinePlot.png')
        #Wanna save in .pdf instead? No problem!
        #figure.savefig('ZoneConsumption.pdf')
        
    #Show combined zones, Line plot
    elif (plotType==2) and (len(data)>=25):
        figure = plt.figure();
        plt.figure();

        plt.plot(index,(groupingdata[:,5]+groupingdata[:,6]+groupingdata[:,7]+groupingdata[:,8]),"b*",linestyle='-',label='Combined consumption')
        plt.title("Consumption of all zones combined.", fontsize=20) # Set the title of the graph
        plt.xlabel(x_label, fontsize=16) # Set the x-axis label
        plt.ylabel("Consumption (Watt-hour)", fontsize=16) # Set the y-axis label
        plt.grid()
        plt.legend()
        plt.show() 
        figure.savefig('combinedZoneLinePlot.png')
    #Show each zone, bar plot. 
    elif (plotType==2) and (len(data)<25):
    #Plotting instances.
        figure = plt.figure();
        plt.bar(index,(groupingdata[:,5]+groupingdata[:,6]+groupingdata[:,7]+groupingdata[:,8]))
        plt.title("Consumption of all zones combined.", fontsize=20) # Set the title of the graph
        plt.xlabel(x_label, fontsize=16) # Set the x-axis label
        plt.ylabel("Consumption (Watt-hour)", fontsize=16) # Set the y-axis label
        plt.grid()
        plt.legend()
        plt.show()  
        figure.savefig('CombinedZonebarPlot.png')
    elif (plotType==1) and (len(data)<25):
        figure = plt.figure();
        #changing index from list to array so it can be used in subraction in plt.bar.
        index = np.array(index)
        plt.bar(index-0.15, groupingdata[:,5],width=0.1,color='b',align='center',label='Zone 1')
        plt.bar(index-0.05, groupingdata[:,6],width=0.1,color='r',align='center',label='Zone 2')
        plt.bar(index+0.05, groupingdata[:,7],width=0.1,color='g',align='center',label='Zone 3')
        plt.bar(index+0.15, groupingdata[:,8],width=0.1,color='y',align='center',label='Zone 4')
        plt.title("Consumption of all zones.", fontsize=20) # Set the title of the graph
        plt.xlabel(x_label, fontsize=16) # Set the x-axis label
        plt.ylabel("Consumption (Watt-hour)", fontsize=16) # Set the y-axis label
        plt.grid()
        plt.legend()
        plt.show()  
        figure.savefig('eachZoneLinePlot.png')
        
         
        
    
    
    
        
