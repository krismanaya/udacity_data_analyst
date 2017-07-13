# Summary for ML 

in this class we learned the following summaries below and how best to tune and create your own classification. 

## Dataset / Question 

*  Do I have enough data?
* Can I define a question? 
* enough / right features to answer question? 


## Features 

* exploration 
    * inspect for correlations 
    * outlier removal 
    * impulation 
    * cleaning 

* creating 
    * thing about it like a human 

* representation 
    * test vectorization 
    * discretinitiation 

* scalling 
    * mean subratction 
    * minmax scaler 
    * standard scaler

* selection 
    * KBest 
    * Percentile 
    * Recursive features 

* Transforms 
    * PCA
    * LCA 

## Algorithms 

* tune your alorightms 
    * parameters of algorithm 
    * visual inspection 
    * performance on test data 
    * GridSearchCV 

* pick and algorithm 
    * labeled data ? 
        * NO / unsupervised 
            * k-means clustering
            * spectral clustering 
            * PCA 
            * mixture models / EM algorithm 
            * outlier detections
        * YES / supervised 
            * non-ordered or discrete output 
            * decision tree 
            * Naive Bayes
            * SVM 
            * Ensembles
            * K - Nearest Neighbors 
            * LDA 
            * Logistic Regressions 
            * Ordered or continous out put
                * linear regression 
                * lasso regresssion 
                * decision tree regression 
                * sv regression 

## Evaluation 

* Validate 
    * train/ test split
    * k-fold
    * visualize 

* Pick metric(s)
    * SSE / R^2 
    * precision 
    * recall 
    * F1 Score
    * ROC curve 
    * custom bias / variance