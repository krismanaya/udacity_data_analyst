# Interview Practice (Data-Analyst)



## Question One - Describe a data project you worked on recently. 

** Answer 1 ** 

** I'm going to highlight the parts that I think connect with the job positings***


Recently, I had the option of choosing a data of my choice and was ask to make an effective data visualization. The data I chose to explore consisted information of twenty-eight episodes of the Simpsons. I felt this data would create a fun unique effective visualization with Dimple.js because most people would consider themselves a fan of the beloved Simpsons television show. My first instinct when acquiring the data was to explore the features that could possible represents an overall analytical landscape. The way I sketched out my data was to explore the content in detail through the Pandas module using Seaborn, Matplotlib and Numpy. The idea I had was how to best represent the possible features that are given in the dataset. ** My required skills in Machine Learning methodoligies such as: Regression, Naive Bayesian classifier, Clustering, Matrix Factorization, k-Nearest Neighbors, Natural Language processing, Decision trees, Support Vector Machines and Neural Networks was obtained with my degree at Udacity where we were asked to create a detection model of fraud from the enron data set. I have also have a bachelor's degree In mathematics and have worked on various coding languages such as Python and Matlab.** To describe to you how I could possible approach this data set in a more machine learning methodology, I will break down how I could possible create some analysis within the data. 


First, I looked at the type features whether they are Boolean, time data, integer, and strings or float objects. ** Features are important in any type of dataset because a working knowledge of how to select the best possible features for Machine Learning methodologies such as Regression, Naive Bayesian classifier, Clustering, Matrix Factorization, k-Nearest Neighbors, Natural Language processing, Decision trees, Support Vector Machines and Neural Networks can be crucial to achieving the best approximations. For example, what if we wanted to train the data to possible build a simpsons script writer or a twitter bot, we would want to have the best approximations so we can achieve the best Simpsons script. This connects with the Job Description that you are looking for someone who knows how to integrate diverse data with statistical algorithms and characterize targets of interest. ** 


Secondly, I choose the features that would best represent a visualized interpretation of the data like a boxplot, line plot, bubble plot and pair plot. Visualized exploration is going to let us have large data sets investigations easier to interpret and will show that we could possibly be overfitting or underfitting our data set. Selecting the best suitable features will gives a better target of interest. 


Lastly, I tried to wrap the data objects together by having them be represented by a hue, this lead me to a conclusion of the possible features and what sort of best visualization I may proceed with in my project. The features I chose in the project were: Viewers in united states by millions, date, imdb rating, title and season of the show. I knew I wanted to capture each feature within my visualized data so I decided that a bubble plot would be the best representation of the data with viewers in united states by millions in the y variable and date in the x variable. The reason why I chose a bubble plot is I wanted to create a toolbox feature that contained the title, rating and airdate. It gives the reader something to connect with when the hoover over the bubble and se that possibly there favorite episode wasn't or was liked by a majority of the viewership population, while the color hue would represent all twenty-eight different seasons of the show. I did not want to overcrowd the chart with legends because in my opinion it was another object I felt unnecessary for the reader to analyze. All the information that was needed was contained in each bubble. Personally, this was an exciting project for me because it was unique and a fun dataset to play around with and I believe projects like this is what brings people wanting more visualized data.








## Question Two - You are given a ten piece box of chocolate truffles. You know based on the label that six of the pieces have an orange cream filling and four of the pieces have a coconut filling. If you were to eat four pieces in a row, what is the probability that the first two pieces you eat have an orange cream filling and the last two have a coconut filling? Follow-up question: If you were given an identical box of chocolates and again eat four pieces in a row, what is the probability that exactly two contain coconut filling?


** Answer 2 Part One ** 

The way I would approach this problem would be like selecting slots for the amount of orange fillings to coconut fillings. 

Orange Filling = O 
Coconut Filling = C 

Slot one O: since I have to fill slot one I have 6 pieces of O from my ten choices the P(O) = 6/10 

Slot two O since now I have to fill the second slot with O I have only 5 pieces to choose from then P(O) = 5/9

Slot three C: now I have to fill the third slot with C and I have 4 pieces to choose from then P(C) = 4/8

Slot four C: now I have to fill the forth slot with C and I have 3 pieces left to choose from then P(C) = 3/7 

