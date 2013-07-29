#########################################################################################
#########################################################################################
##
## DEMONSTRATION OF IV AND CONTROL FUNCTION METHODS
##
## Author: Nick Mader
##
## Description: This code is a simple demonstration of the use and implementation of IV
## and Control Function estimation procedures
##
## Model: Our model, using names for our hypothetical variables for familiarity rather than generalizability, is:
##
##              wage = 5 + 1.0*JobTraining + 0.3*Act_Rel + e_w
##       JobTraining = 1[-1 + 0.2*Act_Rel - 0.4*Dist_Mi + e_j > 0]
##   
##  where e_w and e_j are correlated since we can't control for motivation, and since  motivation will determine both
##  wages and JobTraining. Note that, for interpretive simplicity, "Act_Dev", is interpreted as the relative difference
##  between one's Act score and the average Act.
##
## Notes on control function approach: E[w|X, Z, D] = E[XB + aD + e_w | X, Z, D]= XB + aD + E[e_w | X, Z, D]
##                                                  = XB + aD + D*(E[e_w | X, Z, D=1]) + (1-D)*(E[e_w | X, Z, D=0])
##                                                  = XB + aD + D*(E[e_w | e_j > -ZG]) + (1-D)*(E[e_w | e_j < -ZG])
##
##  See http://en.wikipedia.org/wiki/Inverse_Mills_ratio for constructions of thesee expectations terms.
##
#########################################################################################
#########################################################################################

#-------#
# Setup #
#-------#
  library("MASS") # gets us mvrnorm for drawing multivariate random normal errors
  rm(list=ls())

#---------------#
# Generate Data #
#---------------#
  
  n <- 100000 # Picked a large sample size to get enough precision to comfortably confirm cases when we have obtained the correct parameter estimates
  e_mu <- as.vector(c(0, 0))
  e_sig <- matrix(c(1.0, 0.3, 0.3, 1.0), nrow = 2)
  e <- data.frame(mvrnorm(n, e_mu, e_sig))
  names(e) <- c("e_w", "e_j")
  Act_Rel <- rnorm(n, 0, 4)
  Dist_Mi <- exp(rnorm(n, 0, 0.3))

  JobTraining <- 1*(-1 + 0.2*Act_Rel - 0.4*Dist_Mi + e$e_j > 0)
  wage <- 9 + 1.0*JobTraining + 0.3*Act_Rel + e$e_w

#------------------------#
# Run Various Estimation #
#------------------------#
  
  ### OLS - gives biased estimate of the JobTraining effect -- it's getting
    # credit for being confused with people's motivation!

      summary(lm(wage ~ JobTraining + Act_Rel)) # The estimated effect of training is ~1.5 but should be 1.0
  
  ### IV - instead of using observed JobTraing, IV bases our estimate on the
    # predicted value based on use of an instrumental variable

    # First stage - predict JobTraining using only exogenous predictors
      FirstStage <- glm(JobTraining ~ Act_Rel + Dist_Mi, family = binomial(link="probit"))
      summary(FirstStage)

      ZG_hat <- predict(FirstStage)
      JobTraining_pred <- pnorm(ZG_hat)
      
    # Second stage - use JobTraining, as predicted by controls plus the instrument
      summary(lm(wage ~ JobTraining_pred + Act_Rel))
        # Bias in the estimated effect is gone, but note that the level of statistical significance on the effect
        # is much lower than under OLS. Unlike before, we're only using the portion of variation in training that
        # can be explained by exogenous factors (and we're throwing out the rest), giving us less "identifying"
        # variation in treatment.
    
  ### Control function approach
    InvMills_D1 <-  ifelse(JobTraining==1,  dnorm(-ZG_hat)/(1-pnorm(-ZG_hat)), 0)
    InvMills_D0 <-  ifelse(JobTraining==0, -dnorm(-ZG_hat)/(  pnorm(-ZG_hat)), 0)
    ExpectedError <- ifelse(JobTraining==1, InvMills_D1, InvMills_D0)
      plot(e$e_j, ExpectedError)
      plot(e$e_w, ExpectedError)

    summary(lm(wage ~ JobTraining + Act_Rel + ExpectedError))
      # Again, we get an unbiased estimate of the effect of training, this time by directly accounting for the
      # expected influence of motivation, rather than looking for explanations of training that have nothing to
      # do with motivation (which is what IV does).
      #
      # In this case, we're getting stronger statistical significance with the control function approach (making
      # it a more "efficient" estimation procedure; i.e., it has gotten more statistical precision using no
      # additional resources). However, one advantage that this particular case has which may not always be true
      # is that this particular control function approach that I've taken assumes multivariate normality between
      # the two errors, which we know is true by how the data were constructed. The less appropriate that assumption
      # is, the worse this control function approach will perform, motivating us to use more general methods.





