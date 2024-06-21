import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#read in
def read_file(csv_file):
    df = pd.read_csv(csv_file)
    return df

adult_reconstructed = read_file('data_2018.csv')
adult_old = read_file('adult.csv')
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

#women
education_sex_HS_female_old = 100* education_sex_old[5]/(education_sex_old[0] + education_sex_old[5])
education_sex_bachelors_female_old = 100* education_sex_old[2]/(education_sex_old[4] + education_sex_old[2])
education_sex_masters_female_old =100* education_sex_old[6]/(education_sex_old[8] + education_sex_old[6])
education_sex_doctorate_female_old = 100* education_sex_old[16]/(education_sex_old[14] + education_sex_old[16])
education_sex_associate_degree_female_old = 100* education_sex_old[7]/(education_sex_old[9] + education_sex_old[7])

#men
education_sex_HS_male_old = 100* education_sex_old[0]/(education_sex_old[0] + education_sex_old[5])
education_sex_bachelors_male_old = 100* education_sex_old[4]/(education_sex_old[4] + education_sex_old[2])
education_sex_masters_male_old = 100* education_sex_old[8]/(education_sex_old[8] + education_sex_old[6])
education_sex_doctorate_male_old = 100* education_sex_old[14]/(education_sex_old[14] + education_sex_old[16])
education_sex_associate_degree_male_old = 100* education_sex_old[9]/(education_sex_old[9] + education_sex_old[7])

print(education_sex_old)

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

# Prepare the data for plotting
education_levels = ['High School', 'Bachelors', 'Masters', 'Doctorate', 'Associate Degree']
# Organize the data into lists
female_percentages_old= [
    education_sex_HS_female_old,
    education_sex_bachelors_female_old,
    education_sex_masters_female_old,
    education_sex_doctorate_female_old,
    education_sex_associate_degree_female_old
]

male_percentages_old = [
    education_sex_HS_male_old,
    education_sex_bachelors_male_old,
    education_sex_masters_male_old,
    education_sex_doctorate_male_old,
    education_sex_associate_degree_male_old
]

# Create the grouped bar graph
from matplotlib import style
bar_width = 0.18
index = np.arange(len(education_levels))
style.use("Solarize_Light2")

plt.figure(figsize=(10, 6))

# Plot bars for males
plt.bar(index + bar_width/2, male_percentages_old, bar_width, label='Old Male', color='darkgreen')

plt.bar(index + bar_width /2 + bar_width, male_percentages, bar_width, label='2018 Male', color='yellowgreen')
plt.bar(index - bar_width/2 -bar_width, female_percentages_old, bar_width, label='Old Female', color='rebeccapurple')


plt.bar(index - bar_width/2, female_percentages, bar_width, label='2018 Female', color='plum')

# Add title and labels
plt.title('Percentage Distribution of Education Levels by Sex for 2018 data')
plt.xlabel('Education Level')
plt.ylabel('Percentage (%)')
plt.xticks(index, education_levels)
plt.legend()

# Display the bar graph
plt.tight_layout()
plt.show()

#print print print
# print(adult_old.head())
# print(percentage_women_reconstructed)
# print(percentage_men_reconstructed)
# print(ms_income_reconstructed)
# print(education_income_reconstructed)
# print(high_income_female_reconstructed)
# print(high_income_male_reconstructed)
# print(high_income_black_reconstructed)
# print(high_income_white_reconstructed)
# print(gender_income_reconstructed)