# HCML_project
-------------------------------------------------------------------------------------------------------------------
Feedback: <\br>
•	You can take a look at this more recent paper for a newer dataset on income prediction:  <\br> https://proceedings.neurips.cc/paper/2021/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf The link might give you some related ideas: e.g. training models on different time periods and doing a temporal fairness analysis (expanding on what the paper did), or thinking about reweighing methods with temporal data. <\br>
•	The idea of ‘modernizing’ the dataset is interesting (but do look at the link above) but your experimental setup is unclear. If you’re still going to evaluate on the original data, 'modernizing' the training data might not be beneficial?  <\br>
•	Related to this, your current approach is not yet clear: What would be the advantage of this method over the existing reweighing methods? Why do you prefer reweighing according to the current ratio?  <\br>
•	Small note: Linear models can work surprisingly well even if the data is not linearly solvable. Regularization can help to prevent overfitting. 

 
