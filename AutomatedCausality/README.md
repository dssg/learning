#This is a tutorial created by Manojit (Jit) Nandi for Data Science for Social Good fellowship.

## installPackages.R 
Installs the necessary R packages to run the examples in this tutorial. Installs pcalg, RGraphViz and SMPracticals.

##pcExample.R
Runs the PC algorithm on synthetic data where the true causal graph is known, and compares the estimated fit with the true results.

##fciExample.R
Runs the FCI algorithm on synthetic data where the true causal graph is known, and compares the estimated fit with the true results

##twoChainsExample.R
Runs the PC algorithm on the data in twoChains.txt. 

##mathmarksExample.R
Runs the PC algorithm on mathmarks dataset pertaining to student's scores on different mathematics exams. The Mathmarks dataset comes from the SMPracticals package.

##twoChains.txt
Contains the results of simulating 100,000 instances from a DAG where TV influences BMI through two different chains.

##LHC.txt
Contains the results of simulation 100,000 instances from a DAG where TV and BMI are confounded by Diet and Exercise.