Since we have related choices in choosing, the probability that the first two pieces you eat have an orange cream filling is the product of probabilities ```6/10 * 5/9 * 4/8 * 3/78 = 0.07```




** Answer 2 Part Two **

First let's write down all the possible combinations: 

```
Comb1  = (O,O,C,C)
Comb2  = (O,C,C,O) 
Comb3  = (C,C,O,O)
Comb4  = (C,O,O,C)
Comb5  = (O,C,O,C)
Comb6  = (C,O,C,O)

```

There are six different combinations or 4 choose 2. To obtain the total combinations in the entire set we just add the combinations of different O to C, which is 16 different, which is the sum of n, choose k possibilities: 

``` n choose k = 1 + 4 + 6 + 4 + 1 = 16. Then we have the P(6/16) = 0.375  or  0.4 ``` 

So the probability that you eat exactly two coconuts chocolate is 6/16 = 0.4. 


## Question Three - Given the table "users":

```
     Table "users"
+-------------+-----------+
| Column      | Type      |
+-------------+-----------+
| id          | integer   |
| username    | character |
| email       | character |
| city        | character |
| state       | character |
| zip         | integer   |
| active      | boolean   |
+-------------+-----------+

```

construct a query to find the top 5 states with the highest number of active users. Include the number for each state in the query result. Example result:

```
+------------+------------------+
| state      | num_active_users |
+------------+------------------+
| New Mexico | 502              |
| Alabama    | 495              |
| California | 300              |
| Maine      | 201              |
| Texas      | 189              |
+------------+------------------+

```

** Answer 3 ** 

``` sql 

SELECT state, count(id) as sum_active_users from users 
WHERE active = 1 
GROUP BY state 
ORDER BY sum_active_users DESC 
limit 5

```


## Question 4 - Define a function first_unique that takes a string as input and returns the first non-repeated (unique) character in the input string. If there are no unique characters return None. Note: Your code should be in Python.

** Answer 4 ** 
``` python 


def first_unique(string):
    ### create list to append string
    unique_char = list()
    for letter in string: 
        ### count letter in string 
        if string.count(letter) == 1: 
            ### if it equals one append to list and choose the first
            unique_char.append(letter)
            return unique_char[0]
    return "None"


```
Probably a better way to look at this problem but if this was an in-interview test I would go with the slowest way. I know the count is very costly here but since this is a practice interview I’m going with my gut and the first thing that pops in my head. 


## Question 5 - What are underfitting and overfitting in the context of Machine Learning? How might you balance them?

** Answer 5 ** 

Underfitting occurs when your training data performs poorly. The reason for this is primarly, the model is unable to capture relationships of the input and the target. Overfitting occurs when the training data does perform well with the input and target, however, when we evaluate the new data its performance hinders. Generally, this is because the model you have created memorized the data and is unable to generalize the unseen examples. 

For underfitting, these probelms may occur if you have poor accuracies on your training data because you probably oversimplified your model. We may be able to repair this we create new features and check them with cross validation methods. Moreover, we may improve if by decreasing the amount of regularization used.

If your model is overfitting we maybe able to create more flexibility by using fewer features, decreasing the size of n and the number of attributes. Finally, we must consider the problem with accuracy on the training and test data. This often could be problematic because the learning algorithm does not have enough data to learn from. You may increase the performance if you could increase the number of training data example. 



## Question 6 - f you were to start your data analyst position today, what would be your goals a year from now?


** Answer 6 - Job Discription ** 


A year from now I would like to be learning new techniques in Deep Learning Neural Networks such as Tensor Flow and be able to work with the team to create new mathematical theories that would benefit the team. I would also like to be a more efficient coder and to be wiser the ways we approach ML, ANN and DNNs. While there is never a concrete way to solve a problem it is the training I will be learning with the team that will make me a better Analyst. Furthermore, I would like to learn more about the Sklearn libraries, Java Script visualizations, new applied mathematical theorems, statistical knowledge and better understanding of computer science. 

My goals I wish to set for the next year would be able to try and finish a Machine Learning project using TensorFlow to create procedural generated recurrent networks which creates cohesive music. Secondly, my goal for next year will be to enroll in the garduate studies math program and the University of California Davis so I can learn more applied mathematics to help better my understanding of more theoretical computer problems. 


