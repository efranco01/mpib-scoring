# INPUT:
# TODO: Build simple ui or just use terminal for inputs
# TODO: Allow for more in-depth customization in args (argparse)
# TODO: Make script into executable (pyinstaller)
# TODO: Allow running DEFAULT and OVERRIDE (e.g. default is all tests, override is only selected plus other customizations)

# SCORING:
# TODO: Score distance using city block method (will be in the nitty gritty area)
# TODO: Score avg distance across blocks (will be in the nitty gritty area)
# TODO: The PRACT subset only has 3 instead of 4 inputs! (fix this)
# TODO: Add additional scoring methods (e.g. avg distance from correct block)
# TODO: Check for 0 in response time (this likely indicates a lack of response)

# OUTPUT:
# TODO: Display more in-depth details further along (horizontal)
# TODO: Display avg distance from correct block (incorrect answers) in the 
# TODO: Change csv file names to be more descriptive also change column names to be shorter
# TODO: Add 0s to "invalid responses" column
# TODO: Word recall add incorrect responses
# TODO: LU add mean streak length correct vs incorrect
# TODO: VS add failure for same and different
# TODO: MS sort errors by square
# TODO: Maybe add a column for interesting response time values (e.g. 0, 9999, etc.)

# OTHER:
# TODO: Compile as executable for MAC and PC
# TODO: Error handling!!!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import os
import logging as log
import shutil
import argparse as ap

