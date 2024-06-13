**Problem Description**<br>
We will evaluate the Census Income data set from the UCI machine learning repository [1] on fairness regarding gender. This dataset from 1996 seems to be the only dataset for income prediction of its size so it is cited and used a lot. It has been a while since this dataset was published, and society has changed in the meantime, so we will examine if it is possible to modernize this dataset by rebalancing the features according to ratios in modern society. We will evaluate whether this improves the fairness.

**Dataset**<br>
We will use the Adult Census Income dataset as extracted from the 1994 Census Bureau database [1]. It contains 48842 instances and 14 features. The features include sex, marital status, relationship, and income.

**Methods and Evaluation**<br>
We will train a classifier to predict per instance whether the income will be above or below the average/median income in the dataset. We will create an extra column containing this information using the existing data so we have the correct target values.

We consider two options for training the classifier. The first option is using an ordinary least squares linear model. This will only give good results if the problem is linearly solvable. The second is using a generalized additive model. This is a linear solution for problems that cannot be solved with a simple linear regression model. The models will predict the outcome which we then convert into a binary classification outcome. 

We will evaluate the fairness of this model regarding gender using group fairness criteria: equal decision measures and conditional on outcome. Then, we will modernize the dataset based on more recent statistics of the ratios for marital status and education per gender. We will do this by reweighing the data points. For example, 
the weight of a data point with 'female' and 'married', will be: current portion of married women in the US / portion of married women in the dataset. We will train and evaluate again, and compare it with the original outcome.

**Discussion**<br>
The first potential risk is that we might need to reconsider the regression model chosen because the model does not fit the data well.
A second risk is that we might not find good demographic data and need to reconsider how we will modernize the dataset.

**References**<br>
[1] R. Kohavi et al. Scaling up the accuracy of naive-bayes classifiers: A decision-tree hybrid. 96:202–207, 1996.

-----

We have assessed your proposal with a “go”. Below we have provided our feedback:
You can take a look at this more recent paper for a newer dataset on income prediction: https://proceedings.neurips.cc/paper/2021/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf The link might give you some related ideas: e.g. training models on different time periods and doing a temporal fairness analysis (expanding on what the paper did), or thinking about reweighing methods with temporal data.

The idea of ‘modernizing’ the dataset is interesting (but do look at the link above) but your experimental setup is unclear. If you’re still going to evaluate on the original data, 'modernizing' the training data might not be beneficial?
Related to this, your current approach is not yet clear: What would be the advantage of this method over the existing reweighing methods? Why do you prefer reweighing according to the current ratio?

Small note: Linear models can work surprisingly well even if the data is not linearly solvable. Regularization can help to prevent overfitting.

General note: <br>
Some of our feedback may contain questions. They are to guide your thinking about the project--we don’t require you to send us a response to these questions. If you have any questions about the project outside of the allocated office hours, you’re welcome to send us an email.
