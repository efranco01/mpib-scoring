import pandas as pd
from util import Util

class Scoring(Util):
    def __init__(self) -> None:
        super().__init__()

    def fsScore(self):
        
        # TODO: Give maximum and minimum response times per block (not including 0s)

        # initialize scoring
        blockDfs = self.initScoring('FiguralSpeed')

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
            minResponseTime = block.iloc[:, 14].min()
            maxResponseTimeCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponseTimeCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].min()
            maxResponseTimeIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseTimeIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
            
            blockData.append({
                'ID': self.getTestID(),
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

        # initialize scoring
        blockDfs = self.initScoring('LetterUpdating')
        
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
                'ID': self.getTestID(),
                'Block': blockName,
                'PC': pc,
                'Trials': totalTrials
            })

        self.outputToFile(blockData, 'letUp_sc')

    def msScore(self):

        # initialize scoring
        blockDfs = self.initScoring('MotoricSpeed')
        
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
            minResponseTime = block.iloc[:, 14].min()
            maxResponseTimeCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].max()
            minResponseTimeCorrect = block[block.iloc[:, 15] == 1].iloc[:, 14].min()
            maxResponseTimeIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].max()
            minResponseTimeIncorrect = block[block.iloc[:, 15] == 0].iloc[:, 14].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()

            blockData.append({
                'ID': self.getTestID(),
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
        blockDfs = self.initScoring('NumberMemory')
        
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
            minResponseTime = block.iloc[:, 11].min()
            maxResponseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11].max()
            minResponseCorrect = block[block.iloc[:, 10] == 1].iloc[:, 11].min()
            maxResponseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11].max()
            minResponseIncorrect = block[block.iloc[:, 10] == 0].iloc[:, 11].min()
            numZeroInputs = block[block.iloc[:, 11] == 0].iloc[:, 11].count()
            
            blockData.append({
                'ID': self.getTestID(),
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
        blockDfs = self.initScoring('Numerical_nBack')
        
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
            minResponseTime = block.iloc[:, 14].min()
            maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponceCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].min()
            maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
            

            blockData.append({
                'ID': self.getTestID(),
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
        blockDfs = self.initScoring('NumericalSpeed')
        
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
            minResponseTime = block.iloc[:, 14].min()
            maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].min()
            maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()

            blockData.append({
                'ID': self.getTestID(),
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
        blockDfs = self.initScoring('SpeedTabbing')
        
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
            minResponseTime = block.iloc[:, 10].min()
            firstPress = block.iloc[0, 10]
            lastPress = block.iloc[-1, 10]

            blockData.append({
                'ID': self.getTestID(),
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
        blockDfs = self.initScoring('VerbalSpeed')
        
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
            minResponseTime = block.iloc[:, 14].min()
            maxResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].max()
            minResponseCorrect = block[block.iloc[:, 13] == 1].iloc[:, 14].min()
            maxResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].max()
            minResponseIncorrect = block[block.iloc[:, 13] == 0].iloc[:, 14].min()
            numZeroInputs = block[block.iloc[:, 14] == 0].iloc[:, 14].count()
            
            blockData.append({
                'ID': self.getTestID(),
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

        # initialize scoring
        blockDfs = self.initScoring('ObjectLocationMemory')
        
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

            blockData.append({
                'ID': self.getTestID(),
                'Block': blockType,
                'PC': pc,
                'Total Response Time': responseTimes
            })

        # Nitty gritty details
        # 1. Determine the original coordinates of the object
        # 2. Determine the coordinates of the object after the translation

        self.outputToFile(blockData, 'objLocMem_sc')

    def suScore(self):
    
        # NOTE: consists of 3, 3x3 grids of objects

        # initialize scoring
        blockDfs = self.initScoring('SpatialUpdating')
        
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

            blockData.append({
                'ID': self.getTestID(),
                'Block': blockType,
                'PC Grid 1': pcGrid1,
                'PC Grid 2': pcGrid2,
                'PC Grid 3': pcGrid3,
                'PC Total': pcTotal
            })

        # Nitty gritty details
        # 1. Determine the original coordinates of the object
        # 2. Determine the coordinates of the object after the translation

        self.outputToFile(blockData, 'spatUp_sc')

    def wrScore(self):
        
        # TODO: Word recall add incorrect responses

        # initialize scoring
        blockDfs = self.initScoring('WordRecall')
        
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
                'ID': self.getTestID(),
                'Block': blockType,
                'PC': pc,
                'Prop Intrusions': intrusions,
                'PI (No Intrusions)': pi
            })

        self.outputToFile(blockData, 'wrdRec_sc')