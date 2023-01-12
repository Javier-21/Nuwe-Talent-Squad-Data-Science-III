# Nuwe Talent Squad Data Science III
## Background
We want to know if the academic performace of students is influenced by their parents. We have available the score of the students in differents areas and extra information about the students and their parents.

## Problem
To find a solution to this problem we have two files. One of them has all the information we need to extract a predictive solution. In the other file we have all the information of the student, but no the information of the parents.

The student data are:
- *Gender*: Sex of the students.
- *Lunch*: If the student has dining scholarships.
- *Test preparation course*: If the student attends an academy
- *Math score*: Score in math
- *Reading score*: Score in reading comprehension
- *Writing score*: Score in writing

The information about the parents is their level of education. The are six levels of classification:
1. *High school*
2. *Some high school*
3. *Some college*
4. *Associate's degree*
5. *Bachelor's degree*
6. *Master's degree*

## Result
The results of the study conclude that the educational level of the parents cannot explain the performance of the students.

## Analysis
To carry out this study, the first step was to observe the data in the file that contains the complete information. I needed to check that all the information is relevant and what kind of correlation there is between it.

In the following image we can see the correlation map.

![Correlations](https://github.com/Javier-21/Nuwe-Talent-Squad-Data-Science-III/blob/main/rsc/correlation.png "Correlations")

The *Unnamed: 0* column is the student ID.

In keeping with the goals of the project I removed all extra information that is not important.
*Gender*, *Lunch*, *Test preparation course* are information that can explain the results of students in the tests, but are not relevant to solving the study problem.

If we look at the image, the scores and the parental level of education have a low correlation.

Another transformation that I did was to calculate the average of the three exams, because all the scores are highly correlated with each other and I want to know the explanation to the general performance, not to the each area.

In the second step, I trained different models of classification, but none of them explain how to predict the level of parents through student performance.
I tried a *neural network*, a *support vector machine (SVM)*, a *random forest* and a *naives bayes*. The *SVM* was the model that achived the best results.

To give a metric to evaluate, I take the best model (*SVM*) and split the entire content of the file in two datasets, one with 80% of the data to train the model and one with 20% to calculate the metrics.

Got an **F1 score (macro) equal to 0.191**

I calculated the confusion matrix. In this matrix we can see what the model predicts compared to the real values.
The following image is the confusion matrix.

![Confusion matrix](https://github.com/Javier-21/Nuwe-Talent-Squad-Data-Science-III/blob/main/rsc/conusion_matrix.png "Confusion matrix")

The axes of the matrix show a coding from 0 to 5, but this corresponds to the parental level of eduction from the lowest to the highest category.

## Solution
To give a final solution I have retrained the *SVM*, but now with all the content of the file with the complete information. After training, I predicted the values from the second file and generated a JSON file named [*predictions.json*](https://github.com/Javier-21/Nuwe-Talent-Squad-Data-Science-III/blob/master/src/predictions.json)

## License
- [*Javier Alegre Revuelta*](https://github.com/Javier-21)
