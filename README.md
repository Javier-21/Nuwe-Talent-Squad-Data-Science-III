# Nuwe Talent Squad Data Science III
## Background
We want to know if the academic performace of students is influenced by their parents. We have available the score of the students in differents areas and extra information about the students and their parents.

## Problem
To  found a solution to this problem we have two files. One of them have all the information that we need to extract a predictive solution. in the other file we have all the information abaout the student, but no the information abaout the parents.

The information of students are:
- *Gender*: Sex of students.
- *Lunch*: If the student has dining scholarships.
- *Test preparation course*: If the student assist to an academi
- *Math score*: Puntuation in math
- *Reading score*: Puntuation in reading comprension
- *Writing score*: Puntuacion in writing

The information about the parents is the parental level of education. The are six level levels of classification:
1. *High school*
2. *Some high school*
3. *Some college*
4. *Associate's degree*
5. *Bachelor's degree*
6. *Master's degree*

## Result
The results of the study conclude that the parental level of education can not explain the performance of students.

## Analysis
To do this study the first step was observe the data of the file that contain the complete information. I needed check that all the information is relevant and what type of correlation there are between her.

In the next image we can see a map of correlation.

INSERTAR IMAGEN

According to the objective of the project I deleted all the extra that is not important.
*Gender*, *Lunch*, *Test preparation course* are information that can explain the result of students in the proofs, but there aren't relevant to solve to problem of the study.

If we see in the image that the scores and the parental level of education are low.

Other transformation that I did was, I calculte the mean of the three exams, because all scores are very correlated between him and want to know the explanation to the general performance, not to the each area.

In the second step I trained different models of classifications, but any of them no explain how to predict the level of parents througth the performance of the student.
I proved a *neural network*, a *support vector machine (SVM)*, a *random forest* and a *naives bayes*. The *SVM* was the model that achive best results

To give a metrics to evaluate I catch the best model (*SVM*) and split all contents of the file in two dataset, one with the 80% of data to train the model and other with the 20% to calculate the metrics.

I obtained a **F1 score (macro) equal to 0.191**

I calculated the confusión matrix. In this matrix we can see what predict the model in comparasion to the real values.
The next image is the confusion matrix.

INSERTAR IMAGEN

The axis of the matrix show a codification from 0 to 5, but this corresponds the parental level of eduction from the lowest category to the highest.

## Solution
To give a final solution I train the *SVM* again, but now with of the content of file with the complete information. Later to train I predict the values of the second file and generated a JSON file named [*predictions.json*](https://github.com/Javier-21/Nuwe-Talent-Squad-Data-Science-III/blob/master/src/predictions.json)

## License
- [*Javier Alegre Revuelta*](https://github.com/Javier-21)
