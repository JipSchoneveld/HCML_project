import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#read in
def read_file(csv_file):
    df = pd.read_csv(csv_file)
    return df

adult_reconstructed = read_file(os.path.join('Processed_data', 'data_2018.csv'))
adult_old = read_file(os.path.join('Processed_data', 'adult.csv'))
print(adult_reconstructed[['sex']])

# #explore
print(adult_reconstructed[['marital.status', 'sex']].value_counts())
print(adult_reconstructed[['education', 'sex']].value_counts())
# print(adult_reconstructed[['income', 'gender']].value_counts())
print(adult_reconstructed[['race', 'sex']].value_counts())
# print(adult_reconstructed[['age', 'gender']].value_counts())

number_of_rows = adult_reconstructed.shape[0]

#age demographic
age_reconstructed = adult_reconstructed['age'].value_counts()

#gender demographic
gender_reconstructed = adult_reconstructed['sex'].value_counts()
percentage_women_reconstructed = (gender_reconstructed[1]/(gender_reconstructed[1]+gender_reconstructed[0]))*100
percentage_men_reconstructed = (gender_reconstructed[0]/(gender_reconstructed[1]+gender_reconstructed[0]))*100

#income demographic
income_reconstructed = adult_reconstructed['income'].value_counts()
percentage_high_reconstructed =  income_reconstructed[1]/(income_reconstructed[0]+income_reconstructed[1])*100
percentage_low_reconstructed = income_reconstructed[0]/(income_reconstructed[0]+income_reconstructed[1])*100

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
ms_income_reconstructed = adult_reconstructed[['marital.status', 'income']].value_counts()
high_income_married_reconstructed = 100 * ms_income_reconstructed[1]/(ms_income_reconstructed[0] + ms_income_reconstructed[1])
high_income_never_married_reconstructed = 100 * ms_income_reconstructed[4]/(ms_income_reconstructed[4] + ms_income_reconstructed[2])
high_income_divorced_reconstructed = 100 * ms_income_reconstructed[5]/(ms_income_reconstructed[3] + ms_income_reconstructed[5])
high_income_separated_reconstructed = 100 * ms_income_reconstructed[9]/(ms_income_reconstructed[9] + ms_income_reconstructed[7])
high_income_widowed_reconstructed = 100 * ms_income_reconstructed[8]/(ms_income_reconstructed[8] + ms_income_reconstructed[6])

#non-high-income percentages
non_high_income_married_reconstructed = 100 - high_income_married_reconstructed
non_high_income_never_married_reconstructed = 100 - high_income_never_married_reconstructed
non_high_income_divorced_reconstructed = 100 - high_income_divorced_reconstructed
non_high_income_separated_reconstructed = 100 - high_income_separated_reconstructed
non_high_income_widowed_reconstructed = 100 - high_income_widowed_reconstructed

#marital status, sex and income
ms_sex_income_reconstructed = adult_reconstructed[['marital.status', 'sex', 'income']].value_counts()
high_income_married_female_reconstructed = 100 * ms_sex_income_reconstructed[5]/(ms_sex_income_reconstructed[5] + ms_sex_income_reconstructed[1])
high_income_never_married_female_reconstructed = 100 * ms_sex_income_reconstructed[9]/(ms_sex_income_reconstructed[9] + ms_sex_income_reconstructed[4])
high_income_divorced_female_reconstructed = 100 * ms_sex_income_reconstructed[10]/(ms_sex_income_reconstructed[10] + ms_sex_income_reconstructed[6])
high_income_separated_female_reconstructed = 100 * ms_sex_income_reconstructed[19]/(ms_sex_income_reconstructed[19] + ms_sex_income_reconstructed[13])
high_income_widowed_female_reconstructed = 100 * ms_sex_income_reconstructed[14]/(ms_sex_income_reconstructed[14] + ms_sex_income_reconstructed[12])

