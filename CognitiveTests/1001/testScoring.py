# INPUT:
# TODO: Build simple ui or just use terminal for inputs
# TODO: Allow for more in-depth customization in args (argparse)

# SCORING:
# TODO: Score distance using city block method (will be in the nitty gritty area)
# TODO: Score avg distance across trials (will be in the nitty gritty area)
# TODO: The PRACT subset only has 3 instead of 4 inputs! (fix this)

# OUTPUT:
# TODO: Display more in-depth details further along (horizontal)
# TODO: Display avg distance from correct block (incorrect answers) in the 
# TODO: Print LOGS stating what is being done

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
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

        if len(files_found) == 0:
            print(f'No TXT file named {testName} found in current directory')
            return None
        elif len(files_found) == 1:
            # If a TXT file is found, read it into a Pandas dataframe
            df = pd.read_csv(os.path.join(self.currentDir, files_found[0]), delimiter='\t')
            print(f'Successfully read file: {files_found[0]}')
            return df
        else:
            print(f'{len(files_found)} files with the name {testName} found in current directory:')
            for i, file in enumerate(files_found):
                print(f'{i+1}. {file}')
            selection = input('Please select the file you want to read (enter number): ')
            try:
                selection = int(selection)
            except:
                print('Invalid input, please enter a number.')
                return None
            if selection > 0 and selection <= len(files_found):
                df = pd.read_csv(os.path.join(self.currentDir, files_found[selection-1]), delimiter='\t')
                print(f'Successfully read file: {files_found[selection-1]}')
                return df
            else:
                print(f'Invalid selection: {selection}. Please enter a number between 1 and {len(files_found)}.')
                return None

    def getTrialType(self, df=pd.DataFrame, trialLoc=4):
        
        # List different types of trials in the dataframe
        trialTypes = df.iloc[:, trialLoc].unique()
        
        return trialTypes
    
    def subsetByTrial(self, df=pd.DataFrame, trialTypes=np.ndarray, trialLoc=4):
        
        # Create a list to hold the subsetted dataframes
        subsetList = []
        
        # Subset data based on trial number
        for trial in trialTypes:
            # Create a new dataframe for each trial type
            trialDf = df[df.iloc[:, trialLoc] == trial]
            
            # Add each dataframe to a list
            subsetList.append(trialDf)
        
        # Return the list of dataframes
        return subsetList

    def makeScoredDir(self):
        
        # Create a new directory for the scored files
        newDir = os.path.join(self.currentDir, 'scored')
        if not os.path.exists(newDir):
            os.mkdir(newDir)
            print(f'Successfully created directory: {newDir}')
        else:
            print(f'Directory {newDir} already exists')
        
        # Move all files with 'scores' in their name to the new scored directory
        for file in os.listdir(self.currentDir):
            if 'scores' in file:
                filePath = os.path.join(self.currentDir, file)
                shutil.move(filePath, newDir)
                print(f'Successfully moved {file} to {newDir}')

    def logConfig(self):
        
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

        # Get trial types
        trialTypes = self.getTrialType(df)

        # Subset data by trial type
        subsetList = self.subsetByTrial(df, trialTypes)

        return subsetList


