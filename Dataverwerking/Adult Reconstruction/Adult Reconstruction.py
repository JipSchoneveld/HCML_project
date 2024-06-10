import pandas as pd

#read in
adult_reconstructed = pd.read_csv('adult_reconstruction.csv')
print(adult_reconstructed.head())
print(adult_reconstructed[['gender']])

#explore
print(adult_reconstructed[['marital-status', 'gender']].value_counts())
print(adult_reconstructed[['income', 'gender']].value_counts())
print(adult_reconstructed[['race', 'gender']].value_counts())
print(adult_reconstructed[['age', 'gender']].value_counts())

number_of_rows = adult_reconstructed.shape[0]

#age demographic
age_reconstructed = adult_reconstructed['age'].value_counts()

#gender demographic
gender_reconstructed = adult_reconstructed['gender'].value_counts()
percentage_women_reconstructed = (gender_reconstructed[1]/(gender_reconstructed[1]+gender_reconstructed[0]))*100
percentage_men_reconstructed = (gender_reconstructed[0]/(gender_reconstructed[1]+gender_reconstructed[0]))*100
print(percentage_women_reconstructed)
print(percentage_men_reconstructed)

#marital status and income

#gender and income

#race and income


#transpose age and income to categories?
