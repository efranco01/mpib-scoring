import numpy as np
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
        
        # TODO: LU add mean streak length correct vs incorrect

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
        
        # TODO: MS sort errors by square (will be in the nitty gritty area)

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
        # TODO: Add additional scoring methods (e.g. avg distance from correct block)
        # TODO: Add a matrix representation of the grid showing correct vs incorrect responses
        
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
                'ID': self.getTestID(),
                'Block': blockType,
                'PC': pc,
                'Total Response Time': responseTimes,
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
                'ID': self.getTestID(),
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