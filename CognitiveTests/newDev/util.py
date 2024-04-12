import numpy as np
import pandas as pd
import os
import shutil
import math
import sys


class Util:
    def __init__(self) -> None:
        if os.name == 'nt': # Check if OS is Windows
            self.script_dir = os.getcwd()
        else: # If OS is not Windows, change the working directory to the directory of the script (Windows does this automatically)
            self.script_dir = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])
            os.chdir(self.script_dir)
            
        print('Initial working directory:', self.script_dir)
        self.visitCounter = 0
            
    def askTestID(self):
        
        # Prompt user for test ID
        testID = input('Test ID: ')
        # Check viability of input, check if the ID consists of 4 digits
        if testID == '':
            print('No Test ID entered. Please enter a valid Test ID.')
            self.askTestID()
        elif len(testID) != 4 or testID.isdigit() == False:
            print('Invalid Test ID. Please enter a valid Test ID.')
            self.askTestID()
        else:
            return testID
        
    def askOverride(self):
        
        # Prompt user for input
        answer = input('Mode: Default (Enter) or Override (O)? ')
        
        if answer.lower() == 'override' or answer.lower() == 'o':
            return True
        else:
            input('Default mode on. Press enter.')
            return False
        
    def askVisit(self):
        
        # Prompt user for visit number
        visit = input('Score which visits? (1. 2. or 1 2): ')
        visitList = visit.split()
        # Check viability of input, check if the visit number is 1, 2 or both (separated by spaces or commas)
        if visit == '':
            print('No visit entered. Please enter a valid number of visits.')
            self.askVisit()
        elif visitList[0].isdigit() == False:
            print('Invalid visit. Please enter a valid number of visits.')
            self.askVisit()
        else:
            return visitList
        
    def cityBlockDistance(self, list1, list2):
        # will return the distance between two points using the city block method
        return abs(list2[0] - list1[0]) + abs(list2[1] - list1[1])
    
    def convertToCoord(self, letterCoord):
        if letterCoord[0] == 'A':
            return (1, int(letterCoord[1]))
        elif letterCoord[0] == 'B':
            return (2, int(letterCoord[1]))
        elif letterCoord[0] == 'C':
            return (3, int(letterCoord[1]))
        else:
            raise ValueError("Invalid letter coordinate")
    
    def euclideanDistance(self, list1, list2):    
        # will return the distance between two points using the Euclidean method
        return math.sqrt((list2[0] - list1[0])**2 + (list2[0] - list1[0])**2)
        
    def findDirectory(self, testname=str):
        for dir in os.listdir(os.getcwd()):
            if testname.lower() in dir.lower() and os.path.isdir(os.path.join(os.getcwd(), dir)):
                # If a directory is found, change the current directory to that directory
                os.chdir(os.path.join(os.getcwd(), dir))
                print(f'Dir changed to: ...{os.path.basename(os.getcwd())}')
        # If no directory is found, return error message
        return None
    
    def findFile(self, testName=str): # Need to exclude ._ files
        
        # Search for a txt file in the current directory
        files_found = []
        for file in os.listdir(os.getcwd()):
            if file.endswith('.txt') and testName in file:
                if file.startswith('._') == False:
                    files_found.append(file)

        # If no TXT file is found, return None
        if len(files_found) == 0:
            return None
        
        # If one TXT file is found, read it into a Pandas dataframe
        elif len(files_found) == 1:
            file_path = os.path.join(os.getcwd(), files_found[0])
            df = pd.read_csv(file_path, delimiter='\t', header=None)
            return df
        
        # If duplicate tests are found, score one of them and return the dataframe (add input for which one to score)
        elif len(files_found) > 1:
            choice = input(f'Duplicate tests found: {files_found}, which one would you like to score? (enter a number starting from 0): ')
            file_path = os.path.join(os.getcwd(), files_found[int(choice)])
            df = pd.read_csv(file_path, delimiter='\t', header=None)
            return df
        
    def findInput(self, visit=list, testID=str):
        
        # If visit is not specified, run default (defaults to 1st visit)
        if visit == []:
            # Find the directory with the test ID
            self.findDirectory(testID)
            self.currentVisit = '1st'
        elif visit == ['1']:
            # Find the directory with the test ID + 1st visit
            self.findDirectory(testID + ' 1st Time')  
            self.currentVisit = '1st'
        elif visit == ['2']:
            # Find the directory with the test ID + 2nd visit
            self.findDirectory(testID + ' 2nd Time')
            self.currentVisit = '2nd'
        elif visit == ['1', '2'] or visit == ['2', '1']: 
            if self.visitCounter == 0:
                # Find the directory with the first visit, runMain, then find the directory with the second visit, runMain
                self.findDirectory(testID + ' 1st Time')
                self.currentVisit = '1st'
            elif self.visitCounter == 1:
                self.findDirectory(testID + ' 2nd Time')
                self.currentVisit = '2nd'
            else:
                print('Error: counter is out of range')
        
        self.visitCounter += 1
            
    def getBlockItem(self, block, column):
        return block.iloc[:, column].item()
    
    def getBlockType(self, df=pd.DataFrame, blockLoc=4):
        # List different types of blocks in the dataframe
        blockTypes = df.iloc[:, blockLoc].unique()
        return blockTypes
    
    def getBlockValues(self, block, column):
        column_data = block.iloc[:, column].str.strip()  # Remove leading and trailing whitespace
        values = column_data.astype(str).values
        return ' '.join(values)
    
    def initialDir(self):
        return self.script_dir
        
    def initOverride(self):
        
        input('Override mode enabled. Press enter to continue.')
        overrideDict = {"Test": [], "File": []}

        # Ask for settings to override (e.g. test name, file output type, etc.)
        while True:
            setting = input("Enter a setting to override [Test (name of test), File (file type to output ex. csv, xlsx, txt)]: ")
            if setting not in overrideDict.keys():
                print("Invalid setting. Please enter 'Test' or 'File'.")
                continue

            # Take each input as a list
            value = input(f"Enter a value for '{setting}' (separate multiple values by spaces): ")
            overrideDict[setting].extend(value.split())

            # Ask if user wants to override more settings
            more = input("Do you want to override more settings? (y/n): ")
            if more.lower() != 'y':
                break
            
        input('Override settings complete. Press enter to continue.')

        # Return the dictionary of overrides
        return overrideDict
        
    def initScoring(self, testName=str):
        
        # Find the file
        df = self.findFile(testName)
        
        # If there is no file, skip scoring
        if df is None:
            return None
        
        # Get block types
        blockTypes = self.getBlockType(df)
        
        # Subset data by block type
        subsetList = self.subsetByBlock(df, blockTypes)
        return subsetList
    
    def makeScoredDir(self):
        
        # Create a new directory for the scored files
        newDir = os.path.join(os.getcwd(), f'{self.testID}_{self.currentVisit}_scores')
        if os.path.exists(newDir):
            # If the directory already exists, prompt the user for input
            response = input(f"    Dir ...{os.path.basename(newDir)} already exists.\n    Overwrite? (y/n): ")
            while response.lower() not in ['y', 'n']:
                response = input("Invalid input. Enter 'y' for yes or 'n' for no: ")
            
            if response.lower() == 'y':
                # If the user types 'y', delete the existing directory and create a new one
                shutil.rmtree(newDir)
                os.mkdir(newDir)
            
            elif response.lower() == 'n':
                # If the user types 'n', add an iterator to the directory name and create a new one
                i = 1
                while os.path.exists(f'{newDir}_{i}'):
                    i += 1
                newDir = f'{newDir}_{i}'
                os.mkdir(newDir)
                print(f'    Dir created: ...{os.path.basename(newDir)}')
        
        else:
            # If the directory does not exist, create a new one
            os.mkdir(newDir)
            print(f'    Dir created: ...{os.path.basename(newDir)}')

        # Move all files with 'scores' in their name to the new scored directory
        for file in os.listdir(os.getcwd()):
            if 'scores' not in file:
                if '_sc' in file:
                    filePath = os.path.join(os.getcwd(), file)
                    shutil.move(filePath, newDir)
                    
    def outputToFile(self, dlist, filename=str):
        
        # Declare output_path
        output_path = os.getcwd()
        
        # If list = list convert to dataframe
        # if list = dataframe, do nothing
        
        if type(dlist) == list:
            # Convert list to dataframe
            df = pd.DataFrame(dlist)
        else:
            df = dlist
            
        # Replace NaN values with 'NA'
        df.fillna(value="NA", inplace=True)
        
        # Round all values to 2 decimal places
        df = df.round(2)
        
        # If override mode is enabled and the File is specified, write dataframe to specified file type
        if self.overrideBool == True and self.fileOverride != []:
            if self.fileOverride[0] == 'csv':
                filename = os.path.join(output_path, f'{self.testID}_{self.currentVisit}_{filename}.csv')
                df.to_csv(filename, float_format='%.2f', index=False)
            elif self.fileOverride[0] == 'xlsx':
                filename = os.path.join(output_path, f'{self.testID}_{self.currentVisit}_{filename}.csv')
                df.to_excel(filename, float_format='%.2f', index=False)
            elif self.fileOverride[0] == 'txt':
                filename = os.path.join(output_path, f'{self.testID}_{self.currentVisit}_{filename}.csv')
                df.to_csv(filename, float_format='%.2f', index=False)
        
        else:
            # If override mode is disabled or the File is not specified, write dataframe to csv
            filename = os.path.join(output_path, f'{self.testID}_{self.currentVisit}_{filename}.csv')
            df.to_csv(filename, float_format='%.2f', index=False)
            
    def runDefault(self):
        
        print('    Running default tests')
        
        # run the default scoring
        self.fsScore()
        self.fsScore_long()
        self.luScore()
        self.luScore_long()
        self.msScore()
        self.msScore_long()
        self.nmScore()
        self.nmScore_long()
        self.nbScore()
        self.nbScore_long()
        self.nsScore()
        self.nsScore_long()
        self.stScore()
        self.stScore_long()
        self.vsScore()
        self.vsScore_long()
        self.olmScore()
        self.olmScore_long()
        self.suScore()
        self.suScore_long()
        self.wrScore()
        self.wrScore_long()
        
    def runOverride(self, overrideList):  # Only called if test names are overridden
        
        print('Running override tests: ' + str(overrideList))
            
        # Run specifically mentioned tests
        if 'FiguralSpeed' in overrideList or 'fs' in overrideList:
            self.fsScore()
        if 'LetterUpdating' in overrideList or 'lu' in overrideList:
            self.luScore()
        if 'MotoricSpeed' in overrideList or 'ms' in overrideList:
            self.msScore()
        if 'NumberMemory' in overrideList or 'nm' in overrideList:
            self.nmScore()
        if 'Numerical_nBack' in overrideList or 'nb' in overrideList:
            self.nbScore()
        if 'NumericalSpeed' in overrideList or 'ns' in overrideList:
            self.nsScore()
        if 'SpeedTabbing' in overrideList or 'st' in overrideList:
            self.stScore()
        if 'VerbalSpeed' in overrideList or 'vs' in overrideList:
            self.vsScore()
        if 'ObjectLocationMemory' in overrideList or 'olm' in overrideList:
            self.olmScore()
        if 'SpatialUpdating' in overrideList or 'su' in overrideList:
            self.suScore()
        if 'WordRecall' in overrideList or 'wr' in overrideList:
            self.wrScore()
            
    def runMain(self):
        
        # Ask user for test ID
        self.testID = self.askTestID()
        
        # Ask user for visit number
        self.visit = self.askVisit()
        
        # Ask user if they want to run in override mode
        self.overrideBool = self.askOverride()
        
        # Check visit number and run the appropriate function
        self.findInput(self.visit, self.testID)
        
        if self.overrideBool == True:
            # If override mode is enabled, ask user for settings to override
            self.overrideDict = self.initOverride()
            self.fileOverride = self.overrideDict.get('File')
            # Load user settings into runOverride function
            if self.overrideDict.get('Test') != []:
                self.runOverride(self.overrideDict.get('Test'))
            else:
                self.runDefault()
        else:
            self.runDefault()
            
    def runVisit(self): # May need to add this in order to run the program without asking inputs 
        
        # Return to initial directory
        os.chdir(self.initialDir())
        
        # Check visit number and run the appropriate function
        self.findInput(self.visit, self.testID)
        
        if self.overrideBool == True:
            # If override mode is enabled, ask user for settings to override
            self.overrideDict = self.initOverride()
            self.fileOverride = self.overrideDict.get('File')
            # Load user settings into runOverride function
            if self.overrideDict.get('Test') != []:
                self.runOverride(self.overrideDict.get('Test'))
            else:
                self.runDefault()
        else:
            self.runDefault()
        
        # organize the data
        self.makeScoredDir()
            
    def reRun(self): # rerun program for selected ID's
        while True:
            
            # Return to initial directory
            os.chdir(self.initialDir())
            
            # ask if there are any other IDs to score
            moreIDs = input('Are there any other IDs to score? (y/n): ')
            if moreIDs == 'y':
                # reset counter
                self.visitCounter = 0
                
                # run the main function
                self.runMain()

                # organize the data
                self.makeScoredDir()

                # print a message to the console
                print('Done!')
                
            elif moreIDs == 'n':
                break
            else:
                print('Invalid input. Please enter y or n.')
                continue
    
    def subsetByBlock(self, df=pd.DataFrame, blockTypes=np.ndarray, blockLoc=4):
        
        # Create a list to hold the subsetted dataframes
        subsetList = []
        
        # Subset data based on block number
        for block in blockTypes:
            # Create a new dataframe for each block type
            blockDf = df[df.iloc[:, blockLoc] == block]
            
            # Add each dataframe to a list
            subsetList.append(blockDf)
        
        # Return the list of dataframes
        return subsetList
    