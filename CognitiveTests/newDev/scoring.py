from util import Util
import numpy as np
import pandas as pd


class Scoring(Util):
    def __init__(self) -> None:
        super().__init__()

    def fsScore(self):

        # WIDE FORMAT OUTPUT
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_FiguralSpeed')
        
        # create a list to store the results
        blockData = []

        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'PC_Same': 'NA',
                'PC_Different': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',  
                'Std_RT': 'NA',
                'Std_RT_C': 'NA',
                'Std_RT_I': 'NA',
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Max_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT': 'NA',
                'Min_RT_C': 'NA',
                'Min_RT_I': 'NA',
                'Mean_RT_Same': 'NA',
                'Mean_RT_Same_C': 'NA',
                'Mean_RT_Same_I': 'NA',
                'Mean_RT_Different': 'NA',
                'Mean_RT_Different_C': 'NA',
                'Mean_RT_Different_I': 'NA',
                'Std_RT_Same': 'NA',
                'Std_RT_Same_C': 'NA',
                'Std_RT_Same_I': 'NA',
                'Std_RT_Different': 'NA',
                'Std_RT_Different_C': 'NA',
                'Std_RT_Different_I': 'NA',
                'Med_RT_Same': 'NA',
                'Med_RT_Same_C': 'NA',
                'Med_RT_Same_I': 'NA',
                'Med_RT_Different': 'NA',
                'Med_RT_Different_C': 'NA',
                'Med_RT_Different_I': 'NA',
                'Max_RT_Same': 'NA',
                'Max_RT_Same_C': 'NA',
                'Max_RT_Same_I': 'NA',
                'Max_RT_Different': 'NA',
                'Max_RT_Different_C': 'NA',
                'Max_RT_Different_I': 'NA',
                'Min_RT_Same': 'NA',
                'Min_RT_Same_C': 'NA',
                'Min_RT_Same_I': 'NA',
                'Min_RT_Different': 'NA',
                'Min_RT_Different_C': 'NA',
                'Min_RT_Different_I': 'NA',
                'Num_0': 'NA'
            })

        else:
            
            # score each block and add results to the list
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                pc = block.iloc[:, 13].mean()
                pcSame = block[block.iloc[:, 8] == 1].iloc[:, 13].mean()
                pcDifferent = block[block.iloc[:, 8] == 2].iloc[:, 13].mean()
                responseTimes = block.iloc[:, 14].mean()
                responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
                responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
                stdResponseTimes = block.iloc[:, 14].std()
                stdResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].std()
                stdResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].std()
                medianResponseTime = block.iloc[:, 14].median()
                medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
                medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()
                maxResponseTime = block.iloc[:, 14].max()
                minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
                minResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
                minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                responseTimesSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].mean()
                responseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].mean()
                responseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].mean()
                responseTimesDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].mean()
                responseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].mean()
                responseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].mean()
                stdResponseTimesSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].std()
                stdResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].std()
                stdResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].std()
                stdResponseTimesDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].std()
                stdResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].std()
                stdResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].std()
                medianResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].median()
                medianResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].median()
                medianResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].median()
                medianResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].median()
                medianResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].median()
                medianResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].median()
                maxResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].max()
                maxResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].max()
                maxResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].max()
                maxResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].max()
                maxResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].max()
                maxResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].max()
                minResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
                
                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'PC_Same': pcSame,
                    'PC_Different': pcDifferent,
                    'Trials': block.iloc[:, 13].count(),
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Std_RT': stdResponseTimes,
                    'Std_RT_C': stdResponseCorrect,
                    'Std_RT_I': stdResponseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT': minResponseTime,
                    'Min_RT_C': minResponseCorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Mean_RT_Same': responseTimesSame,
                    'Mean_RT_Same_C': responseCorrectSame,
                    'Mean_RT_Same_I': responseIncorrectSame,
                    'Mean_RT_Different': responseTimesDifferent,
                    'Mean_RT_Different_C': responseCorrectDifferent,
                    'Mean_RT_Different_I': responseIncorrectDifferent,
                    'Std_RT_Same': stdResponseTimesSame,
                    'Std_RT_Same_C': stdResponseCorrectSame,
                    'Std_RT_Same_I': stdResponseIncorrectSame,
                    'Std_RT_Different': stdResponseTimesDifferent,
                    'Std_RT_Different_C': stdResponseCorrectDifferent,
                    'Std_RT_Different_I': stdResponseIncorrectDifferent,
                    'Med_RT_Same': medianResponseTimeSame,
                    'Med_RT_Same_C': medianResponseCorrectSame,
                    'Med_RT_Same_I': medianResponseIncorrectSame,
                    'Med_RT_Different': medianResponseTimeDifferent,
                    'Med_RT_Different_C': medianResponseCorrectDifferent,
                    'Med_RT_Different_I': medianResponseIncorrectDifferent,
                    'Max_RT_Same': maxResponseTimeSame,
                    'Max_RT_Same_C': maxResponseCorrectSame,
                    'Max_RT_Same_I': maxResponseIncorrectSame,
                    'Max_RT_Different': maxResponseTimeDifferent,
                    'Max_RT_Different_C': maxResponseCorrectDifferent,
                    'Max_RT_Different_I': maxResponseIncorrectDifferent,
                    'Min_RT_Same': minResponseTimeSame,
                    'Min_RT_Same_C': minResponseCorrectSame,
                    'Min_RT_Same_I': minResponseIncorrectSame,
                    'Min_RT_Different': minResponseTimeDifferent,
                    'Min_RT_Different_C': minResponseCorrectDifferent,
                    'Min_RT_Different_I': minResponseIncorrectDifferent,
                    'Num_0': numZeroInputs
                })
                
        self.outputToFile(blockData, 'figSpd_sc')
        
    def fsScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_FiguralSpeed')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Trial_Num': 'NA',
                'Same_Diff': 'NA',
                'Stimuli_1': 'NA',
                'Stimuli_2': 'NA',
                'Correct': 'NA',
                'Response': 'NA',
                'Accuracy': 'NA',
                'RT': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 6, 7, 15, 16, 17, 18, 19, 20]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Trial_Num', 'Same_Diff', 'Stimuli_1', 'Stimuli_2', 'Correct', 'Response', 'Accuracy', 'RT']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'figSpd_sc_long')
        
    def luScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_LetterUpdating')

        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'Mean_Streak': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA'
            })

        else:
            
            # score each block (this will be general scores)
            for block in blockDfs:
                blockName = block.iloc[0, 4]
                pc = block.iloc[:, 18].mean() / 3
                totalTrials = block.iloc[:, 18].count()
                
                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockName,
                    'PC': pc,
                    'Trials': totalTrials,
                    'Mean_RT': 'NA'
                })

        self.outputToFile(blockData, 'letUp_sc')
    
    def luScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_LetterUpdating')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Correct_1': 'NA',
                'Correct_2': 'NA',
                'Correct_3': 'NA',
                'Response_1': 'NA',
                'Response_2': 'NA',
                'Response_3': 'NA',
                'Accuracy_1': 'NA',
                'Accuracy_2': 'NA',
                'Accuracy_3': 'NA',
                'Prop_Correct': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 5, 6, 7, 8, 19, 20, 21, 22, 23, 24]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Correct_1', 'Correct_2', 'Correct_3', 'Response_1', 'Response_2', 'Response_3', 'Accuracy_1', 'Accuracy_2', 'Accuracy_3', 'Prop_Correct']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'letUp_sc_long')

    def msScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_MotoricSpeed')

        # create an empty list to store block data
        blockData = []

                # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',
                'Std_RT': 'NA',
                'Std_RT_C': 'NA',
                'Std_RT_I': 'NA',
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Max_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT': 'NA',
                'Min_RT_C': 'NA',
                'Min_RT_I': 'NA',
                'Num_0': 'NA'
            })
        
        else:
            
            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 5]
                pc = block.iloc[:, 15].mean()
                totalTrials = block.iloc[:, 13].count()
                responseTimes = block.iloc[:, 14].mean()
                responseCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].mean()
                responseIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].mean()
                stdResponseTimes = block.iloc[:, 14].std()
                stdResponseCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].std()
                stdResponseIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].std()
                medianResponseTime = block.iloc[:, 14].median()
                medianResponseCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].median()
                medianResponseIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].median()
                maxResponseTime = block.iloc[:, 14].max()
                minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].max()
                minResponseCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].max()
                minResponseIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()

                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'Trials': totalTrials,
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Std_RT': stdResponseTimes,
                    'Std_RT_C': stdResponseCorrect,
                    'Std_RT_I': stdResponseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT': minResponseTime,
                    'Min_RT_C': minResponseCorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'motSpd_sc')
        
    def msScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_MotoricSpeed')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Trial_Num': 'NA',
                'Position_Darkened': 'NA',
                'Correct_Input': 'NA',
                'Position_Response': 'NA',
                'Response_Input': 'NA',
                'RT': 'NA',
                'Accuracy': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 4, 6, 7, 8, 16, 17, 18, 19, 20, 21]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Trial_Num', 'Position_Darkened', 'Correct_Input', 'Position_Response', 'Response_Input', 'RT', 'Accuracy']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'motSpd_sc_long')

    def nmScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_NumberMemory')

        # create an empty list to store block data
        blockData = []

        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',  
                'Std_RT': 'NA',
                'Std_RT_C': 'NA',
                'Std_RT_I': 'NA',
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Max_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT': 'NA',
                'Min_RT_C': 'NA',
                'Min_RT_I': 'NA',
                'Num_0': 'NA'
            })
            
        else:
            
            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                pc = block.iloc[:, 10].mean()
                totalTrials = block.iloc[:, 13].count()
                responseTimes = block.iloc[:, 11].mean()
                responseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11].mean()
                responseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11].mean()
                stdResponseTimes = block.iloc[:, 11].std()
                stdResponseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11].std()
                stdResponseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11].std()
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
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'Trials': totalTrials,
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Std_RT': stdResponseTimes,
                    'Std_RT_C': stdResponseCorrect,
                    'Std_RT_I': stdResponseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT': minResponseTime,
                    'Min_RT_C': minResponseCorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'numMem_sc')

    def nmScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_NumberMemory')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Correct_Input': 'NA',
                'Stimulus': 'NA',
                'Response_Input': 'NA',
                'Accuracy': 'NA',
                'RT': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 5, 6, 12, 13, 14, 15, 16, 17]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Correct_Input', 'Stimulus', 'Response_Input', 'Accuracy', 'RT']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'numMem_sc_long')

    # this test has a different block format and the column is 6 instead of 5
    def nbScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_Numerical_nBack')

        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',  
                'Std_RT': 'NA',
                'Std_RT_C': 'NA',
                'Std_RT_I': 'NA',
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Max_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT': 'NA',
                'Min_RT_C': 'NA',
                'Min_RT_I': 'NA',
                'Num_0': 'NA'
            })

        else:
            
            # score each block (this will be general scores)
            for block in blockDfs:
                # remove the first three rows, as they are not part of the test
                block = block.iloc[3:]
                blockType = block.iloc[0, 5]
                pc = block.iloc[:, 13].mean()
                totalCorrect = block.iloc[:, 13].sum()
                totalTrials = block.iloc[:, 13].count()
                responseTimes = block.iloc[:, 14].mean()
                responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
                responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
                stdResponseTimes = block.iloc[:, 14].std()
                stdResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].std()
                stdResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].std()
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
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'Total Correct': totalCorrect,
                    'Trials': totalTrials,
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Std_RT': stdResponseTimes,
                    'Std_RT_C': stdResponseCorrect,
                    'Std_RT_I': stdResponseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT': minResponseTime,
                    'Min_RT_C': minResponseCorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'numNB_sc')
        
    def nbScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_Numerical_nBack')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Trial_Num': 'NA',
                'Stimuli': 'NA',
                'Correct_Input': 'NA',
                'Response_Input': 'NA',
                'Accuracy': 'NA',
                'RT': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 4, 7, 8, 9, 15, 16, 17, 18, 19, 20]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Trial_Num', 'Stimuli', 'Correct_Input', 'Response_Input', 'Accuracy', 'RT']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'numNB_sc_long')

    def nsScore(self):
    
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_NumericalSpeed')
        
        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'PC_Same': 'NA',
                'PC_Different': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',
                'Std_RT': 'NA',
                'Std_RT_C': 'NA',
                'Std_RT_I': 'NA',
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Max_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT': 'NA',
                'Min_RT_C': 'NA',
                'Min_RT_I': 'NA',
                'Mean_RT_Same': 'NA',
                'Mean_RT_Same_C': 'NA',
                'Mean_RT_Same_I': 'NA',
                'Mean_RT_Different': 'NA',
                'Mean_RT_Different_C': 'NA',
                'Mean_RT_Different_I': 'NA',
                'Std_RT_Same': 'NA',
                'Std_RT_Same_C': 'NA',
                'Std_RT_Same_I': 'NA',
                'Std_RT_Different': 'NA',
                'Std_RT_Different_C': 'NA',
                'Std_RT_Different_I': 'NA',
                'Med_RT_Same': 'NA',
                'Med_RT_Same_C': 'NA',
                'Med_RT_Same_I': 'NA',
                'Med_RT_Different': 'NA',
                'Med_RT_Different_C': 'NA',
                'Med_RT_Different_I': 'NA',
                'Max_RT_Same': 'NA',
                'Max_RT_Same_C': 'NA',
                'Max_RT_Same_I': 'NA',
                'Max_RT_Different': 'NA',
                'Max_RT_Different_C': 'NA',
                'Max_RT_Different_I': 'NA',
                'Min_RT_Same': 'NA',
                'Min_RT_Same_C': 'NA',
                'Min_RT_Same_I': 'NA',
                'Min_RT_Different': 'NA',
                'Min_RT_Different_C': 'NA',
                'Min_RT_Different_I': 'NA',
                'Num_0': 'NA'
            })

        else:
            
            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                pc = block.iloc[:, 13].mean()
                pcSame = block[block.iloc[:, 8] == 1].iloc[:, 13].mean()
                pcDifferent = block[block.iloc[:, 8] == 2].iloc[:, 13].mean()
                totalCorrect = block.iloc[:, 13].sum()
                # Don't include 0s in response time calculation
                responseTimes = block.iloc[:, 14].mean()
                responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
                responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
                stdResponseTimes = block.iloc[:, 14].std()
                stdResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].std()
                stdResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].std()
                medianResponseTime = block.iloc[:, 14].median()
                medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
                medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()
                maxResponseTime = block.iloc[:, 14].max()
                minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
                minResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
                minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                responseTimesSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].mean()
                responseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].mean()
                responseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].mean()
                responseTimesDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].mean()
                responseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].mean()
                responseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].mean()
                stdResponseTimesSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].std()
                stdResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].std()
                stdResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].std()
                stdResponseTimesDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].std()
                stdResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].std()
                stdResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].std()
                medianResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].median()
                medianResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].median()
                medianResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].median()
                medianResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].median()
                medianResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].median()
                medianResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].median()
                maxResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].max()
                maxResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].max()
                maxResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].max()
                maxResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].max()
                maxResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].max()
                maxResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].max()
                minResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()

                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'PC_Same': pcSame,
                    'PC_Different': pcDifferent,
                    'Trials': totalCorrect,
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Std_RT': stdResponseTimes,
                    'Std_RT_C': stdResponseCorrect,
                    'Std_RT_I': stdResponseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT': minResponseTime,
                    'Min_RT_C': minResponseCorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Mean_RT_Same': responseTimesSame,
                    'Mean_RT_Same_C': responseCorrectSame,
                    'Mean_RT_Same_I': responseIncorrectSame,
                    'Mean_RT_Different': responseTimesDifferent,
                    'Mean_RT_Different_C': responseCorrectDifferent,
                    'Mean_RT_Different_I': responseIncorrectDifferent,
                    'Std_RT_Same': stdResponseTimesSame,
                    'Std_RT_Same_C': stdResponseCorrectSame,
                    'Std_RT_Same_I': stdResponseIncorrectSame,
                    'Std_RT_Different': stdResponseTimesDifferent,
                    'Std_RT_Different_C': stdResponseCorrectDifferent,
                    'Std_RT_Different_I': stdResponseIncorrectDifferent,
                    'Med_RT_Same': medianResponseTimeSame,
                    'Med_RT_Same_C': medianResponseCorrectSame,
                    'Med_RT_Same_I': medianResponseIncorrectSame,
                    'Med_RT_Different': medianResponseTimeDifferent,
                    'Med_RT_Different_C': medianResponseCorrectDifferent,
                    'Med_RT_Different_I': medianResponseIncorrectDifferent,
                    'Max_RT_Same': maxResponseTimeSame,
                    'Max_RT_Same_C': maxResponseCorrectSame,
                    'Max_RT_Same_I': maxResponseIncorrectSame,
                    'Max_RT_Different': maxResponseTimeDifferent,
                    'Max_RT_Different_C': maxResponseCorrectDifferent,
                    'Max_RT_Different_I': maxResponseIncorrectDifferent,
                    'Min_RT_Same': minResponseTimeSame,
                    'Min_RT_Same_C': minResponseCorrectSame,
                    'Min_RT_Same_I': minResponseIncorrectSame,
                    'Min_RT_Different': minResponseTimeDifferent,
                    'Min_RT_Different_C': minResponseCorrectDifferent,
                    'Min_RT_Different_I': minResponseIncorrectDifferent,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'numSpd_sc')
        
    def nsScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_NumericalSpeed')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Trial_Num': 'NA',
                'Same_Diff': 'NA',
                'Stimuli_1': 'NA',
                'Stimuli_2': 'NA',
                'Correct_Input': 'NA',
                'Response_Input': 'NA',
                'Accuracy': 'NA',
                'RT': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 6, 7, 15, 16, 7, 17, 18, 19, 20]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Trial_Num', 'Same_Diff', 'Stimuli_1', 'Stimuli_2', 'Correct_Input', 'Response_Input', 'Accuracy', 'RT']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'numSpd_sc_long')

    def stScore(self):
    
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_SpeedTabbing')
        
        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Std_RT': 'NA',
                'Med_RT': 'NA',
                'Max_RT': 'NA',
                'Min_RT': 'NA',
                'First_Press': 'NA',
                'Last_Press': 'NA',
            })

        else:

            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                numPresses = block.iloc[:, 5].count()
                responseTimes = block.iloc[:, 10].mean()
                stdResponseTimes = block.iloc[:, 10].std()
                medianResponseTime = block.iloc[:, 10].median()
                maxResponseTime = block.iloc[:, 10].max()
                minResponseTime = block.iloc[:, 10][block.iloc[:, 10] >= 200].min()
                firstPress = block.iloc[0, 10]
                lastPress = block.iloc[-1, 10]

                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'Presses': numPresses,
                    'Mean_RT': responseTimes,
                    'Std_RT': stdResponseTimes,
                    'Med_RT': medianResponseTime,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'First_Press': firstPress,
                    'Last_Press': lastPress
                })

        self.outputToFile(blockData, 'spdTab_sc')

    def stScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_SpeedTabbing')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Presses': 'NA',
                'RT': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Presses', 'RT']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'spdTab_sc_long')
        
    def vsScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_VerbalSpeed')
        
        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'PC_Same': 'NA',
                'PC_Different': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',
                'Std_RT': 'NA',
                'Std_RT_C': 'NA',
                'Std_RT_I': 'NA', 
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Max_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT': 'NA',
                'Min_RT_C': 'NA',
                'Min_RT_I': 'NA',
                'Mean_RT_Same': 'NA',
                'Mean_RT_Same_C': 'NA',
                'Mean_RT_Same_I': 'NA',
                'Mean_RT_Different': 'NA',
                'Mean_RT_Different_C': 'NA',
                'Mean_RT_Different_I': 'NA',
                'Std_RT_Same': 'NA',
                'Std_RT_Same_C': 'NA',
                'Std_RT_Same_I': 'NA',
                'Std_RT_Different': 'NA',
                'Std_RT_Different_C': 'NA',
                'Std_RT_Different_I': 'NA',
                'Med_RT_Same': 'NA',
                'Med_RT_Same_C': 'NA',
                'Med_RT_Same_I': 'NA',
                'Med_RT_Different': 'NA',
                'Med_RT_Different_C': 'NA',
                'Med_RT_Different_I': 'NA',
                'Max_RT_Same': 'NA',
                'Max_RT_Same_C': 'NA',
                'Max_RT_Same_I': 'NA',
                'Max_RT_Different': 'NA',
                'Max_RT_Different_C': 'NA',
                'Max_RT_Different_I': 'NA',
                'Min_RT_Same': 'NA',
                'Min_RT_Same_C': 'NA',
                'Min_RT_Same_I': 'NA',
                'Min_RT_Different': 'NA',
                'Min_RT_Different_C': 'NA',
                'Min_RT_Different_I': 'NA',
                'Num_0': 'NA'
            })

        else:

            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                pc = block.iloc[:, 13].mean()
                pcSame = block[block.iloc[:, 8] == 1].iloc[:, 13].mean()
                pcDifferent = block[block.iloc[:, 8] == 2].iloc[:, 13].mean()
                responseTimes = block.iloc[:, 14].mean()
                responseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].mean()
                responseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].mean()
                stdResponseTimes = block.iloc[:, 14].std()
                stdResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].std()
                stdResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].std()
                medianResponseTime = block.iloc[:, 14].median()
                medianResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].median()
                medianResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].median()
                maxResponseTime = block.iloc[:, 14].max()
                minResponseTime = block.iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
                minResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
                minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                responseTimesSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].mean()
                responseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].mean()
                responseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].mean()
                responseTimesDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].mean()
                responseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].mean()
                responseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].mean()
                stdResponseTimesSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].std()
                stdResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].std()
                stdResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].std()
                stdResponseTimesDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].std()
                stdResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].std()
                stdResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].std()
                medianResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].median()
                medianResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].median()
                medianResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].median()
                medianResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].median()
                medianResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].median()
                medianResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].median()
                maxResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14].max()
                maxResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14].max()
                maxResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14].max()
                maxResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14].max()
                maxResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14].max()
                maxResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14].max()
                minResponseTimeSame = block.loc[block.iloc[:, 8] == 1, :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseCorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 1), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseIncorrectSame = block.loc[(block.iloc[:, 8] == 1) & (block.iloc[:, 13] == 0), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseTimeDifferent = block.loc[block.iloc[:, 8] == 2, :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseCorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 1), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                minResponseIncorrectDifferent = block.loc[(block.iloc[:, 8] == 2) & (block.iloc[:, 13] == 0), :].iloc[:, 14][block.iloc[:, 14] >= 200].min()
                numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
                
                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'PC_Same': pcSame,
                    'PC_Different': pcDifferent,
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Std_RT': stdResponseTimes,
                    'Std_RT_C': stdResponseCorrect,
                    'Std_RT_I': stdResponseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT': minResponseTime,
                    'Min_RT_C': minResponseCorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Mean_RT_Same': responseTimesSame,
                    'Mean_RT_Same_C': responseCorrectSame,
                    'Mean_RT_Same_I': responseIncorrectSame,
                    'Mean_RT_Different': responseTimesDifferent,
                    'Mean_RT_Different_C': responseCorrectDifferent,
                    'Mean_RT_Different_I': responseIncorrectDifferent,
                    'Std_RT_Same': stdResponseTimesSame,
                    'Std_RT_Same_C': stdResponseCorrectSame,
                    'Std_RT_Same_I': stdResponseIncorrectSame,
                    'Std_RT_Different': stdResponseTimesDifferent,
                    'Std_RT_Different_C': stdResponseCorrectDifferent,
                    'Std_RT_Different_I': stdResponseIncorrectDifferent,
                    'Med_RT_Same': medianResponseTimeSame,
                    'Med_RT_Same_C': medianResponseCorrectSame,
                    'Med_RT_Same_I': medianResponseIncorrectSame,
                    'Med_RT_Different': medianResponseTimeDifferent,
                    'Med_RT_Different_C': medianResponseCorrectDifferent,
                    'Med_RT_Different_I': medianResponseIncorrectDifferent,
                    'Max_RT_Same': maxResponseTimeSame,
                    'Max_RT_Same_C': maxResponseCorrectSame,
                    'Max_RT_Same_I': maxResponseIncorrectSame,
                    'Max_RT_Different': maxResponseTimeDifferent,
                    'Max_RT_Different_C': maxResponseCorrectDifferent,
                    'Max_RT_Different_I': maxResponseIncorrectDifferent,
                    'Min_RT_Same': minResponseTimeSame,
                    'Min_RT_Same_C': minResponseCorrectSame,
                    'Min_RT_Same_I': minResponseIncorrectSame,
                    'Min_RT_Different': minResponseTimeDifferent,
                    'Min_RT_Different_C': minResponseCorrectDifferent,
                    'Min_RT_Different_I': minResponseIncorrectDifferent,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'verbSpd_sc')

    def vsScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_VerbalSpeed')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Trial_Num': 'NA',
                'Same_Diff': 'NA',
                'Stimuli_1': 'NA',
                'Stimuli_2': 'NA',
                'Correct_Input': 'NA',
                'Response_Input': 'NA',
                'Accuracy': 'NA',
                'RT': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 6, 7, 15, 16, 17, 18, 19, 20]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Trial_Num', 'Same_Diff', 'Stimuli_1', 'Stimuli_2', 'Correct_Input', 'Response_Input', 'Accuracy', 'RT']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'verbSpd_sc_long')

    def olmScore(self):
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_ObjectLocationMemory')
        
        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'Total_RT': 'NA',
                'Mean_ED': 'NA',
                'Mean_CB': 'NA',
                'ED_1': 'NA',
                'ED_2': 'NA',
                'ED_3': 'NA',
                'ED_4': 'NA',
                'ED_5': 'NA',
                'ED_6': 'NA',
                'ED_7': 'NA',
                'ED_8': 'NA',
                'ED_9': 'NA',
                'ED_10': 'NA',
                'ED_11': 'NA',
                'ED_12': 'NA',
                'CB_1': 'NA',
                'CB_2': 'NA',
                'CB_3': 'NA',
                'CB_4': 'NA',
                'CB_5': 'NA',
                'CB_6': 'NA',
                'CB_7': 'NA',
                'CB_8': 'NA',
                'CB_9': 'NA',
                'CB_10': 'NA',
                'CB_11': 'NA',
                'CB_12': 'NA'
            })

        else:

            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                pc = block.iloc[:, 9].item() / 12
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
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'Total_RT': responseTimes,
                    'Mean_ED': meanEuclideanDist,
                    'Mean_CB': meanCityBlockDist,
                    'ED_1': cellDistancesEuclidean['1'],
                    'ED_2': cellDistancesEuclidean['2'],
                    'ED_3': cellDistancesEuclidean['3'],
                    'ED_4': cellDistancesEuclidean['4'],
                    'ED_5': cellDistancesEuclidean['5'],
                    'ED_6': cellDistancesEuclidean['6'],
                    'ED_7': cellDistancesEuclidean['7'],
                    'ED_8': cellDistancesEuclidean['8'],
                    'ED_9': cellDistancesEuclidean['9'],
                    'ED_10': cellDistancesEuclidean['10'],
                    'ED_11': cellDistancesEuclidean['11'],
                    'ED_12': cellDistancesEuclidean['12'],
                    'CB_1': cellDistancesCityBlock['1'],
                    'CB_2': cellDistancesCityBlock['2'],
                    'CB_3': cellDistancesCityBlock['3'],
                    'CB_4': cellDistancesCityBlock['4'],
                    'CB_5': cellDistancesCityBlock['5'],
                    'CB_6': cellDistancesCityBlock['6'],
                    'CB_7': cellDistancesCityBlock['7'],
                    'CB_8': cellDistancesCityBlock['8'],
                    'CB_9': cellDistancesCityBlock['9'],
                    'CB_10': cellDistancesCityBlock['10'],
                    'CB_11': cellDistancesCityBlock['11'],
                    'CB_12': cellDistancesCityBlock['12']
                })

        self.outputToFile(blockData, 'objLocMem_sc')

    def olmScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_ObjectLocationMemory')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'RT': 'NA',
                'Total_Possible': 'NA',
                'Prop_Correct': 'NA',
                'Num_Stimuli_1': 'NA',
                'Row_Coord_Stimuli_1': 'NA',
                'Col_Coord_Stimuli_1': 'NA',
                'Accuracy_Stimuli_1': 'NA',
                'Num_Stimuli_2': 'NA',
                'Row_Coord_Stimuli_2': 'NA',
                'Col_Coord_Stimuli_2': 'NA',
                'Accuracy_Stimuli_2': 'NA',
                'Num_Stimuli_3': 'NA',
                'Row_Coord_Stimuli_3': 'NA',
                'Col_Coord_Stimuli_3': 'NA',
                'Accuracy_Stimuli_3': 'NA',
                'Num_Stimuli_4': 'NA',
                'Row_Coord_Stimuli_4': 'NA',
                'Col_Coord_Stimuli_4': 'NA',
                'Accuracy_Stimuli_4': 'NA',
                'Num_Stimuli_5': 'NA',
                'Row_Coord_Stimuli_5': 'NA',
                'Col_Coord_Stimuli_5': 'NA',
                'Accuracy_Stimuli_5': 'NA',
                'Num_Stimuli_6': 'NA',
                'Row_Coord_Stimuli_6': 'NA',
                'Col_Coord_Stimuli_6': 'NA',
                'Accuracy_Stimuli_6': 'NA',
                'Num_Stimuli_7': 'NA',
                'Row_Coord_Stimuli_7': 'NA',
                'Col_Coord_Stimuli_7': 'NA',
                'Accuracy_Stimuli_7': 'NA',
                'Num_Stimuli_8': 'NA',
                'Row_Coord_Stimuli_8': 'NA',
                'Col_Coord_Stimuli_8': 'NA',
                'Accuracy_Stimuli_8': 'NA',
                'Num_Stimuli_9': 'NA',
                'Row_Coord_Stimuli_9': 'NA',
                'Col_Coord_Stimuli_9': 'NA',
                'Accuracy_Stimuli_9': 'NA',
                'Num_Stimuli_10': 'NA',
                'Row_Coord_Stimuli_10': 'NA',
                'Col_Coord_Stimuli_10': 'NA',
                'Accuracy_Stimuli_10': 'NA',
                'Num_Stimuli_11': 'NA',
                'Row_Coord_Stimuli_11': 'NA',
                'Col_Coord_Stimuli_11': 'NA',
                'Accuracy_Stimuli_11': 'NA',
                'Num_Stimuli_12': 'NA',
                'Row_Coord_Stimuli_12': 'NA',
                'Col_Coord_Stimuli_12': 'NA',
                'Accuracy_Stimuli_12': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete columns 10 to 63, columns
            blockDfs.drop(blockDfs.columns[10:60], axis=1, inplace=True)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 5, 6]], axis=1, inplace=True)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59, 64, 65, 66, 67, 68, 69]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'RT', 'Total_Possible', 'Prop_Correct', 
                                'Num_Stimuli_1', 'Row_Coord_Stimuli_1', 'Col_Coord_Stimuli_1', 'Accuracy_Stimuli_1', 
                                'Num_Stimuli_2', 'Row_Coord_Stimuli_2', 'Col_Coord_Stimuli_2', 'Accuracy_Stimuli_2',
                                'Num_Stimuli_3', 'Row_Coord_Stimuli_3', 'Col_Coord_Stimuli_3', 'Accuracy_Stimuli_3',
                                'Num_Stimuli_4', 'Row_Coord_Stimuli_4', 'Col_Coord_Stimuli_4', 'Accuracy_Stimuli_4',
                                'Num_Stimuli_5', 'Row_Coord_Stimuli_5', 'Col_Coord_Stimuli_5', 'Accuracy_Stimuli_5',
                                'Num_Stimuli_6', 'Row_Coord_Stimuli_6', 'Col_Coord_Stimuli_6', 'Accuracy_Stimuli_6',
                                'Num_Stimuli_7', 'Row_Coord_Stimuli_7', 'Col_Coord_Stimuli_7', 'Accuracy_Stimuli_7',
                                'Num_Stimuli_8', 'Row_Coord_Stimuli_8', 'Col_Coord_Stimuli_8', 'Accuracy_Stimuli_8',
                                'Num_Stimuli_9', 'Row_Coord_Stimuli_9', 'Col_Coord_Stimuli_9', 'Accuracy_Stimuli_9',
                                'Num_Stimuli_10', 'Row_Coord_Stimuli_10', 'Col_Coord_Stimuli_10', 'Accuracy_Stimuli_10',
                                'Num_Stimuli_11', 'Row_Coord_Stimuli_11', 'Col_Coord_Stimuli_11', 'Accuracy_Stimuli_11',
                                'Num_Stimuli_12', 'Row_Coord_Stimuli_12', 'Col_Coord_Stimuli_12', 'Accuracy_Stimuli_12']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'objLocMem_sc_long')

    def suScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_SpatialUpdating')
        
        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append    ({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC_Grid_1': 'NA',
                'PC_Grid_2': 'NA',
                'PC_Grid_3': 'NA',
                'PC_Total': 'NA',
                'ED_Grid_1': 'NA',
                'ED_Grid_2': 'NA',
                'ED_Grid_3': 'NA',
                'CB_Grid_1': 'NA',
                'CB_Grid_2': 'NA',
                'CB_Grid_3': 'NA',
                'Mean_RT': 'NA'
            })

        else:

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
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC_Grid_1': pcGrid1,
                    'PC_Grid_2': pcGrid2,
                    'PC_Grid_3': pcGrid3,
                    'PC_Total': pcTotal,
                    'ED_Grid_1': cellED['1'],
                    'ED_Grid_2': cellED['2'],
                    'ED_Grid_3': cellED['3'],
                    'CB_Grid_1': cellCB['1'],
                    'CB_Grid_2': cellCB['2'],
                    'CB_Grid_3': cellCB['3'],
                    'Mean_RT': 'NA'
                })

        self.outputToFile(blockData, 'spatUp_sc')

    def suScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_SpatialUpdating')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Trial_Num': 'NA',
                'Begin_Grid_1': 'NA',
                'Begin_Grid_2': 'NA',
                'Begin_Grid_3': 'NA',
                'First_Movement_Grid_1': 'NA',
                'First_Movement_Grid_2': 'NA',
                'First_Movement_Grid_3': 'NA',
                'Second_Movement_Grid_1': 'NA',
                'Second_Movement_Grid_2': 'NA',
                'Second_Movement_Grid_3': 'NA',
                'Final_Grid_1': 'NA',
                'Final_Grid_2': 'NA',
                'Final_Grid_3': 'NA',
                'Response_Grid_1': 'NA',
                'Response_Grid_2': 'NA',
                'Response_Grid_3': 'NA',
                'Accuracy_Grid_1': 'NA',
                'Accuracy_Grid_2': 'NA',
                'Accuracy_Grid_3': 'NA',
                'Accuracy_Entire_Trial': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 6, 7, 8, 9, 11, 13, 21, 23, 25, 27, 29, 31, 37, 38, 39, 40, 41, 42]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Trial_Num', 'Begin_Grid_1', 'Begin_Grid_2', 'Begin_Grid_3', 'First_Movement_Grid_1', 'First_Movement_Grid_2',
                                'First_Movement_Grid_3', 'Second_Movement_Grid_1', 'Second_Movement_Grid_2', 'Second_Movement_Grid_3', 'Final_Grid_1', 
                                'Final_Grid_2', 'Final_Grid_3', 'Response_Grid_1', 'Response_Grid_2', 'Response_Grid_3', 'Accuracy_Grid_1', 'Accuracy_Grid_2', 
                                'Accuracy_Grid_3', 'Accuracy_Entire_Trial']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'spatUp_sc_long')
        
    def wrScore(self):

        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_WordRecall')
        
        # create an empty list to store block data
        blockData = []
        
        # check if file was found, if not found, output the same file but with NA values
        if blockDfs is None:
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'PC': 'NA',
                'Prop_Intrusions': 'NA',
                'Prop_Incorrect_No_Int': 'NA',
                'Mean_RT': 'NA'
            })

        else:

            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                pc_attempted = block.iloc[:, 24].item() / block.iloc[:, 23].item()
                pc_possible = block.iloc[:, 24].item() / 16
                intrusions = block.iloc[:, 25].item() / block.iloc[:, 23].item()
                # proportion incorrect (i.e., no intrusions)
                pi = (block.iloc[:, 23].item() - block.iloc[:, 24].item() - block.iloc[:, 25].item()) / block.iloc[:, 23].item() 
                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC_Attempted': pc_attempted,
                    'PC_Total': pc_possible,
                    'Prop_Intrusions': intrusions,
                    'Prop_Incorrect_No_Int': pi,
                    'Mean_RT': 'NA'
                })

        self.outputToFile(blockData, 'wrdRec_sc')
        
    def wrScore_long(self):
        
        # LONG FORMAT OUTPUT
        # This will be a slightly truncated version of the original file, with only the most important columns
        
        # initialize scoring
        blockDfs = self.initScoring(f'{self.testID}_WordRecall')
        
        # If the file was not found, return None
        # Then output a file with NA values
        if blockDfs is None:
            blockData = []
            blockData.append({
                'ID': self.testID,
                'Visit': self.currentVisit,
                'Block': 'NA',
                'Stimuli_1': 'NA',
                'Stimuli_2': 'NA',
                'Stimuli_3': 'NA',
                'Stimuli_4': 'NA',
                'Stimuli_5': 'NA',
                'Stimuli_6': 'NA',
                'Stimuli_7': 'NA',
                'Stimuli_8': 'NA',
                'Stimuli_9': 'NA',
                'Stimuli_10': 'NA',
                'Stimuli_11': 'NA',
                'Stimuli_12': 'NA',
                'Stimuli_13': 'NA',
                'Stimuli_14': 'NA',
                'Stimuli_15': 'NA',
                'Stimuli_16': 'NA',
                'Num_Responses': 'NA',
                'Num_Correct': 'NA',
                'Num_Intrusions': 'NA'
            })
            
            blockDfs = pd.DataFrame(blockData)
        
        else:
        
            # Turn the initial file into a pandas dataframe
            blockDfs = pd.concat(blockDfs)
            
            # Delete unnecessary columns
            blockDfs = blockDfs.iloc[:, :26]
            blockDfs.drop(blockDfs.columns[[1, 2, 3, 5, 6]], axis=1, inplace=True)
            
            # Label columns
            blockDfs.columns = ['ID', 'Block', 'Stimuli_1', 'Stimuli_2', 'Stimuli_3', 'Stimuli_4', 'Stimuli_5', 'Stimuli_6', 
                                'Stimuli_7', 'Stimuli_8', 'Stimuli_9', 'Stimuli_10', 'Stimuli_11', 'Stimuli_12', 'Stimuli_13', 
                                'Stimuli_14', 'Stimuli_15', 'Stimuli_16', 'Num_Responses', 'Num_Correct', 'Num_Intrusions']
            
            # Add visit number as the second column
            blockDfs.insert(1, 'Visit', self.currentVisit)
        
        # output to file
        self.outputToFile(blockDfs, 'wrdRec_sc_long')