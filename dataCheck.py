import os.path
from pathlib import Path
import glob

def dataCheck(*args):
    """
    %--------------------------------------------------
    % Description:
    
    The following function takes a file name as input.
    If the filename exist in the directory, the function is exited.
    Else, the function will keep on looping until a correct file name is given. 
    
    If the function is started by mistake, the user may stop the loop by writing 'stop loop' (without ' ').
    This will exit the loop, returning no output. The program is the executed.
    
    If a wrong filename is given, the function shows the .csv files in the dir. These are the allowed files to give. 
    
    After a correct filename is given, the user has to define the filling mode.
    For more information on the filling, see load_measurements();
    
    
    %---------------------------------------------------
    %Function input:
        No function input.
     Text input:
        Name of a .csv file in the same folder as the function. 
           - must be .csv
           - must exist in the same folder as the function
           - Dont use "" or '' when writing the file name
           - NOTE: if stop loop is used, the function is ended, and the options will be given again.
     fmode:
         - Way of filling the rows with errors. 
    %---------------------------------------------------
    %Output:
        data = A valid filename.
               The filename is a string with the extention .csv.
               The filename is placed in the same folder as the function.
    
    %---------------------------------------------------
    % Author:
        Kristian Aalling Sørensen.
        s154443.
        August 2018.
    %-------------------------------------------------------
    """
    #Checking if file exists. If it exists, and is a .csv file, this is used in the load_measurements() function. 
    while True:        
        dataset = (input("Name of your dataset:\n"))
        dataCheck = os.path.isfile(dataset);        
        try:
            if (dataCheck==True) and (dataset.lower().endswith('.csv')==True):
                data = dataset;
                break;
            elif (dataCheck==True) and (dataset.lower().endswith('.csv')==False):
                # Showing the user the possible .csv files in directory, i.e is NOT showing .py files ect.
                print("\nSorry, wrong extention.\nPlease only input '.csv' files. Possible files are:\n",glob.glob('*.csv'))
            elif (dataset=="stop loop"):
                print("\nDont wanna give a dataset? - okay.\n")
                return None                        
            elif (dataCheck==False):
                # Showing the user the possible .csv files in directory, i.e is NOT showing .py files ect.
                print("\nFile doesn't exist in directory. Try again.\nNOTE: rembemer .csv extention and no quotes. Possible files are:\n",glob.glob('*.csv'))  
        except FileNotFoundError:
            print("\nFile doesn't exist. Try again. \nPossible files are:\n",glob.glob('*.csv'))
            
    #Finding the filling mode that is to be used in the load_measurements() function.         
    while True:
        #pre-defining string only for readability.
        string = "What mode do you wanna use?:\
        \n1. Fill forward (replace corrupt measurement with latest valid measurement) \
        \n2. Fill backward (replace corrupt measurement with next valid measurement) \
        \n3. Delete corrupt measurements\
        \n4. Using the mean value of the matrix.\
        \n"
        fmode = int(input(string))
        #print("Existing file?: ",dataCheck);
        #data = str(input("Name of your dataset:\n"));
        try:
            if (fmode==1):
                print("Forward fill is used. Please wait.\n");
                break;
            elif (fmode==2):
                print("Backward fill is used. Please wait.\n");
                break;
            elif (fmode==3):
                print("Drop fill is used. Please wait.\n");
                break;
            elif (fmode==4):
                print("The mean value is used. Please wait.\n")
                break;
            else:
                print("sorry. Not a valid numer for fmode")
        except ValueError:
            print("\nNot a valid answer. \nPlease answer a numer(1-4).\n")
                
    #Returning the two varibles to be used in load_measurements.        
    return (data,fmode)
