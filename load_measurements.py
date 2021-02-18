import numpy as np
import pandas as pd
def load_measurements(*args):
    """
    %--------------------------------------------------
    % Description:
        Function to load data.
        
        The function takes a dataset as input at defines a a time vector and a data vector.
        The dataset is a .csv file contating information of electricity consumption with:
            [year, month, day, hour, minute, second, zone1, zone2, zone3, zone4]
        
        The funtion uses dataCheck(); to ask the user for a filename. 
        If the user inputs a correct filename (.csv file and exists in folder), the filename is used to load the data into an array.
        
        
        The user is then asked to select a filling mode. The filling options are as follows:
            - Forward fill, the latest correct measurement is used.
            - Backward fill, the next correct measurement is used.  
            - Drop, removing all rows with errors.
            - Mean, given all errors the mean value of the colum (without the error values.) Proof-of-concept.
        If the first row contain errors with forward fill, og the last row with backward fill the function uses 'drop fill' regardless.
    %---------------------------------------------------
    % Usage
      Input:
          filename - see dataCheck().
      Output:
          tvec = Nx6 matrix where each row is a time vector.
          data = Nx4 matrix where each row is a set of measurements.
        
    %---------------------------------------------------
    % Author:
        Kristian Sørensen
        s154443
        August 2018    
    """
    exec(open("dataCheck.py").read());
    filename,fmode = dataCheck();
    #Importing the datafile.
    data = pd.read_csv(filename, header=None);
    data = np.array(data)   
# =============================================================================
    #handeling fmode:
# =============================================================================
    #Ensuring the correct fmode.
    if isinstance(fmode, str) == True:
        fmode = fmode.lower();
    if fmode==1:
        fmode = 'forward fill';
    elif fmode==2:
        fmode = 'backward fill';
    elif fmode==3:
        fmode = 'drop';
      
    
    #If fmode = forwardfill,  the latest correct measurement is used.    
    if (fmode=='forward fill') or fmode==1:
        for i in range(len(data)):
            for j in range(len(data[0])):
                #If the first row has an error, all rows must be deletead, and thus using 'drop' fill.
                if data[0,j]==-1:
                    data[0,:]='NaN';
                    print("WARNING: There is an error in the first row. \nAll erroneous rows are deleted." );
                    fmode='drop';
                elif data[i,j]==-1 and (fmode=='forward fill'):
                    data[i,:]=data[i-1,:];
    #================================================================
    #If fmode = backwardfill,  the next correct measurement is used.  
    #This is done by flipping the dataset, so the last  row  becomes the first row while the colum values stay the same.
    #The, the same is done as with forward fill, followed by another flip.  (same as doing a for loop starting from the bottom.)
    #This ensures that errors (-1) in the middle of a dataset gets the correct values. 
    elif (fmode=='backward fill') or fmode==2:
        data = np.flipud(data)
        for i in range(len(data)):
            for j in range(len(data[0])):
                #If the last row has an error, all rows must be deletead, and thus using 'drop' fill.
                if data[0,j]==-1:                    
                    data[0,:]='NaN';
                    print("Error. There is an error in the last row. \nAll erroneous rows are deleted." );
                    fmode='drop';   
                elif data[i,j]==-1 and (fmode=='backward fill') :
                    data[i,:]=data[i-1,:]
        data = np.flipud(data) 
    #Using the 'drop' filling method by setting all the rows with an error to 'NaN'.
    if (fmode=='drop') or fmode==3 or (fmode=='mean') or (fmode==4):
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i,j]==-1:
                    data[i,:]='NaN';    
    #removing all rows with a 'NaN'. 
    #Matrix used for average ect.               
    data2 = data[~np.isnan(data).any(axis=1)]
    meanvector = np.transpose(data2.mean(0))
    #If the user, for some reason what the mean to be used..      
    if (fmode=='mean') or fmode==4:    
        for i in range(len(data)):
            for j in range(len(data[0])):
                if np.isnan(data[i,j]):
                    data[i,j]=meanvector[j];
    #If it's not mean:
    else:
        data = data[~np.isnan(data).any(axis=1)]
    
    #Defining the output.  
    tvec = data[:,0:6];
    data = data[:,6:10];
    #returning the output.
    return(tvec,data)