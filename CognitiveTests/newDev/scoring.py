from util import Util
import numpy as np


class Scoring(Util):
    def __init__(self) -> None:
        super().__init__()

    def fsScore(self):

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
                'PC (Same)': 'NA',
                'PC (Different)': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',  
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Min_RT': 'NA',
                'Max_RT_C': 'NA',
                'Min_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT_I': 'NA',
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
                    'PC (Same)': pcSame,
                    'PC (Different)': pcDifferent,
                    'Trials': block.iloc[:, 13].count(),
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Min_RT_C': minResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'figSpd_sc')

    def luScore(self):
        
        # TODO: LU add mean streak length correct vs incorrect

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
                'Trials': 'NA',
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
                    'Trials': totalTrials
                })

        self.outputToFile(blockData, 'letUp_sc')

    def msScore(self):
        
        # TODO: MS sort errors by square

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
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Min_RT': 'NA',
                'Max_RT_C': 'NA',
                'Min_RT_C': 'NA',
                'Max_RT_I': 'NA',
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
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Min_RT_C': minResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'motSpd_sc')

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
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Min_RT': 'NA',
                'Max_RT_C': 'NA',
                'Min_RT_C': 'NA',
                'Max_RT_I': 'NA',
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
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Min_RT_C': minResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'numMem_sc')

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
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Min_RT': 'NA',
                'Max_RT_C': 'NA',
                'Min_RT_C': 'NA',
                'Max_RT_I': 'NA',
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
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Min_RT_C': minResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'numNB_sc')

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
                'PC (Same)': 'NA',
                'PC (Different)': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',  
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Min_RT': 'NA',
                'Max_RT_C': 'NA',
                'Min_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT_I': 'NA',
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
                    'PC (Same)': pcSame,
                    'PC (Different)': pcDifferent,
                    'Trials': totalCorrect,
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Min_RT_C': minResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'numSpd_sc')

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
                    'Med_RT': medianResponseTime,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'First_Press': firstPress,
                    'Last_Press': lastPress
                })

        self.outputToFile(blockData, 'spdTab_sc')

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
                'PC (Same)': 'NA',
                'PC (Different)': 'NA',
                'Trials': 'NA',
                'Mean_RT': 'NA',
                'Mean_RT_C': 'NA',
                'Mean_RT_I': 'NA',  
                'Med_RT': 'NA',
                'Med_RT_C': 'NA',
                'Med_RT_I': 'NA',
                'Max_RT': 'NA',
                'Min_RT': 'NA',
                'Max_RT_C': 'NA',
                'Min_RT_C': 'NA',
                'Max_RT_I': 'NA',
                'Min_RT_I': 'NA',
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
                    'PC (Same)': pcSame,
                    'PC (Different)': pcDifferent,
                    'Mean_RT': responseTimes,
                    'Mean_RT_C': responseCorrect,
                    'Mean_RT_I': responseIncorrect,
                    'Med_RT': medianResponseTime,
                    'Med_RT_C': medianResponseCorrect,
                    'Med_RT_I': medianResponseIncorrect,
                    'Max_RT': maxResponseTime,
                    'Min_RT': minResponseTime,
                    'Max_RT_C': maxResponseCorrect,
                    'Min_RT_C': minResponseCorrect,
                    'Max_RT_I': maxResponseIncorrect,
                    'Min_RT_I': minResponseIncorrect,
                    'Num_0': numZeroInputs
                })

        self.outputToFile(blockData, 'verbSpd_sc')

    def olmScore(self):

        # TODO: Add additional scoring methods (e.g. avg distance from correct block)
        # TODO: Add a matrix representation of the grid showing correct vs incorrect responses
        
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

    def suScore(self):
    
        # TODO: Check ED and CB calculations

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
                'CB_Grid_3': 'NA'
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
                    'CB_Grid_3': cellCB['3']
                })

        self.outputToFile(blockData, 'spatUp_sc')

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
                'Prop_Incorrect_No_Int)': 'NA'
            })

        else:

            # score each block (this will be general scores)
            for block in blockDfs:
                blockType = block.iloc[0, 4]
                pc = block.iloc[:, 24].item() / block.iloc[:, 23].item()
                intrusions = block.iloc[:, 25].item() / block.iloc[:, 23].item()
                # proportion incorrect (i.e., no intrusions)
                pi = (block.iloc[:, 23].item() - block.iloc[:, 24].item() - block.iloc[:, 25].item()) / block.iloc[:, 23].item() 
                blockData.append({
                    'ID': self.testID,
                    'Visit': self.currentVisit,
                    'Block': blockType,
                    'PC': pc,
                    'Prop_Intrusions': intrusions,
                    'Prop_Incorrect_No_Int)': pi
                })

        self.outputToFile(blockData, 'wrdRec_sc')