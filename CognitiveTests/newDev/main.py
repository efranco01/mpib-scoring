from scoring import Scoring
import os

if __name__ == '__main__':
    # create a new instance of the class
    scoringTime = Scoring()

    # run the main function
    scoringTime.runMain()

    # organize the data
    scoringTime.makeScoredDir()
    
    # return to initial directory
    print(f'    Returning to: ...{os.path.basename(scoringTime.script_dir)}')
    
    # if there are more than one visit numbers listed, keep input from askVisit()
    # and run 
    if len(scoringTime.visit) > 1:
        scoringTime.runVisit()
        
    # print a message to the console
    print('___________________________________Done!___________________________________ \n')
    
    # check if user want's to score another ID, if so, run the main function again
    scoringTime.reRun()