class Scoring(Util):
    def __init__(self) -> None:
        super().__init__()

    def fsScore(self):

        # initialize scoring
        trialDfs = self.initScoring('FiguralSpeed')

        # create a list to store the results
        trialData = []

        # score each trial and add results to the list
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            pc = trial.iloc[:, 13].mean()
            responseTimes = trial.iloc[:, 14].mean()
            responseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = trial.iloc[:, 14].median()
            medianResponseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].median()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Total Inputs': trial.iloc[:, 13].count(),
                'Average Response Time': responseTimes,
                'Average Response Time (Correct)': responseCorrect,
                'Average Response Time (Incorrect)': responseIncorrect,
                'Median Response Time': medianResponseTime,
                'Median Response Time (Correct)': medianResponseCorrect,
                'Median Response Time (Incorrect)': medianResponseIncorrect
            })

        self.outputToCsv(trialData, 'fs_scores.csv')

    def luScore(self):

        # initialize scoring
        trialDfs = self.initScoring('LetterUpdating')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialName = trial.iloc[0, 4]
            pc = trial.iloc[:, 18].mean() / 3
            totalInputs = trial.iloc[:, 18].count()

            trialData.append({
                'Trial': trialName,
                'Proportion Correct': pc,
                'Total Inputs': totalInputs
            })

        self.outputToCsv(trialData, 'lu_scores.csv')

    def msScore(self):

        # initialize scoring
        trialDfs = self.initScoring('MotoricSpeed')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 5]
            pc = trial.iloc[:, 15].mean()
            totalInputs = trial.iloc[:, 13].count()
            responseTimes = trial.iloc[:, 14].mean()
            responseCorrect = trial[trial.iloc[:, 15] == 1].iloc[:, 14].mean()
            responseIncorrect = trial[trial.iloc[:, 15] == 0].iloc[:, 14].mean()
            medianResponseTime = trial.iloc[:, 14].median()
            medianResponseCorrect = trial[trial.iloc[:, 15] == 1].iloc[:, 14].median()
            medianResponseIncorrect = trial[trial.iloc[:, 15] == 0].iloc[:, 14].median()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Total Inputs': trial.iloc[:, 13].count(),
                'Average Response Time': responseTimes,
                'Average Response Time (Correct)': responseCorrect,
                'Average Response Time (Incorrect)': responseIncorrect,
                'Median Response Time': medianResponseTime,
                'Median Response Time (Correct)': medianResponseCorrect,
                'Median Response Time (Incorrect)': medianResponseIncorrect
            })

        self.outputToCsv(trialData, 'ms_scores.csv')

    def nmScore(self):

        # initialize scoring
        trialDfs = self.initScoring('NumberMemory')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            pc = trial.iloc[:, 10].mean()
            totalInputs = trial.iloc[:, 13].count()
            responseTimes = trial.iloc[:, 11].mean()
            responseCorrect = trial[trial.iloc[:, 10] == 1].iloc[:, 11].mean()
            responseIncorrect = trial[trial.iloc[:, 10] == 0].iloc[:, 11].mean()
            medianResponseTime = trial.iloc[:, 11].median()
            medianResponseCorrect = trial[trial.iloc[:, 10] == 1].iloc[:, 11].median()
            medianResponseIncorrect = trial[trial.iloc[:, 10] == 0].iloc[:, 11].median()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Total Inputs': totalInputs,
                'Average Response Time': responseTimes,
                'Average Response Time (Correct)': responseCorrect,
                'Average Response Time (Incorrect)': responseIncorrect,
                'Median Response Time': medianResponseTime,
                'Median Response Time (Correct)': medianResponseCorrect,
                'Median Response Time (Incorrect)': medianResponseIncorrect
            })

        self.outputToCsv(trialData, 'nm_scores.csv')

    # this test has a different trial format and the column is 6 instead of 5
    def nbScore(self):

        # initialize scoring
        trialDfs = self.initScoring('Numerical_nBack')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 5]
            pc = trial.iloc[:, 13].mean()
            totalCorrect = trial.iloc[:, 13].sum()
            totalInputs = trial.iloc[:, 13].count()
            responseTimes = trial.iloc[:, 14].mean()
            responseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = trial.iloc[:, 14].median()
            medianResponseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].median()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Total Correct': totalCorrect,
                'Total Inputs': totalInputs,
                'Average Response Time': responseTimes,
                'Average Response Time (Correct)': responseCorrect,
                'Average Response Time (Incorrect)': responseIncorrect,
                'Median Response Time': medianResponseTime,
                'Median Response Time (Correct)': medianResponseCorrect,
                'Median Response Time (Incorrect)': medianResponseIncorrect
            })

        self.outputToCsv(trialData, 'nb_scores.csv')

    def nsScore(self):
    
        # initialize scoring
        trialDfs = self.initScoring('NumericalSpeed')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            pc = trial.iloc[:, 13].mean()
            totalCorrect = trial.iloc[:, 13].sum()
            responseTimes = trial.iloc[:, 14].mean()
            responseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = trial.iloc[:, 14].median()
            medianResponseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].median()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Total Inputs': totalCorrect,
                'Average Response Time': responseTimes,
                'Average Response Time (Correct)': responseCorrect,
                'Average Response Time (Incorrect)': responseIncorrect,
                'Median Response Time': medianResponseTime,
                'Median Response Time (Correct)': medianResponseCorrect,
                'Median Response Time (Incorrect)': medianResponseIncorrect
            })

        self.outputToCsv(trialData, 'ns_scores.csv')

    def stScore(self):
    
        # initialize scoring
        trialDfs = self.initScoring('SpeedTabbing')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            numPresses = trial.iloc[:, 5].count()
            responseTimes = trial.iloc[:, 10].mean()
            medianResponseTime = trial.iloc[:, 10].median()
            firstPress = trial.iloc[0, 10]
            lastPress = trial.iloc[-1, 10]

            trialData.append({
                'Trial Type': trialType,
                'Total Number of Presses': numPresses,
                'Average Response Time': responseTimes,
                'Median Response Time': medianResponseTime,
                'First Press': firstPress,
                'Last Press': lastPress
            })

        self.outputToCsv(trialData, 'st_scores.csv')

    def vsScore(self):

        # initialize scoring
        trialDfs = self.initScoring('VerbalSpeed')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            pc = trial.iloc[:, 13].mean()
            responseTimes = trial.iloc[:, 14].mean()
            responseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].mean()
            responseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].mean()
            medianResponseTime = trial.iloc[:, 14].median()
            medianResponseCorrect = trial[trial.iloc[:, 13] == 1].iloc[:, 14].median()
            medianResponseIncorrect = trial[trial.iloc[:, 13] == 0].iloc[:, 14].median()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Average Response Time': responseTimes,
                'Average Response Time (Correct)': responseCorrect,
                'Average Response Time (Incorrect)': responseIncorrect,
                'Median Response Time': medianResponseTime,
                'Median Response Time (Correct)': medianResponseCorrect,
                'Median Response Time (Incorrect)': medianResponseIncorrect
            })

        self.outputToCsv(trialData, 'vs_scores.csv')

    def olmScore(self):

        # NOTE: consists of 6x6 grid of objects

        # initialize scoring
        trialDfs = self.initScoring('ObjectLocationMemory')
        
        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            pc = trial.iloc[:, 9].item()
            responseTimes = trial.iloc[:, 7].item()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Total Response Time': responseTimes
            })

        # Nitty gritty details
        # 1. Determine the original coordinates of the object
        # 2. Determine the coordinates of the object after the translation

        self.outputToCsv(trialData, 'olm_scores.csv')

    def suScore(self):
    
        # NOTE: consists of 3, 3x3 grids of objects

        # initialize scoring
        trialDfs = self.initScoring('SpatialUpdating')

        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            pcGrid1 = trial.iloc[:, 33].mean()
            pcGrid2 = trial.iloc[:, 34].mean()
            pcGrid3 = trial.iloc[:, 35].mean()
            pcTotal = trial.iloc[:, 36].mean()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct Grid 1': pcGrid1,
                'Proportion Correct Grid 2': pcGrid2,
                'Proportion Correct Grid 3': pcGrid3,
                'Proportion Correct Total': pcTotal
            })

        # Nitty gritty details
        # 1. Determine the original coordinates of the object
        # 2. Determine the coordinates of the object after the translation

        self.outputToCsv(trialData, 'su_scores.csv')

    def wrScore(self):

        # initialize scoring
        trialDfs = self.initScoring('WordRecall')
        
        # create an empty list to store trial data
        trialData = []

        # score each trial (this will be general scores)
        for trial in trialDfs:
            trialType = trial.iloc[0, 4]
            pc = trial.iloc[:, 24].item() / trial.iloc[:, 23].item()
            intrusions = trial.iloc[:, 25].item() / trial.iloc[:, 23].item()

            trialData.append({
                'Trial Type': trialType,
                'Proportion Correct': pc,
                'Proportion Intrusions': intrusions
            })

        self.outputToCsv(trialData, 'wr_scores.csv')

if __name__ == '__main__':
    # create a new instance of the class
    scoring = Scoring()

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
    scoring.makeScoredDir()

    # print a message to the console
    print('Done!')