high_income_married_male_reconstructed = 100 * ms_sex_income_reconstructed[0]/(ms_sex_income_reconstructed[0] + ms_sex_income_reconstructed[3])
high_income_never_married_male_reconstructed = 100 * ms_sex_income_reconstructed[7]/(ms_sex_income_reconstructed[7] + ms_sex_income_reconstructed[2])
high_income_divorced_male_reconstructed = 100 * ms_sex_income_reconstructed[11]/(ms_sex_income_reconstructed[11] + ms_sex_income_reconstructed[8])
high_income_separated_male_reconstructed = 100 * ms_sex_income_reconstructed[18]/(ms_sex_income_reconstructed[18] + ms_sex_income_reconstructed[15])
high_income_widowed_male_reconstructed = 100 * ms_sex_income_reconstructed[17]/(ms_sex_income_reconstructed[17] + ms_sex_income_reconstructed[16])


#gender and income
gender_income_reconstructed = adult_reconstructed[['sex', 'income']].value_counts()
high_income_female_reconstructed = 100 * gender_income_reconstructed[3]/gender_reconstructed[1]
high_income_male_reconstructed = 100 * gender_income_reconstructed[2]/gender_reconstructed[0]

#race and income
# race_income_reconstructed = adult_reconstructed[['race', 'income']].value_counts()

# high_income_white_reconstructed = 100 * race_income_reconstructed[1]/race_reconstructed[0]
# high_income_black_reconstructed = 100 * race_income_reconstructed[4]/race_reconstructed[1]

#education and income
education_income_reconstructed = adult_reconstructed[['education', 'income']].value_counts()
high_income_HS_reconstructed = 100 * education_income_reconstructed[7]/(education_income_reconstructed[7] + education_income_reconstructed[0])
high_income_bachelors_reconstructed = 100 * education_income_reconstructed[2]/(education_income_reconstructed[2] + education_income_reconstructed[3])
high_income_masters_reconstructed = 100 * education_income_reconstructed[4]/(education_income_reconstructed[4] + education_income_reconstructed[9])
high_income_doctorate_reconstructed = 100 * education_income_reconstructed[13]/(education_income_reconstructed[13] + education_income_reconstructed[20])
high_income_associate_degree_reconstructed = 100 * education_income_reconstructed[8]/(education_income_reconstructed[8] + education_income_reconstructed[5])

# Calculate the percentages
# high_income_HS_reconstructed = 100 * education_income_reconstructed[7] / (education_income_reconstructed[7] + education_income_reconstructed[0])
# high_income_bachelors_reconstructed = 100 * education_income_reconstructed[2] / (education_income_reconstructed[2] + education_income_reconstructed[3])
# high_income_masters_reconstructed = 100 * education_income_reconstructed[4] / (education_income_reconstructed[4] + education_income_reconstructed[9])
# high_income_doctorate_reconstructed = 100 * education_income_reconstructed[13] / (education_income_reconstructed[13] + education_income_reconstructed[20])
# high_income_associate_degree_reconstructed = 100 * education_income_reconstructed[8] / (education_income_reconstructed[8] + education_income_reconstructed[5])


# non_high_income_HS_reconstructed = 100 - high_income_HS_reconstructed
# non_high_income_bachelors_reconstructed = 100 - high_income_bachelors_reconstructed
# non_high_income_masters_reconstructed = 100 - high_income_masters_reconstructed
# non_high_income_doctorate_reconstructed = 100 - high_income_doctorate_reconstructed
# non_high_income_associate_degree_reconstructed = 100 - high_income_associate_degree_reconstructed

#education, sex and income
education_sex_income_reconstructed = adult_reconstructed[['education', 'sex', 'income']].value_counts()

#women
high_income_HS_female_reconstructed = 100 * education_sex_income_reconstructed[18]/(education_sex_income_reconstructed[18] + education_sex_income_reconstructed[2])
high_income_bachelors_female_reconstructed = 100 * education_sex_income_reconstructed[6]/(education_sex_income_reconstructed[6] + education_sex_income_reconstructed[5])
high_income_masters_female_reconstructed = 100 * education_sex_income_reconstructed[12]/(education_sex_income_reconstructed[12] + education_sex_income_reconstructed[14])
high_income_doctorate_female_reconstructed = 100 * education_sex_income_reconstructed[28]/(education_sex_income_reconstructed[28] + education_sex_income_reconstructed[41])
high_income_associate_female_degree_reconstructed = 100 * education_sex_income_reconstructed[17]/(education_sex_income_reconstructed[17] + education_sex_income_reconstructed[10])

