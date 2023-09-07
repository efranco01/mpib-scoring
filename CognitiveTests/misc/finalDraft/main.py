# TODO: Add a GUI (will need to compile with modules included)

# IMPORTS
import scoring as sc

if __name__ == '__main__':
    # create a new instance of the class
    scoringTime = sc.Scoring()

    # initialize logging
    scoringTime.initLogging()

    # run the main function
    scoringTime.runMain()

    # organize the data
    scoringTime.makeScoredDir(scoringTime.getTestID())

    # print a message to the console
    print('Done!')