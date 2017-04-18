reddit <- read.csv('reddit.csv') #read the csvfile 
str(reddit) #str command
table(reddit$employment.status) #read the table of employment status
summary(reddit) #invoke a summary on the class
levels(reddit$age.range) # the levels of age

##### Plots ###### 
library(ggplot2)
qplot(data = reddit, x = age.range) #this makes a qplot with x being the range of age levels
qplot(data = reddit, x = income.range) #makes plot with x being income

### ordered factors ### 
# something you can group from highest lowest or lowest to highest
ageFactor <- factor(x = reddit$age.range, levels = c('Under 18','18-24','25-34','45-54','55-64','65 or Above'))
is.factor(ageFactor)
qplot(data = reddit, x = ageFactor)

levels(reddit$income.range)
IncomeFactor <- factor(x = reddit$income.range, levels = c("Under $20,000", "$20,000 - $29,999", "$30,000 - $39,999","$40,000 - $49,999","$50,000 - $69,999","$70,000 - $99,999","$100,000 - $149,999", "$150,000 or more" ))
is.factor(IncomeFactor) #order the plot of incomes and check if it is True 
qplot(data=reddit, x = IncomeFactor)
