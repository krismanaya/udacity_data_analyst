################################# CSV HOW TO ###################################

getwd() #checks working directory
setwd('/Users/Anaya/repos/udacity_data_analyst/project_4/data_sets') #sets working directory

statesInfo <- read.csv('stateData.csv') #reads csv command

stateSubset <- subset(statesInfo, state.region == 1) #retrive column with region one. 
head(stateSubset, 2) #checks first top two with state region 1
dim(stateSubset) #checks the dimension of the dataframe

stateSubsetBracket <- statesInfo[statesInfo$state.region == 1, ] # example column df[rows,columns] of dataframe. 
head(stateSubsetBracket) #checks the first default head region 
dim(stateSubsetBracket) #checks dimension


gradSubsetAboveFifty <- subset(statesInfo, highSchoolGrad >= 50.0) #reads all the states with grads > 50%
gradSubsetLessFifty <- subset(statesInfo, highSchoolGrad < 50.0) #reads all less than 50%

mean(gradSubsetAboveFifty$life.exp) #the average life.exp of a graduate more than and =50%
mean(gradSubsetLessFifty$life.exp) #the average life.exp of a graduate less than 50%
