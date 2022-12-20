# Classification


### Introduction

Myers-Briggs-Type Indicator (MBTI) is an introspective self-report survey questionnaire that indicates the personality of different people perceiving the world. There are 16 categories of MBTI as a combination of choosing one for each from the four pairs of preferences: extraversion/introversion, sensing/intuition, thinking/feeling, and judging/perception. As the MBTI test from the 16-personalities website gained a reputation, MBTI became a very popular tool in Korea to categorize and discuss people's personalities in real life. Although there are criticisms of its unscientific origin, MBTI is still widely used as a topic for conversation in Korean society. Because of that reason, I also got interested in this personality type indicator and wanted to investigate on how it works through machine learning.

My goal for this project is to classify the Myers-Briggs-Type Indicator (MBTI) of the respondents from the data. The question in mind is about how to classify MBTI accurately and effectively. The data I'm using to achieve this task is from Kaggle, and it includes the various responses of participants on the questions they were asked from the 16-personalities test and the resulting MBTI. I aim to apply two different supervised classification models on the data--Decision Tree and Support Vector Machine--and find a better model that results in higher accuracy after using cross-validation. Then, I will fit the model with to the entire data, and assess its performance again using the test data. 

### Approaches

While I was proceeding, I faced several challenges caused by the big size of the data, such as having a long running time for both the algorithm and the visualizations. Especially in the Decision Tree model, the branching got enormously huge, and the computer didn't seem to be able to handle all the computations. Therefore, I decided to cut the data to be in a size of (5000, 61) instead of using the full data with a size of (59999, 61). This decision allowed me to have leftover data to test the model at the end. 

### Decision Tree

I first chose to fit a Decision Tree algorithm because the algorithm sounded most intuitive to me to classify the personality. I could visualize how the MBTI test might also have a similar branching algorithm to the decision tree. Having that in mind, I was expecting the decision tree to yield a higher accuracy when fit to the data. I also chose the hyperparameters that make sure the model doesn't overfit nor underfit, which ended up being a cost-complexity pruning alpha value of 0.001. However, the 5-fold cross-validation result of this decision tree model wasn't so great, because the mean squared error was 0.548 on average. This meant that the model was inaccurate for about 54.8%, which suggests that the model can't even classify half of the new responses to a correct MBTI.

### Support Vector Machine

Then, I turned to the Support Vector Machine. I couldn't really intuitively understand how the support vector machine can work in high-dimensional data like the MBTI dataset that has 60 different variables. However, as I thought more about it, using the kernel function to cut through the dimensions sounded like it was a decent model to try out. I chose to use the SVM model with a polynomial kernel of degree 3 and the regularization parameter C = 1  after comparing the mse, and running cross-validation with it. The result was that the SVM model outperformed the Decision Tree model, with a mean mse of 0.02 for 5-fold cross-validation. This model was accurate for about 98% of the validation. When I fitted this model again to the whole data to predict the classification of new test data from the original data, the accuracy was still very high at 97.4%. 


### Conclusion

It was surprising for me to see SVM doing a better job than Decision Tree because it contradicted my initial guess. However, it made sense if we consider the algorithm of the way the MBTI test categorizes personality as something other than the branching mechanism of the decision tree. Since the test accuracy was very high, there must have been some kind of formula in categorizing the personality using different weights for the responses on each question that puts each response into clear categories. In this case, the responses were probably clearly separated for each class, positioned in distinct places when visualized in 60 dimensions. There must have been no respondents making ambiguous moves, like checking 0 (neither disagree nor agree) for all the questions. 

I learned that the Decision Tree algorithm is a lot more restricted in the context of the data to achieve high performance. When we are not sure about whether one variable is weighted a lot higher than the others, performing a decision tree may be able to give some insights on that. If the decision tree doesn't do great, then the data probably doesn't have a strong context or relationships between the variables and the class. I also learned that although the SVM is harder to visualize in high dimensions, the performance can be high if the data are clearly separated. In addition, it will be nice to search about how the MBTI test actually gets scored, and compare the scoring mechanism and the classification algorithm.





### Resources consulted 

1) I consulted with Lab 14,15-SVM, and https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html to recall my memory on SVM and how to implement it using sklearn.

2) I consulted with Lab 16,17-Decision Tree: to recall my memory on Decision Tree and how to implement it using sklearn.

3) I consulted with https://scikit-learn.org/stable/auto_examples/tree/plot_cost_complexity_pruning.html to decide how to prune the tree. I used the code to plot the alpha vs test/train accuracy graph, but I decided the alpha and wrote the code to fit the model and compute mse.

4) I consulted with Homework 5-K-fold Cross Validation: to see the format of the k-fold function and compute_mse function I built by myself. I modified it to be applicable to the classification setting.

5) Further explanations on why SVM works well with high dimensional data: https://datascience.stackexchange.com/questions/103576/why-svm-works-well-with-high-dimensional-data