class Util:
    def __init__(self) -> None:
        self.currentDir = os.getcwd()

    def findFile(self, testName=str):

        # Search for a txt file in the current directory
        files_found = []
        for file in os.listdir(self.currentDir):
            if file.endswith('.txt') and testName in file:
                files_found.append(file)

        if len(files_found) == 0:
            log.info(f'No TXT file named {testName} found in current directory')
            return None
        elif len(files_found) == 1:
            # If a TXT file is found, read it into a Pandas dataframe
            df = pd.read_csv(os.path.join(self.currentDir, files_found[0]), delimiter='\t')
            (f'Successfully read file: {files_found[0]}')
            return df
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
        log.info(f'Test ID: {testID}')
        return testID

    def makeScoredDir(self, testID=str):
        
        # Create a new directory for the scored files
        newDir = os.path.join(self.currentDir, f'{testID}_scores')
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
            if 'sc' in file or file == 'output.log':
                filePath = os.path.join(self.currentDir, file)
                shutil.move(filePath, newDir)
                log.info(f'Successfully moved {file} to {newDir}')

    def initLogging(self):
        
        # Configure logging
        log.basicConfig(filename='output.log', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        log.info('Program started')

    def outputToCsv(self, list=list, filename=str):
        
        # Convert list to dataframe
        df = pd.DataFrame(list)

        # Write dataframe to csv
        df.to_csv(filename, float_format='%.2f', index=False)

    def initScoring(self, testName=str):
        
        # Find the file
        df = self.findFile(testName)

        # Get block types
        blockTypes = self.getBlockType(df)

        # Subset data by block type
        subsetList = self.subsetByBlock(df, blockTypes)

        return subsetList
    
class InputHandler(Util):
        def __init__(self) -> None:
            super().__init__()

        def overrideMode(self):
            pass
            
        def userPrompt(self):
            # Prompt user for input
            input('Hello! Welcome to the test scoring program. Press enter to continue.')
            input('Would you like to begin in default or override mode? Press enter for default or type "override" for override mode: ')
            
            if input == 'override':
                self.overrideMode()
            else:
                return None


class Scoring(Util):
    def __init__(self) -> None:
        super().__init__()

    def fsScore(self):

        # initialize scoring
        blockDfs = self.initScoring('FiguralSpeed')

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

            blockData.append({
                'Block': blockType,
                'PC': pc,
                'Trials': block.iloc[:, 13].count(),
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect
            })

        self.outputToCsv(blockData, 'figSpd_sc.csv')

    def luScore(self):

        # initialize scoring
        blockDfs = self.initScoring('LetterUpdating')

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockName = block.iloc[0, 4]
            pc = block.iloc[:, 18].mean() / 3
            totalTrials = block.iloc[:, 18].count()

            blockData.append({
                'Block': blockName,
                'PC': pc,
                'Trials': totalTrials
            })

        self.outputToCsv(blockData, 'letUp_sc.csv')

    def msScore(self):

        # initialize scoring
        blockDfs = self.initScoring('MotoricSpeed')

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

            blockData.append({
                'Block': blockType,
                'PC': pc,
                'Trials': block.iloc[:, 13].count(),
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect
            })

        self.outputToCsv(blockData, 'motSpd_sc.csv')

    def nmScore(self):

        # initialize scoring
        blockDfs = self.initScoring('NumberMemory')

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

            blockData.append({
                'Block': blockType,
                'PC': pc,
                'Trials': totalTrials,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect
            })

        self.outputToCsv(blockData, 'numMem_sc.csv')

    # this test has a different block format and the column is 6 instead of 5
    def nbScore(self):

        # initialize scoring
        blockDfs = self.initScoring('Numerical_nBack')

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

            blockData.append({
                'Block': blockType,
                'PC': pc,
                'Total Correct': totalCorrect,
                'Trials': totalTrials,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect
            })

        self.outputToCsv(blockData, 'numNB_sc.csv')

    def nsScore(self):
    
        # initialize scoring
        blockDfs = self.initScoring('NumericalSpeed')

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 13].mean()
            totalCorrect = block.iloc[:, 13].sum()
            responseTimes = block.iloc[:, 14].mean()
            responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = block.iloc[:, 14].median()
            medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()

            blockData.append({
                'Block': blockType,
                'PC': pc,
                'Trials': totalCorrect,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect
            })

        self.outputToCsv(blockData, 'numSpd_sc.csv')

    def stScore(self):
    
        # initialize scoring
        blockDfs = self.initScoring('SpeedTabbing')

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            numPresses = block.iloc[:, 5].count()
            responseTimes = block.iloc[:, 10].mean()
            medianResponseTime = block.iloc[:, 10].median()
            firstPress = block.iloc[0, 10]
            lastPress = block.iloc[-1, 10]

            blockData.append({
                'Block': blockType,
                'Presses': numPresses,
                'Mean RT': responseTimes,
                'Med RT': medianResponseTime,
                'First Press': firstPress,
                'Last Press': lastPress
            })

        self.outputToCsv(blockData, 'spdTab_sc.csv')

    def vsScore(self):

        # initialize scoring
        blockDfs = self.initScoring('VerbalSpeed')

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 13].mean()
            responseTimes = block.iloc[:, 14].mean()
            responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = block.iloc[:, 14].median()
            medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()

            blockData.append({
                'Block': blockType,
                'PC': pc,
                'Mean RT': responseTimes,
                'Mean RT (C)': responseCorrect,
                'Mean RT (I)': responseIncorrect,
                'Med RT': medianResponseTime,
                'Med RT (C)': medianResponseCorrect,
                'Med RT (I)': medianResponseIncorrect
            })

        self.outputToCsv(blockData, 'verbSpd_sc.csv')

    def olmScore(self):

        # NOTE: consists of 6x6 grid of objects

        # initialize scoring
        blockDfs = self.initScoring('ObjectLocationMemory')
        
        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pc = block.iloc[:, 9].item()
            responseTimes = block.iloc[:, 7].item()

            blockData.append({
                'Block': blockType,
                'PC': pc,
                'Total Response Time': responseTimes
            })

        # Nitty gritty details
        # 1. Determine the original coordinates of the object
        # 2. Determine the coordinates of the object after the translation

        self.outputToCsv(blockData, 'objLocMem_sc.csv')

    def suScore(self):
    
        # NOTE: consists of 3, 3x3 grids of objects

        # initialize scoring
        blockDfs = self.initScoring('SpatialUpdating')

        # create an empty list to store block data
        blockData = []

        # score each block (this will be general scores)
        for block in blockDfs:
            blockType = block.iloc[0, 4]
            pcGrid1 = block.iloc[:, 33].mean()
            pcGrid2 = block.iloc[:, 34].mean()
            pcGrid3 = block.iloc[:, 35].mean()
            pcTotal = block.iloc[:, 36].mean()

            blockData.append({
                'Block': blockType,
                'PC Grid 1': pcGrid1,
                'PC Grid 2': pcGrid2,
                'PC Grid 3': pcGrid3,
                'PC Total': pcTotal
            })

        # Nitty gritty details
        # 1. Determine the original coordinates of the object
        # 2. Determine the coordinates of the object after the translation

        self.outputToCsv(blockData, 'spatUp_sc.csv')

    def wrScore(self):

        # initialize scoring
        blockDfs = self.initScoring('WordRecall')
        
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
                'Block': blockType,
                'PC': pc,
                'Prop Intrusions': intrusions,
                'PI (No Intrusions)': pi
            })

        self.outputToCsv(blockData, 'wrdRec_sc.csv')

if __name__ == '__main__':
    # create a new instance of the class
    scoring = Scoring()

    # initialize logging
    scoring.initLogging()

    # score the data
    scoring.fsScore()
    scoring.luScore()
    scoring.msScore()
    scoring.nmScore()
    scoring.nbScore()
    scoring.nsScore()
    scoring.stScore()
    scoring.vsScore()
    scoring.olmScore()
    scoring.suScore()
    scoring.wrScore()

    # organize the data
    scoring.makeScoredDir(scoring.getTestID())

    # print a message to the console
    print('Done!')