from astropy.table import Table, Column
import numpy as np

def print_statistics(tvec, data):
    """
    %--------------------------------------------------
    % Description:
    
    The following function takes a dataset as input
    It the calculates the statistics for each zone and print the table. No output is given.
    The statics being:
        - minimum value
        - 25 percentile
        - 50 percentile
        - 75 percentile
        - maximum value. 
    
    %---------------------------------------------------
    %Input:
        tvec = Nx6 matrix where each row is a time vector.
        data = Nx4 matrix where each row is a set of measurements.
    %---------------------------------------------------
    %Output:
        None 
    
    %---------------------------------------------------
    % Author:
        Kristian Aalling Sørensen.
        s154443.
        August 2018.
    %-------------------------------------------------------
    """
    #Defining vectors with the data from each zone.
    zone1 = data[:,0];
    zone2 = data[:,1];
    zone3 = data[:,2];
    zone4 = data[:,3];
    
    #Creating the rows for the table using built-in functions. 
    data_rows = [(1,min(zone1),np.percentile(zone1,25),np.percentile(zone1,50),np.percentile(zone1,75),max(zone1)), \
                 (2,min(zone2),np.percentile(zone2,25),np.percentile(zone2,50),np.percentile(zone2,75),max(zone2)), \
                 (3,min(zone3),np.percentile(zone3,25),np.percentile(zone3,50),np.percentile(zone3,75),max(zone1)), \
                 (4,min(zone4),np.percentile(zone4,25),np.percentile(zone4,50),np.percentile(zone4,75),max(zone4)), \
                 ('All',data.min(),np.percentile(data,25),np.percentile(data,50),np.percentile(data,75),data.max())];
    #Creating table and given names.   



    indexNo = np.nonzero(np.any(tvec != 0, axis=0))[0];
    #If aggregated data is used, this most be stated. 
    if (len(indexNo)==1):        
        if (indexNo[0]==1):
            Groupmode = 'consumption per month';
        elif (indexNo[0]==2):
            Groupmode = 'consumption per day';
        elif (indexNo[0]==3):
            Groupmode = 'consumption per hour';
        elif (indexNo[0]==4):
            Groupmode = 'consumption per minute';
    else:
        Groupmode ="combined consumption";
      
    stat_table = Table(rows=data_rows, names=('Zone','Min(wH)', '1. percentile(wH)', '2. percentile(wH)','3. percentile(wH)','Max(wH)'))
    #Printing table. 
    print("\n=============================================================================\n Displaying statistics of",Groupmode,"\n\n",stat_table,"\n")
    
    return