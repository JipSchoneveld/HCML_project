import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#read in
def read_and_clean_file(csv_file):
    df = pd.read_csv(csv_file)
    mask = df.applymap(lambda x:'?' in str(x))
    df_clean = df[~mask.any(axis=1)]
    
    income = df_clean['income']
    high_income_reconstructed = []

    for i in income:
        if i > 50000:
            high_income_reconstructed.append(1)
        else:
            high_income_reconstructed.append(0)
        
    high_income_reconstructed = pd.DataFrame({'high_income': high_income_reconstructed[:len(df_clean)]})
    df_clean['high_income'] = high_income_reconstructed
    return df_clean

adult_reconstructed = read_and_clean_file('adult_reconstruction.csv')
print(adult_reconstructed[['gender']])

# #explore
print(adult_reconstructed[['marital-status', 'gender']].value_counts())
print(adult_reconstructed[['education', 'gender']].value_counts())
# print(adult_reconstructed[['income', 'gender']].value_counts())
print(adult_reconstructed[['race', 'gender']].value_counts())
# print(adult_reconstructed[['age', 'gender']].value_counts())

number_of_rows = adult_reconstructed.shape[0]

#age demographic
age_reconstructed = adult_reconstructed['age'].value_counts()

#gender demographic
gender_reconstructed = adult_reconstructed['gender'].value_counts()
percentage_women_reconstructed = (gender_reconstructed[1]/(gender_reconstructed[1]+gender_reconstructed[0]))*100
percentage_men_reconstructed = (gender_reconstructed[0]/(gender_reconstructed[1]+gender_reconstructed[0]))*100


#race demographic
race_reconstructed = adult_reconstructed['race'].value_counts()

#split income
# income = adult_reconstructed['income']
# high_income_reconstructed = []

# for i in income:
#     if i > 50000:
#         high_income_reconstructed.append(1)
#     else:
#         high_income_reconstructed.append(0)
        
# high_income_reconstructed = pd.DataFrame({'high_income': high_income_reconstructed[:len(adult_reconstructed)]})
# adult_reconstructed['high_income'] = high_income_reconstructed


#marital status and income
ms_income_reconstructed = adult_reconstructed[['marital-status', 'high_income']].value_counts()


#gender and income
gender_income_reconstructed = adult_reconstructed[['gender', 'high_income']].value_counts()
high_income_female_reconstructed = 100 * gender_income_reconstructed[3]/gender_reconstructed[1]
high_income_male_reconstructed = 100 * gender_income_reconstructed[2]/gender_reconstructed[0]

#race and income
race_income_reconstructed = adult_reconstructed[['race', 'high_income']].value_counts()

high_income_white_reconstructed = 100 * race_income_reconstructed[1]/race_reconstructed[0]
high_income_black_reconstructed = 100 * race_income_reconstructed[4]/race_reconstructed[1]

#education and income
education_income_reconstructed = adult_reconstructed[['education', 'high_income']].value_counts()

#create bar graphs

age_range = pd.Series(index=range(91), dtype=int)
age_reconstructed = age_reconstructed.reindex(age_range.index, fill_value=0)
age_reconstructed_non_zero = age_reconstructed[age_reconstructed > 0]

age_reconstructed_non_zero.plot(kind= 'bar')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.xticks(rotation=0)

education_income_reconstructed.plot(kind='bar')
plt.title('Education and Income')



plt.show()

#print print print
print(adult_reconstructed.head())
print(percentage_women_reconstructed)
print(percentage_men_reconstructed)
print(ms_income_reconstructed)
print(education_income_reconstructed)
print(high_income_female_reconstructed)
print(high_income_male_reconstructed)
print(high_income_black_reconstructed)
print(high_income_white_reconstructed)


