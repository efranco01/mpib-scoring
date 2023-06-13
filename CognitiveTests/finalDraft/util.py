import numpy as np
import pandas as pd
import os
import logging as log
import shutil

class Util:
    def __init__(self) -> None:
        self.currentDir = os.getcwd()

    def findFile(self, testName=str):
        
        # Search for a txt file in the current directory
        files_found = []
        for file in os.listdir(self.currentDir):
            if file.endswith('.txt') and testName in file:
                files_found.append(file)

        # If no TXT file is found, return None
        if len(files_found) == 0:
            log.info(f'No TXT file named {testName} found in current directory')
            return None
        
        # If one TXT file is found, read it into a Pandas dataframe
        elif len(files_found) == 1:
            df = pd.read_csv(os.path.join(self.currentDir, files_found[0]), delimiter='\t')
            (f'Successfully read file: {files_found[0]}')
            return df
        # If multiple TXT files are found, prompt the user to select one
        else:
            log.info(f'{len(files_found)} files with the name {testName} found in current directory:')
            for i, file in enumerate(files_found):
                log.info(f'{i+1}. {file}')
            selection = input('Please select the file you want to read (enter number): ')
            try:
                selection = int(selection)
            except:
                log.info('Invalid input, please enter a number.')
                return None
            if selection > 0 and selection <= len(files_found):
                df = pd.read_csv(os.path.join(self.currentDir, files_found[selection-1]), delimiter='\t')
                log.info(f'Successfully read file: {files_found[selection-1]}')
                return df
            else:
                log.info(f'Invalid selection: {selection}. Please enter a number between 1 and {len(files_found)}.')
                return None

    def getBlockType(self, df=pd.DataFrame, blockLoc=4):
        
        # List different types of blocks in the dataframe
        blockTypes = df.iloc[:, blockLoc].unique()
        
        return blockTypes
    
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

    def getTestID(self):

        # get test ID from directory name
        testID = os.path.basename(self.currentDir)
        return testID
    
    def askTestID(self):
        
        # Prompt user for test ID
        self.testID = input('Enter the test ID: ')
        
    def makeScoredDir(self, testID=str):
        
        # Create a new directory for the scored files
        newDir = os.path.join(os.getcwd(), f'{testID}_scores')
        if os.path.exists(newDir):
            # If the directory already exists, prompt the user for input
            response = input(f"Directory {newDir} already exists.\n Do you want to overwrite it? Enter 'y' for yes or 'n' for no: ")
            while response.lower() not in ['y', 'n']:
                response = input("Invalid input. Enter 'y' for yes or 'n' for no: ")
            if response.lower() == 'y':
                # If the user types 'y', delete the existing directory and create a new one
                shutil.rmtree(newDir)
                os.mkdir(newDir)
                log.info(f'Successfully created directory: {newDir}')
            elif response.lower() == 'n':
                # If the user types 'n', add an iterator to the directory name and create a new one
                i = 1
                while os.path.exists(f'{newDir}_{i}'):
                    i += 1
                newDir = f'{newDir}_{i}'
                os.mkdir(newDir)
                log.info(f'Successfully created directory: {newDir}')

        else:
            # If the directory does not exist, create a new one
            os.mkdir(newDir)
            log.info(f'Successfully created directory: {newDir}')

        # Move all files with 'scores' in their name to the new scored directory and move the log file
        for file in os.listdir(self.currentDir):
            if 'scores' not in file:
                if '_sc' in file: # or file == 'output.log'
                    filePath = os.path.join(self.currentDir, file)
                    shutil.move(filePath, newDir)
                    log.info(f'Successfully moved {file} to {newDir}')

    def initLogging(self):
        
        # Configure logging
        log.basicConfig(filename='output.log', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        log.info('Program started')

    def outputToFile(self, list=list, filename=str):
        
        # Convert list to dataframe
        df = pd.DataFrame(list)
        
        # If override mode is enabled and the File is specified, write dataframe to specified file type
        if self.overrideBool == True and self.fileOverride != []:
            if self.fileOverride[0] == 'csv':
                filename = f'{self.getTestID()}_{filename}.csv'
                df.to_csv(filename, float_format='%.2f', index=False)
            elif self.fileOverride[0] == 'xlsx':
                filename = f'{self.getTestID()}_{filename}.xlsx'
                df.to_excel(filename, float_format='%.2f', index=False)
            elif self.fileOverride[0] == 'txt':
                filename = f'{self.getTestID()}_{filename}.txt'
                df.to_csv(filename, float_format='%.2f', index=False)
        else:
            
            # If override mode is disabled or the File is not specified, write dataframe to csv
            filename = f'{self.getTestID()}_{filename}.csv'
            df.to_csv(filename, float_format='%.2f', index=False)

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
    
    def initOverride(self):
        
        input('Override mode enabled. Press enter to continue.')
        overrideDict = {"Test": [], "Block": [], "File": []}

        # Ask for settings to override (e.g. test name, block types, file output type, etc.)
        while True:
            setting = input("Enter a setting to override [Test (name of test), Block (block type), File (file type to output ex. csv, xlsx, txt)]: ")
            if setting not in overrideDict.keys():
                print("Invalid setting. Please enter 'Test', 'Block', or 'File'.")
                continue

            # Take each input as a list
            value = input(f"Enter a value for '{setting}' (separate multiple values by spaces): ")
            overrideDict[setting].extend(value.split())

            # Ask if user wants to override more settings
            more = input("Do you want to override more settings? (y/n): ")
            if more.lower() != 'y':
                break
            
        log.debug(f'Override settings: {overrideDict}')
        input('Override settings complete. Press enter to continue.')

        # Return the dictionary of overrides
        return overrideDict
        
    def askOverride(self):
        
        # Prompt user for input
        answer = input('Would you like to run in default or override mode? Press enter for default or type "override" ("o") for override mode: ')
        
        if answer == 'override' or answer == 'o':
            log.debug('Override mode enabled')
            return True
        else:
            log.debug('Default mode enabled')
            input('Default mode enabled. Press enter to continue.')
            return False
        
    def runDefault(self):
        
        print('Running default tests')
        
        # run the default scoring
        self.fsScore()
        self.luScore()
        self.msScore()
        self.nmScore()
        self.nbScore()
        self.nsScore()
        self.stScore()
        self.vsScore()
        self.olmScore()
        self.suScore()
        self.wrScore()
        
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
        
        # Ask user if they want to run in override mode
        self.overrideBool = self.askOverride()
        
        if self.overrideBool == True:
            # If override mode is enabled, ask user for settings to override
            self.overrideDict = self.initOverride()
            self.fileOverride = self.overrideDict.get('File')

            # Load user settings into runOverride function
            if self.overrideDict.get('Test') != []:
                self.runOverride(self.overrideDict.get('Test'))
                log.debug('runOverride(Test) called')
            else:
                self.runDefault()
        else:
            self.runDefault()
