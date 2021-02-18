import pandas as pd
import numpy as np

def aggregate_measurements(tvec,data,period="default"):
    """
    %--------------------------------------------------
    % Description:
    
    The following function takes a dataset as input
    It then plots the data as a bar or scatter plot. 
    If the dataset contains more than 24 datapoints, a scatterplot is used.
    If the dataset containg 24 or less datapoint, a bar plot is given.
    
    The user may chooce to show the consumption combined, of diveded into the 4 different zones.
    
    NOTE:
        The prjocet description clearly states 3 input arguments. For this reason, period is defined, but is not called in the main script.
        This argument, period, will be given by the user in the function.
    
    %---------------------------------------------------
    %Input:
        data = Nx4 matrix where each row is a set of measurements.
        tvec = Nx6 matrix where each row is a time vector.
        
    %---------------------------------------------------
    %Output:
        tvec_a = Nx6 matrix. Colum corresponding to the aggregated data is non-zero. The rest is zero, since aggregating time-series(data/year ect) is pure nonsense....
        data_a = Nx4 matrix where each row is a set of measurements.
    
    %---------------------------------------------------
    % Author:
        Kristian Aalling Sørensen.
        s154443.
        August 2018.
    %-------------------------------------------------------
    """
    
    while True:
        period = int(input("What period do you wanna work with?:\n1. Consumption per minute. \n2. Consumption per hour. \n3. Consumption per day.\n4. Consumption per month.\n5. Hour-of-day consumption (hourly average).\n6. No aggregation.\n"))
        #print("Existing file?: ",dataCheck);
        #data = str(input("Name of your dataset:\n"));
        try:
            if (period==1):
                print("Consumption per minute.\n");             
                Periodsum='min'
                timez=4;
                break;
                
            elif (period==2):
                print("Consumption per hour.\n");
                Periodsum='hour';
                timez=3;
                break;
            elif (period==3):
                print("Consumption per day.\n");
                Periodsum='day';
                timez =2
                break;
            elif (period==4):
                print("Consumption per month.\n");
                Periodsum='month';
                timez=1;
                break;
            elif (period==5):
                print("Hour-of-day consumption.\n");
                Periodsum = 'average';
                timez=3;
                break;
            elif (period==6):
                print("No aggregation. Original data is used.\n");
                Periodsum = 'no Aggregation'
                break;
            else:
                print("sorry. Not a valid number. Please define period using 1-5.")
        except ValueError:
            print("\nNot a valid answer. \nPlease answer a numer.\n")
            
    if Periodsum =='no Aggregation':
        tvec_a = tvec;
        data_a = data;
    else:       
        #Combining vector to aggregate.
        combined = np.hstack((tvec, data))
        df = pd.DataFrame(combined,columns = ["year","month","day","hour","minute","second","zone1","zone2","zone3","zone4"])
        #Creating loop to aggregate.
        for i in range(len(tvec[0])):  
            if (Periodsum=='hour'):
                suming = (df.groupby("hour").sum())
            elif (Periodsum=='day'):
                suming = (df.groupby("day").sum())
            elif (Periodsum=='month'):
                suming = (df.groupby("month").sum())
            elif (Periodsum=='average'):
                suming = (df.groupby("hour").mean())
            elif (Periodsum=='min'):
                suming = (df.groupby("minute").sum())
        #Output must be a Nx6 Matrix. Only time attribute that has any meaning is the aggregated one.
        #Thus, setting all but the chosen aggregating time to zero gives a matrix in which
        #the non-zero row explain the time aggregate and the non-zero colum is the values.
        #Creating time matrix:
        TimeMatrix = np.zeros((len(list(suming.index)), 6))
        #Input the aggregated time at the correct location (while the rest is zero.)
        TimeMatrix[:,timez]=np.transpose(list(suming.index))
        #Changing the summation from dataFrame to array.
        suming = np.array(suming)
        #defining output. 
        data_a = suming[:,5:9]
        tvec_a = TimeMatrix;
        
    return(tvec_a,data_a)
