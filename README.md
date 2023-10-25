**MPIB SCORING**

This repository contains all files related to the MPIB Scoring Tool developed under the guidance of Dr. Naftali Raz of Stony Brook University.

Note: 
For MacOS you may need to give this executable permission to be run on your computer, in this case use these commands to grant permission in terminal: 
cd YourScriptDirectory
chmod 755 testScoringV1

Method 1:
Place testScoringV1 into desktop
Double click to run testScoringv1
When asked whether you want to input a test ID, type “y”
Input the test ID (make sure the test directory is in the Desktop folder and contains the test ID)
Choose default of override mode
Done! The new scored folder should appear inside the test folder and be marked testID_scores

Method 2:
Place testScoringV1 into directory containing gathered tests
Double click to run testScoringV1
When asked whether you want to input a test ID, type “n”
Choose default of override mode
Done! The new scored folder should appear in the current working directory and be marked testID_scores

Override Mode: Allows the user to input specific commands into the program

-Test (acceptable inputs): fs, lu, ms, nm, nb, ns, olm, su, st, vs, wr
-Block (acceptable inputs): N/A
-File (acceptable inputs): csv, xlsx, txt

Glossary

ID: Subject ID number
Block: Practice run or trial run (numbered in order)
PC: Proportion correct (out of 1)
Trials: Total number of inputs per run
RT: Response time
Num 0: Number of zero inputs
Total Correct: Total number of correct responses
ED: Euclidean distance
CB: City block distance
Presses: Total number of presses
PI: Proportion incorrect (out of 1)
Prop Intrusion: Proportion of intrusions (only used in Word Recall)