#men
high_income_HS_male_reconstructed = 100 * education_sex_income_reconstructed[8]/(education_sex_income_reconstructed[8] + education_sex_income_reconstructed[0])
high_income_bachelors_male_reconstructed = 100 * education_sex_income_reconstructed[4]/(education_sex_income_reconstructed[4] + education_sex_income_reconstructed[9])
high_income_masters_male_reconstructed = 100 * education_sex_income_reconstructed[11]/(education_sex_income_reconstructed[11] + education_sex_income_reconstructed[21])
high_income_doctorate_male_reconstructed = 100 * education_sex_income_reconstructed[25]/(education_sex_income_reconstructed[25] + education_sex_income_reconstructed[42])
high_income_associate_degree_male_reconstructed = 100 * education_sex_income_reconstructed[15]/(education_sex_income_reconstructed[15] + education_sex_income_reconstructed[13])
# print(education_sex_income_reconstructed)

#education and sex
education_sex_reconstructed = adult_reconstructed[['education', 'sex']].value_counts()

#women
education_sex_HS_female_reconstructed = 100* education_sex_reconstructed[5]/(education_sex_reconstructed[0] + education_sex_reconstructed[5])
education_sex_bachelors_female_reconstructed = 100* education_sex_reconstructed[2]/(education_sex_reconstructed[4] + education_sex_reconstructed[2])
education_sex_masters_female_reconstructed =100* education_sex_reconstructed[6]/(education_sex_reconstructed[8] + education_sex_reconstructed[6])
education_sex_doctorate_female_reconstructed = 100* education_sex_reconstructed[16]/(education_sex_reconstructed[14] + education_sex_reconstructed[16])
education_sex_associate_degree_female_reconstructed = 100* education_sex_reconstructed[7]/(education_sex_reconstructed[9] + education_sex_reconstructed[7])

#men
education_sex_HS_male_reconstructed = 100* education_sex_reconstructed[0]/(education_sex_reconstructed[0] + education_sex_reconstructed[5])
education_sex_bachelors_male_reconstructed = 100* education_sex_reconstructed[4]/(education_sex_reconstructed[4] + education_sex_reconstructed[2])
education_sex_masters_male_reconstructed = 100* education_sex_reconstructed[8]/(education_sex_reconstructed[8] + education_sex_reconstructed[6])
education_sex_doctorate_male_reconstructed = 100* education_sex_reconstructed[14]/(education_sex_reconstructed[14] + education_sex_reconstructed[16])
education_sex_associate_degree_male_reconstructed = 100* education_sex_reconstructed[9]/(education_sex_reconstructed[9] + education_sex_reconstructed[7])

print(education_sex_reconstructed)

#create bar graphs

# age_range = pd.Series(index=range(91), dtype=int)
# age_reconstructed = age_reconstructed.reindex(age_range.index, fill_value=0)
# age_reconstructed_non_zero = age_reconstructed[age_reconstructed > 0]

# age_reconstructed_non_zero.plot(kind= 'bar')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)

# education_income_reconstructed.plot(kind='bar')
# plt.title('Education and Income')



# plt.show()

# Prepare the data for plotting
education_levels = ['High School', 'Bachelors', 'Masters', 'Doctorate', 'Associate Degree']
# Organize the data into lists
female_percentages = [
    education_sex_HS_female_reconstructed,
    education_sex_bachelors_female_reconstructed,
    education_sex_masters_female_reconstructed,
    education_sex_doctorate_female_reconstructed,
    education_sex_associate_degree_female_reconstructed
]

male_percentages = [
    education_sex_HS_male_reconstructed,
    education_sex_bachelors_male_reconstructed,
    education_sex_masters_male_reconstructed,
    education_sex_doctorate_male_reconstructed,
    education_sex_associate_degree_male_reconstructed
]

#For old data
number_of_rows = adult_old.shape[0]

#age demographic
age_old = adult_old['age'].value_counts()

#gender demographic
gender_old = adult_old['sex'].value_counts()
percentage_women_old = (gender_old[1]/(gender_old[1]+gender_old[0]))*100
percentage_men_old = (gender_old[0]/(gender_old[1]+gender_old[0]))*100

#income demographic
income_old = adult_old['income'].value_counts()
percentage_high_old =  income_old[1]/(income_old[0]+income_old[1])*100
percentage_low_old = income_old[0]/(income_old[0]+income_old[1])*100

