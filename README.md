# HCML project
Run all cells in <code>Get_data.ipynb</code> to create preprocessed data. This uses the raw data in <code>data/adult.csv</code> and the data from the FolkTables package to produce the files in <code>Processed_data</code>. 

The code in <code>train_dev.ipynb</code> was used to determine the hyperparameters of the classifier and is only supplied here to demonstrate the development procedure. 

The files <code>train.ipynb</code> and <code>reweigh_train.ipynb</code> contain the code to perform the feature encoding (using <code>Dataverwerking/data_transform.py</code>), train the models and evaluate (using <code>fairness_evals.py</code>) the models. The first file uses an unweighted classifier and the last file uses a weighted classifier. The results are written to CSV files and can be found in the <code>Results</code> folder, where the subfolder <code>weighted</code> contains the results produced with the weighted classifier. The training notebooks also produce the feature importance plots which can be found in the <code>plots</code> folder. 

The weights are calculated using the functions in <code>Dataverwerking/reweighing.py</code> which is imported in the training notebooks. 

Data analysis was done in <code>Data_Analysis.py</code> and can be run in the terminal without any arguments. This produces some plots which can be found in the <code>plots</code> folder. 