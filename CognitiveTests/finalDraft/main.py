# SCORING:
# TODO: Score distance using city block method (will be in the nitty gritty area) OLM and SU
# OLM is 6x6 and SU is 3x3, show correct cell vs incorrect cell
# TODO: Score avg distance across blocks (will be in the nitty gritty area)
# TODO: Add additional scoring methods (e.g. avg distance from correct block)

# OUTPUT:
# TODO: LU add mean streak length correct vs incorrect
# TODO: MS sort errors by square (will be in the nitty gritty area)
# TODO: OS Module on windows seems to be duplicating the output.log file, besides that it works fine

# OTHER:
# TODO: Compile as executable for MAC and PC
# TODO: Add a GUI (will need to compile with modules included)
# TODO: Send windows executable to Dr. Raz
# TODO: Override option to filter 0s from response time
# TODO: Finish Block Override

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