#race demographic
race_old = adult_old['race'].value_counts()

#split income
# income = adult_old['income']
# high_income_old = []

# for i in income:
#     if i > 50000:
#         high_income_old.append(1)
#     else:
#         high_income_old.append(0)
        
# high_income_old = pd.DataFrame({'high_income': high_income_old[:len(adult_old)]})
# adult_old['high_income'] = high_income_old


#marital status and income
ms_income_old = adult_old[['marital.status', 'income']].value_counts()
high_income_married_old = 100 * ms_income_old[1]/(ms_income_old[0] + ms_income_old[1])
high_income_never_married_old = 100 * ms_income_old[4]/(ms_income_old[4] + ms_income_old[2])
high_income_divorced_old = 100 * ms_income_old[5]/(ms_income_old[3] + ms_income_old[5])
high_income_separated_old = 100 * ms_income_old[9]/(ms_income_old[9] + ms_income_old[7])
high_income_widowed_old = 100 * ms_income_old[8]/(ms_income_old[8] + ms_income_old[6])

#non-high-income percentages
non_high_income_married_old = 100 - high_income_married_old
non_high_income_never_married_old = 100 - high_income_never_married_old
non_high_income_divorced_old = 100 - high_income_divorced_old
non_high_income_separated_old = 100 - high_income_separated_old
non_high_income_widowed_old = 100 - high_income_widowed_old

#marital status, sex and income
ms_sex_income_old = adult_old[['marital.status', 'sex', 'income']].value_counts()
high_income_married_female_old = 100 * ms_sex_income_old[5]/(ms_sex_income_old[5] + ms_sex_income_old[1])
high_income_never_married_female_old = 100 * ms_sex_income_old[9]/(ms_sex_income_old[9] + ms_sex_income_old[4])
high_income_divorced_female_old = 100 * ms_sex_income_old[10]/(ms_sex_income_old[10] + ms_sex_income_old[6])
high_income_separated_female_old = 100 * ms_sex_income_old[19]/(ms_sex_income_old[19] + ms_sex_income_old[13])
high_income_widowed_female_old = 100 * ms_sex_income_old[14]/(ms_sex_income_old[14] + ms_sex_income_old[12])

high_income_married_male_old = 100 * ms_sex_income_old[0]/(ms_sex_income_old[0] + ms_sex_income_old[3])
high_income_never_married_male_old = 100 * ms_sex_income_old[7]/(ms_sex_income_old[7] + ms_sex_income_old[2])
high_income_divorced_male_old = 100 * ms_sex_income_old[11]/(ms_sex_income_old[11] + ms_sex_income_old[8])
high_income_separated_male_old = 100 * ms_sex_income_old[18]/(ms_sex_income_old[18] + ms_sex_income_old[15])
high_income_widowed_male_old = 100 * ms_sex_income_old[17]/(ms_sex_income_old[17] + ms_sex_income_old[16])


#gender and income
gender_income_old = adult_old[['sex', 'income']].value_counts()
high_income_female_old = 100 * gender_income_old[3]/gender_old[1]
high_income_male_old = 100 * gender_income_old[2]/gender_old[0]

#race and income
# race_income_old = adult_old[['race', 'income']].value_counts()

# high_income_white_old = 100 * race_income_old[1]/race_old[0]
# high_income_black_old = 100 * race_income_old[4]/race_old[1]

#education and income
education_income_old = adult_old[['education', 'income']].value_counts()
high_income_HS_old = 100 * education_income_old[7]/(education_income_old[7] + education_income_old[0])
high_income_bachelors_old = 100 * education_income_old[2]/(education_income_old[2] + education_income_old[3])
high_income_masters_old = 100 * education_income_old[4]/(education_income_old[4] + education_income_old[9])
high_income_doctorate_old = 100 * education_income_old[13]/(education_income_old[13] + education_income_old[20])
high_income_associate_degree_old = 100 * education_income_old[8]/(education_income_old[8] + education_income_old[5])

