import numpy as np
import pandas as pd
import os
import logging as log
import shutil
import math
import sys

# TODO: Add matrix representation of correct/incorrect positions of OLM and SU tests (heatmap)

class Util:
    def __init__(self) -> None:
        self.script_dir = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])
        os.chdir(self.script_dir)
        
    def findDirectory(self, testID=str):
        for dir in os.listdir(os.getcwd()):
            if testID in dir and os.path.isdir(os.path.join(os.getcwd(), dir)):
                # If a directory is found, change the current directory to that directory
                os.chdir(os.path.join(os.getcwd(), dir))
                print('The working directory has been changed to:', os.getcwd())
        # If no directory is found, return error message
        log.info(f'No directory named {testID} found in current directory, checking for files')
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
            log.info(f'No TXT file named {testName} found in current directory')
            return None
        
        # If one TXT file is found, read it into a Pandas dataframe
        elif len(files_found) == 1:
            file_path = os.path.join(os.getcwd(), files_found[0])
            df = pd.read_csv(file_path, delimiter='\t')
            log.info(f'Successfully read file: {files_found[0]}')
            return df
        
        # If duplicate tests are found, score one of them and return the dataframe (add input for which one to score)
        elif len(files_found) > 1:
            choice = input(f'Duplicate tests found: {files_found}, which one would you like to score? (enter a number starting from 0): ')
            file_path = os.path.join(os.getcwd(), files_found[int(choice)])
            df = pd.read_csv(file_path, delimiter='\t')
            log.info(f'Successfully read file: {files_found[int(choice)]}')
            return df

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
    
    def initialDir(self):
        return self.script_dir
        
    def getTestID(self): # Not being used currently

        # get test ID from directory name
        testID = os.path.basename(os.getcwd())
        return testID
    
    def askTestID(self):
        
        # Prompt user for test ID
        testID = input('Please enter the test ID: ')
        return testID
        
    def euclideanDistance(self, list1, list2):    
        # will return the distance between two points using the Euclidean method
        return math.sqrt((list2[0] - list1[0])**2 + (list2[0] - list1[0])**2)
    
    def cityBlockDistance(self, list1, list2):
        # will return the distance between two points using the city block method
        return abs(list2[0] - list1[0]) + abs(list2[1] - list1[1])
    
    def getBlockItem(self, block, column):
        return block.iloc[:, column].item()
    
    def getBlockValues(self, block, column):
        column_data = block.iloc[:, column].str.strip()  # Remove leading and trailing whitespace
        values = column_data.astype(str).values
        return ' '.join(values)

    def convertToCoord(self, letterCoord):
        if letterCoord[0] == 'A':
            return (1, int(letterCoord[1]))
        elif letterCoord[0] == 'B':
            return (2, int(letterCoord[1]))
        elif letterCoord[0] == 'C':
            return (3, int(letterCoord[1]))
        else:
            raise ValueError("Invalid letter coordinate")

    def makeScoredDir(self):
        
        print("Current working directory:", os.getcwd())
        
        # Create a new directory for the scored files
        newDir = os.path.join(os.getcwd(), f'{self.testID}_scores')
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
                print(f'Successfully created directory: {newDir}')
                log.info(f'Successfully created directory: {newDir}')
        
        else:
            # If the directory does not exist, create a new one
            os.mkdir(newDir)
            print(f'Successfully created directory: {newDir}')
            log.info(f'Successfully created directory: {newDir}')

        # Move all files with 'scores' in their name to the new scored directory and move the log file
        for file in os.listdir(os.getcwd()):
            if 'scores' not in file:
                if '_sc' in file or ".log" in file:
                    filePath = os.path.join(os.getcwd(), file)
                    shutil.move(filePath, newDir)
                    log.info(f'Successfully moved {file} to {newDir}')

    def initLogging(self):
        
        # Configure logging
        log.basicConfig(filename='output.log', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        log.info('Program started')

    def outputToFile(self, list=list, filename=str):
        
        # Declare output_path
        output_path = os.getcwd()
        
        # Convert list to dataframe
        df = pd.DataFrame(list)
        
        df.fillna(value="NA", inplace=True)
        
        # If override mode is enabled and the File is specified, write dataframe to specified file type
        if self.overrideBool == True and self.fileOverride != []:
            if self.fileOverride[0] == 'csv':
                filename = os.path.join(output_path, f'{self.testID}_{filename}.csv')
                df.to_csv(filename, float_format='%.2f', index=False)
            elif self.fileOverride[0] == 'xlsx':
                filename = os.path.join(output_path, f'{self.testID}_{filename}.csv')
                df.to_excel(filename, float_format='%.2f', index=False)
            elif self.fileOverride[0] == 'txt':
                filename = os.path.join(output_path, f'{self.testID}_{filename}.csv')
                df.to_csv(filename, float_format='%.2f', index=False)
        
        else:
            # If override mode is disabled or the File is not specified, write dataframe to csv
            filename = os.path.join(output_path, f'{self.testID}_{filename}.csv')
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
        
        # Ask user for test ID
        self.testID = self.askTestID()
        
        # Ask user if they want to run in override mode
        self.overrideBool = self.askOverride()
        
        # Find the directory with the test ID
        self.findDirectory(self.testID)
        
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
            
class Scoring(Util):
    def __init__(self) -> None:
        super().__init__()

    def fsScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_FiguralSpeed')

        # check if scoring was successful
        if blockDfs is None:
            return
        
        # create a list to store the results
        blockData = []
        
        # score each block and add results to the list
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 13].mean()
            responseTimes = block.iloc[:, 14].mean()
            responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = block.iloc[:, 14].median()
            medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()
            maxResponseTime = block.iloc[:, 14].max()
            minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseTimeCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponseTimeCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseTimeIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseTimeIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
            
            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'Trials': block.iloc[:, 13].count(),
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect,
                'Max RT': maxResponseTime,
                'Min RT': minResponseTime,
                'Max RT (C)': maxResponseTimeCorrect,
                'Min RT (C)': minResponseTimeCorrect,
                'Max RT (I)': maxResponseTimeIncorrect,
                'Min RT (I)': minResponseTimeIncorrect,
                'Num 0': numZeroInputs
            })

        self.outputToFile(blockData, 'figSpd_sc')

    def luScore(self):
        
        # TODO: LU add mean streak length correct vs incorrect

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_LetterUpdating')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockName = block.iloc[0, 4]
            pc = block.iloc[:, 18].mean() / 3
            totalTrials = block.iloc[:, 18].count()  
            
            blockData.append({
                'ID': self.testID,
                'Block': blockName,
                'PC': pc,
                'Trials': totalTrials
            })

        self.outputToFile(blockData, 'letUp_sc')

    def msScore(self):
        
        # TODO: MS sort errors by square

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_MotoricSpeed')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 5]
            pc = block.iloc[:, 15].mean()
            totalTrials = block.iloc[:, 13].count()
            responseTimes = block.iloc[:, 14].mean()
            responseCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].mean()
            responseIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].mean()
            medianResponseTime = block.iloc[:, 14].median()
            medianResponseCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].median()
            medianResponseIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].median()
            maxResponseTime = block.iloc[:, 14].max()
            minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseTimeCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].max()
            minResponseTimeCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseTimeIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].max()
            minResponseTimeIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()

            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'Trials': totalTrials,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect,
                'Max RT': maxResponseTime,
                'Min RT': minResponseTime,
                'Max RT (C)': maxResponseTimeCorrect,
                'Min RT (C)': minResponseTimeCorrect,
                'Max RT (I)': maxResponseTimeIncorrect,
                'Min RT (I)': minResponseTimeIncorrect,
                'Num 0': numZeroInputs
            })

        self.outputToFile(blockData, 'motSpd_sc')

    def nmScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_NumberMemory')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 10].mean()
            totalTrials = block.iloc[:, 13].count()
            responseTimes = block.iloc[:, 11].mean()
            responseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11].mean()
            responseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11].mean()
            medianResponseTime = block.iloc[:, 11].median()
            medianResponseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11].median()
            medianResponseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11].median()
            maxResponseTime = block.iloc[:, 11].max()
            minResponseTime = block.iloc[:, 11][block.iloc[:, 11] >= 200].min()
            maxResponseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11].max()
            minResponseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11][block.iloc[:, 11] >= 200].min()
            maxResponseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11].max()
            minResponseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11][block.iloc[:, 11] >= 200].min()
            numZeroInputs = block[block.iloc[:, 11] == 0].iloc[:, 11].count()
            
            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'Trials': totalTrials,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect,
                'Max RT': maxResponseTime,
                'Min RT': minResponseTime,
                'Max RT (C)': maxResponseCorrect,
                'Min RT (C)': minResponseCorrect,
                'Max RT (I)': maxResponseIncorrect,
                'Min RT (I)': minResponseIncorrect,
                'Num 0': numZeroInputs
            })

        self.outputToFile(blockData, 'numMem_sc')

    # this test has a different block format and the column is 6 instead of 5
    def nbScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_Numerical_nBack')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 5]
            pc = block.iloc[:, 13].mean()
            totalCorrect = block.iloc[:, 13].sum()
            totalTrials = block.iloc[:, 13].count()
            responseTimes = block.iloc[:, 14].mean()
            responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = block.iloc[:, 14].median()
            medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()
            maxResponseTime = block.iloc[:, 14].max()
            minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponceCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
            

            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'Total Correct': totalCorrect,
                'Trials': totalTrials,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect,
                'Max RT': maxResponseTime,
                'Min RT': minResponseTime,
                'Max RT (C)': maxResponseCorrect,
                'Min RT (C)': minResponceCorrect,
                'Max RT (I)': maxResponseIncorrect,
                'Min RT (I)': minResponseIncorrect,
                'Num 0': numZeroInputs
            })

        self.outputToFile(blockData, 'numNB_sc')

    def nsScore(self):
    
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_NumericalSpeed')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 13].mean()
            totalCorrect = block.iloc[:, 13].sum()
            # Don't include 0s in response time calculation
            responseTimes = block.iloc[:, 14].mean()
            responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = block.iloc[:, 14].median()
            medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()
            maxResponseTime = block.iloc[:, 14].max()
            minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()

            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'Trials': totalCorrect,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect,
                'Max RT': maxResponseTime,
                'Min RT': minResponseTime,
                'Max RT (C)': maxResponseCorrect,
                'Min RT (C)': minResponseCorrect,
                'Max RT (I)': maxResponseIncorrect,
                'Min RT (I)': minResponseIncorrect,
                'Num 0': numZeroInputs
            })

        self.outputToFile(blockData, 'numSpd_sc')

    def stScore(self):
    
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_SpeedTabbing')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            numPresses = block.iloc[:, 5].count()
            responseTimes = block.iloc[:, 10].mean()
            medianResponseTime = block.iloc[:, 10].median()
            maxResponseTime = block.iloc[:, 10].max()
            minResponseTime = block.iloc[:, 10][block.iloc[:, 10] >= 200].min()
            firstPress = block.iloc[0, 10]
            lastPress = block.iloc[-1, 10]

            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'Presses': numPresses,
                'Mean RT': responseTimes,
                'Med RT': medianResponseTime,
                'Max RT': maxResponseTime,
                'Min RT': minResponseTime,
                'First Press': firstPress,
                'Last Press': lastPress
            })

        self.outputToFile(blockData, 'spdTab_sc')

    def vsScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_VerbalSpeed')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 13].mean()
            pcSame = block[block.iloc[:, 8] == 1].iloc[:, 13].mean()
            pcDifferent = block[block.iloc[:, 8] == 2].iloc[:, 13].mean()
            responseTimes = block.iloc[:, 14].mean()
            responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = block.iloc[:, 14].median()
            medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()
            maxResponseTime = block.iloc[:, 14].max()
            minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
            
            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'PC (Same)': pcSame,
                'PC (Different)': pcDifferent,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect,
                'Max RT': maxResponseTime,
                'Min RT': minResponseTime,
                'Max RT (C)': maxResponseCorrect,
                'Min RT (C)': minResponseCorrect,
                'Max RT (I)': maxResponseIncorrect,
                'Min RT (I)': minResponseIncorrect,
                'Num 0': numZeroInputs
            })

        self.outputToFile(blockData, 'verbSpd_sc')

    def olmScore(self):

        # NOTE: consists of 6x6 grid of objects
        # TODO: Add additional scoring methods (e.g. avg distance from correct block)
        # TODO: Add a matrix representation of the grid showing correct vs incorrect responses
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_ObjectLocationMemory')
        
        # check if scoring was successful
        if blockDfs is None:
            return
        
        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 9].item()
            responseTimes = block.iloc[:, 7].item()
            
            # 12 stimuli total
            cellDistances = {
                '1': [[self.getBlockItem(block, 12), self.getBlockItem(block, 13)], [self.getBlockItem(block, 61), self.getBlockItem(block, 62)]],
                '2': [[self.getBlockItem(block, 16), self.getBlockItem(block, 17)], [self.getBlockItem(block, 66), self.getBlockItem(block, 67)]],
                '3': [[self.getBlockItem(block, 20), self.getBlockItem(block, 21)], [self.getBlockItem(block, 71), self.getBlockItem(block, 72)]],
                '4': [[self.getBlockItem(block, 24), self.getBlockItem(block, 25)], [self.getBlockItem(block, 76), self.getBlockItem(block, 77)]],
                '5': [[self.getBlockItem(block, 28), self.getBlockItem(block, 29)], [self.getBlockItem(block, 81), self.getBlockItem(block, 82)]],
                '6': [[self.getBlockItem(block, 32), self.getBlockItem(block, 33)], [self.getBlockItem(block, 86), self.getBlockItem(block, 87)]],
                '7': [[self.getBlockItem(block, 36), self.getBlockItem(block, 37)], [self.getBlockItem(block, 91), self.getBlockItem(block, 92)]],
                '8': [[self.getBlockItem(block, 40), self.getBlockItem(block, 41)], [self.getBlockItem(block, 96), self.getBlockItem(block, 97)]],
                '9': [[self.getBlockItem(block, 44), self.getBlockItem(block, 45)], [self.getBlockItem(block, 101), self.getBlockItem(block, 102)]],
                '10': [[self.getBlockItem(block, 48), self.getBlockItem(block, 49)], [self.getBlockItem(block, 106), self.getBlockItem(block, 107)]],
                '11': [[self.getBlockItem(block, 52), self.getBlockItem(block, 53)], [self.getBlockItem(block, 111), self.getBlockItem(block, 112)]],
                '12': [[self.getBlockItem(block, 56), self.getBlockItem(block, 57)], [self.getBlockItem(block, 116), self.getBlockItem(block, 117)]]
                #   correct(x, y), response(x, y)
            }
            
            # there should be a way to do this in a loop, but I'm not sure how yet
            # maybe a dictionary with the coordinates of each cell? then loop through the dictionary
            
            cellDistancesEuclidean = {
                '1' : self.euclideanDistance(cellDistances['1'][0], cellDistances['1'][1]),
                '2' : self.euclideanDistance(cellDistances['2'][0], cellDistances['2'][1]),
                '3' : self.euclideanDistance(cellDistances['3'][0], cellDistances['3'][1]),
                '4' : self.euclideanDistance(cellDistances['4'][0], cellDistances['4'][1]),
                '5' : self.euclideanDistance(cellDistances['5'][0], cellDistances['5'][1]),
                '6' : self.euclideanDistance(cellDistances['6'][0], cellDistances['6'][1]),
                '7' : self.euclideanDistance(cellDistances['7'][0], cellDistances['7'][1]),
                '8' : self.euclideanDistance(cellDistances['8'][0], cellDistances['8'][1]),
                '9' : self.euclideanDistance(cellDistances['9'][0], cellDistances['9'][1]),
                '10' : self.euclideanDistance(cellDistances['10'][0], cellDistances['10'][1]),
                '11' : self.euclideanDistance(cellDistances['11'][0], cellDistances['11'][1]),
                '12' : self.euclideanDistance(cellDistances['12'][0], cellDistances['12'][1])
            }
            
            cellDistancesCityBlock = {
                '1' : self.cityBlockDistance(cellDistances['1'][0], cellDistances['1'][1]),
                '2' : self.cityBlockDistance(cellDistances['2'][0], cellDistances['2'][1]),
                '3' : self.cityBlockDistance(cellDistances['3'][0], cellDistances['3'][1]),
                '4' : self.cityBlockDistance(cellDistances['4'][0], cellDistances['4'][1]),
                '5' : self.cityBlockDistance(cellDistances['5'][0], cellDistances['5'][1]),
                '6' : self.cityBlockDistance(cellDistances['6'][0], cellDistances['6'][1]),
                '7' : self.cityBlockDistance(cellDistances['7'][0], cellDistances['7'][1]),
                '8' : self.cityBlockDistance(cellDistances['8'][0], cellDistances['8'][1]),
                '9' : self.cityBlockDistance(cellDistances['9'][0], cellDistances['9'][1]),
                '10' : self.cityBlockDistance(cellDistances['10'][0], cellDistances['10'][1]),
                '11' : self.cityBlockDistance(cellDistances['11'][0], cellDistances['11'][1]),
                '12' : self.cityBlockDistance(cellDistances['12'][0], cellDistances['12'][1])
            }
            
            meanEuclideanDist = np.array(list(cellDistancesEuclidean.values())).mean()
            meanCityBlockDist = np.array(list(cellDistancesCityBlock.values())).mean()
            
            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'Total RT': responseTimes,
                'Mean ED': meanEuclideanDist,
                'Mean CB': meanCityBlockDist,
                'ED 1': cellDistancesEuclidean['1'],
                'ED 2': cellDistancesEuclidean['2'],
                'ED 3': cellDistancesEuclidean['3'],
                'ED 4': cellDistancesEuclidean['4'],
                'ED 5': cellDistancesEuclidean['5'],
                'ED 6': cellDistancesEuclidean['6'],
                'ED 7': cellDistancesEuclidean['7'],
                'ED 8': cellDistancesEuclidean['8'],
                'ED 9': cellDistancesEuclidean['9'],
                'ED 10': cellDistancesEuclidean['10'],
                'ED 11': cellDistancesEuclidean['11'],
                'ED 12': cellDistancesEuclidean['12'],
                'CB 1': cellDistancesCityBlock['1'],
                'CB 2': cellDistancesCityBlock['2'],
                'CB 3': cellDistancesCityBlock['3'],
                'CB 4': cellDistancesCityBlock['4'],
                'CB 5': cellDistancesCityBlock['5'],
                'CB 6': cellDistancesCityBlock['6'],
                'CB 7': cellDistancesCityBlock['7'],
                'CB 8': cellDistancesCityBlock['8'],
                'CB 9': cellDistancesCityBlock['9'],
                'CB 10': cellDistancesCityBlock['10'],
                'CB 11': cellDistancesCityBlock['11'],
                'CB 12': cellDistancesCityBlock['12']
            })

        self.outputToFile(blockData, 'objLocMem_sc')

    def suScore(self):
    
        # TODO: Check ED and CB calculations

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_SpatialUpdating')
        
        # check if scoring was successful
        if blockDfs is None:
            return

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pcGrid1 = block.iloc[:, 33].mean()
            pcGrid2 = block.iloc[:, 34].mean()
            pcGrid3 = block.iloc[:, 35].mean()
            pcTotal = block.iloc[:, 36].mean()
            
            gridCoords = {
                '1': (self.convertToCoord(self.getBlockValues(block, 22)), self.convertToCoord(self.getBlockValues(block, 28))),
                '2': (self.convertToCoord(self.getBlockValues(block, 24)), self.convertToCoord(self.getBlockValues(block, 30))),
                '3': (self.convertToCoord(self.getBlockValues(block, 26)), self.convertToCoord(self.getBlockValues(block, 32))),
                # correct(A1) and incorrect(A2) coordinates --> (x1, y1), (x2, y2)
            }
            
            cellED = {
                '1': self.euclideanDistance(gridCoords['1'][0], gridCoords['1'][1]),
                '2': self.euclideanDistance(gridCoords['2'][0], gridCoords['2'][1]),
                '3': self.euclideanDistance(gridCoords['3'][0], gridCoords['3'][1])
            }
            
            cellCB = {
                '1': self.cityBlockDistance(gridCoords['1'][0], gridCoords['1'][1]),
                '2': self.cityBlockDistance(gridCoords['2'][0], gridCoords['2'][1]),
                '3': self.cityBlockDistance(gridCoords['3'][0], gridCoords['3'][1])
            }
            
            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC Grid 1': pcGrid1,
                'PC Grid 2': pcGrid2,
                'PC Grid 3': pcGrid3,
                'PC Total': pcTotal,
                'ED Grid 1': cellED['1'],
                'ED Grid 2': cellED['2'],
                'ED Grid 3': cellED['3'],
                'CB Grid 1': cellCB['1'],
                'CB Grid 2': cellCB['2'],
                'CB Grid 3': cellCB['3']
            })

        self.outputToFile(blockData, 'spatUp_sc')

    def wrScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_WordRecall')
        
        # check if scoring was successful
        if blockDfs is None:
            return
        
        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 24].item() / block.iloc[:, 23].item()
            intrusions = block.iloc[:, 25].item() / block.iloc[:, 23].item()
            # proportion incorrect (i.e., no intrusions)
            pi = (block.iloc[:, 23].item() - block.iloc[:, 24].item() - block.iloc[:, 25].item()) / block.iloc[:, 23].item() 
            blockData.append({
                'ID': self.testID,
                'Block': blockType,
                'PC': pc,
                'Prop Intrusions': intrusions,
                'PI (No Intrusions)': pi
            })

        self.outputToFile(blockData, 'wrdRec_sc')
        
if __name__ == '__main__':
    # create a new instance of the class
    scoringTime = Scoring()

    # initialize logging
    scoringTime.initLogging()

    # run the main function
    scoringTime.runMain()

    # organize the data
    scoringTime.makeScoredDir()

    # print a message to the console
    print('Done!')
    
    # ask if there are any other IDs to score
    while True:
        
        # Return to initial directory
        os.chdir(scoringTime.initialDir())
        
        # ask if there are any other IDs to score
        moreIDs = input('Are there any other IDs to score? (y/n): ')
        if moreIDs == 'y':
            # run the main function
            scoringTime.runMain()

            # organize the data
            scoringTime.makeScoredDir()

            # print a message to the console
            print('Done!')
        elif moreIDs == 'n':
            break
        else:
            print('Invalid input. Please enter y or n.')
            continue