# Calculate the percentages
# high_income_HS_old = 100 * education_income_old[7] / (education_income_old[7] + education_income_old[0])
# high_income_bachelors_old = 100 * education_income_old[2] / (education_income_old[2] + education_income_old[3])
# high_income_masters_old = 100 * education_income_old[4] / (education_income_old[4] + education_income_old[9])
# high_income_doctorate_old = 100 * education_income_old[13] / (education_income_old[13] + education_income_old[20])
# high_income_associate_degree_old = 100 * education_income_old[8] / (education_income_old[8] + education_income_old[5])


# non_high_income_HS_old = 100 - high_income_HS_old
# non_high_income_bachelors_old = 100 - high_income_bachelors_old
# non_high_income_masters_old = 100 - high_income_masters_old
# non_high_income_doctorate_old = 100 - high_income_doctorate_old
# non_high_income_associate_degree_old = 100 - high_income_associate_degree_old

#education, sex and income
education_sex_income_old = adult_old[['education', 'sex', 'income']].value_counts()

#women
high_income_HS_female_old = 100 * education_sex_income_old[18]/(education_sex_income_old[18] + education_sex_income_old[2])
high_income_bachelors_female_old = 100 * education_sex_income_old[6]/(education_sex_income_old[6] + education_sex_income_old[5])
high_income_masters_female_old = 100 * education_sex_income_old[12]/(education_sex_income_old[12] + education_sex_income_old[14])
high_income_doctorate_female_old = 100 * education_sex_income_old[28]/(education_sex_income_old[28] + education_sex_income_old[41])
high_income_associate_female_degree_old = 100 * education_sex_income_old[17]/(education_sex_income_old[17] + education_sex_income_old[10])

#men
high_income_HS_male_old = 100 * education_sex_income_old[8]/(education_sex_income_old[8] + education_sex_income_old[0])
high_income_bachelors_male_old = 100 * education_sex_income_old[4]/(education_sex_income_old[4] + education_sex_income_old[9])
high_income_masters_male_old = 100 * education_sex_income_old[11]/(education_sex_income_old[11] + education_sex_income_old[21])
high_income_doctorate_male_old = 100 * education_sex_income_old[25]/(education_sex_income_old[25] + education_sex_income_old[42])
high_income_associate_degree_male_old = 100 * education_sex_income_old[15]/(education_sex_income_old[15] + education_sex_income_old[13])
# print(education_sex_income_old)

#education and sex

education_sex_old = adult_old[['education', 'sex']].value_counts()
#print(education_sex_old)
values_educ_old = {"Male": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}, "Female": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}}
for sex in adult_old["sex"].unique():
    total = sum(education_sex_old[:,sex])
    for edu in adult_old["education"].unique():
        values_educ_old[sex][edu] = 100* education_sex_old[edu][sex]/(total)

values_educ_reconstructed = {"Male": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}, "Female": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}}
for sex in adult_reconstructed["sex"].unique():
    total = sum(education_sex_reconstructed[:,sex])
    for edu in adult_old["education"].unique():
        values_educ_reconstructed[sex][edu] = 100* education_sex_reconstructed[edu][sex]/(total)


#marital status and sex
marital_sex_old = adult_old[['marital.status', 'sex']].value_counts()
values_mar_old = {"Male":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}, "Female":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}}
for sex in adult_old["sex"].unique():
    total = sum(marital_sex_old[:,sex])
    for mar in adult_old["marital.status"].unique():
        values_mar_old[sex][mar] = 100* marital_sex_old[mar][sex]/(total)

marital_sex_reconstructed = adult_reconstructed[['marital.status', 'sex']].value_counts()
values_mar_reconstructed = {"Male":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}, "Female":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}}
for sex in adult_reconstructed["sex"].unique():
    total = sum(marital_sex_reconstructed[:,sex])
    for mar in adult_old["marital.status"].unique():
        values_mar_reconstructed[sex][mar] = 100* marital_sex_reconstructed[mar][sex]/(total)
#create bar graphs

# age_range = pd.Series(index=range(91), dtype=int)
# age_old = age_old.reindex(age_range.index, fill_value=0)
# age_old_non_zero = age_old[age_old > 0]

# age_old_non_zero.plot(kind= 'bar')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.xticks(rotation=0)

# education_income_old.plot(kind='bar')
# plt.title('Education and Income')



# plt.show()
# Create the grouped bar graph
from matplotlib import style
bar_width = 0.18

style.use("ggplot")
#['Preschool', '1st-4th', '5th-6th','7th-8th', '9th', '10th' ,'11th','12th', 'HS-grad','Assoc', 'Some-college',  'Bachelors','Masters','Prof-school', 'Doctorate']
values_male = [value for _, value in values_educ_old['Male'].items() ]
labels_male = [value for value,_ in values_educ_old['Male'].items() ]
values_female = [value for _, value in values_educ_old['Female'].items() ]
values_male_new = [value for _, value in values_educ_reconstructed['Male'].items() ]
values_female_new = [value for _, value in values_educ_reconstructed['Female'].items() ]
index = np.arange(len(labels_male))
print(labels_male)
plt.figure(figsize=(10, 6))
# Plot bars for males
plt.bar(index + bar_width/2, values_male, bar_width, label='Old, Male', color='sienna')

plt.bar(index + bar_width /2 + bar_width, values_male_new, bar_width, label='2018, Male', color='darksalmon')
plt.bar(index - bar_width/2 -bar_width, values_female, bar_width, label='Old, Female', color='palevioletred')
plt.bar(index - bar_width/2, values_female_new , bar_width, label='2018, Female', color='lightpink')

#Add demographic data 
plt.scatter(index + bar_width/2+ bar_width, [3.689159521146597/4, 3.689159521146597/4, 3.689159521146597/4, 3.689159521146597/4, 7.709705480303218/3, 7.709705480303218/3,7.709705480303218/3, 30.051779130939067/2, 30.051779130939067/2, 18.30578683567375, 8.689780870717865, 20.197174930615965, 7.699763887162918, 1.4912389710451102, 2.1656103723955096], color="black", label="2018 demographic data")
plt.scatter(index - bar_width/2,  [3.625269482515741/4, 3.625269482515741/4,3.625269482515741/4,3.625269482515741/4, 6.814697206721303/3, 6.814697206721303/3,6.814697206721303/3, 27.313269046673984/2, 27.313269046673984/2, 18.740417318483583, 10.594846171207982, 21.034812860445026, 9.329348494400213, 1.0903826846295734, 1.4569567349225991],color="black")

# Add title and labels
plt.title('Percentage Distribution of Education Levels by Sex')
plt.xlabel('Education Level')
plt.ylabel('Percentage per sex (%)')
plt.xticks(index, labels=labels_male, rotation=45)
plt.legend()

# Display the bar graph
plt.tight_layout()
plt.savefig(os.path.join("plots", 'data_analysis_educ'))
plt.show()

#marital status
values_male = [value for _, value in values_mar_old['Male'].items() ]
labels_male = [value for value,_ in values_mar_old['Male'].items() ]
values_female = [value for _, value in values_mar_old['Female'].items() ]
values_male_new = [value for _, value in values_mar_reconstructed['Male'].items() ]
values_female_new = [value for _, value in values_mar_reconstructed['Female'].items() ]
index = np.arange(len(labels_male))
print(labels_male)
plt.figure(figsize=(10, 6))
# Plot bars for males
plt.bar(index + bar_width/2, values_male, bar_width, label='Old, Male', color='sienna')

plt.bar(index + bar_width /2 + bar_width, values_male_new, bar_width, label='2018, Male', color='darksalmon')
plt.bar(index - bar_width/2 -bar_width, values_female, bar_width, label='Old, Female', color='palevioletred')
plt.bar(index - bar_width/2, values_female_new , bar_width, label='2018, Female', color='lightpink')

#Add demographic data 
plt.scatter(index + bar_width /2 + bar_width,[x*100 for x in [0.355, 0.531, 0.016, 0.089, 0.009] ], color="black", label="2018 demographic data")
plt.scatter(index - bar_width/2, [x*100 for x in[0.342 , 0.475 , 0.025 , 0.130 , 0.027 ] ],color="black")

# Add title and labels
plt.title('Percentage Distribution of marital status by Sex')
plt.xlabel('Education Level')
plt.ylabel('Percentage per sex (%)')
plt.xticks(index, labels=labels_male, rotation=45)
plt.legend()

# Display the bar graph
plt.tight_layout()
plt.savefig(os.path.join("plots", 'data_analysis_mar'))
plt.show()