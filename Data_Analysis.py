import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


#Getting the data
def read_file(csv_file):
    df = pd.read_csv(csv_file)
    return df


adult_reconstructed = read_file(os.path.join('Processed_data', 'data_2018.csv'))
adult_old = read_file(os.path.join('Processed_data', 'adult.csv'))

#Getting the specific data needed for plots old education
education_sex_old = adult_old[['education', 'sex']].value_counts()
values_educ_old = {"Male": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}, "Female": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}}
for sex in adult_old["sex"].unique():
    total = sum(education_sex_old[:,sex])
    for edu in adult_old["education"].unique():
        values_educ_old[sex][edu] = 100* education_sex_old[edu][sex]/(total)
#Getting the specific data needed for plots reconstructed education
education_sex_reconstructed = adult_reconstructed[['education', 'sex']].value_counts()
values_educ_reconstructed = {"Male": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}, "Female": {'Preschool':0, '1st-4th':0, '5th-6th':0,'7th-8th':0, '9th':0, '10th':0 ,'11th':0,'12th':0, 'HS-grad':0,'Assoc':0, 'Some-college':0,  'Bachelors':0,'Masters':0,'Prof-school':0, 'Doctorate':0}}
for sex in adult_reconstructed["sex"].unique():
    total = sum(education_sex_reconstructed[:,sex])
    for edu in adult_old["education"].unique():
        values_educ_reconstructed[sex][edu] = 100* education_sex_reconstructed[edu][sex]/(total)


#Getting the specific data needed for plots old marital status
marital_sex_old = adult_old[['marital.status', 'sex']].value_counts()
values_mar_old = {"Male":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}, "Female":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}}
for sex in adult_old["sex"].unique():
    total = sum(marital_sex_old[:,sex])
    for mar in adult_old["marital.status"].unique():
        values_mar_old[sex][mar] = 100* marital_sex_old[mar][sex]/(total)

#Getting the specific data needed for plots reconstructed marital status
marital_sex_reconstructed = adult_reconstructed[['marital.status', 'sex']].value_counts()
values_mar_reconstructed = {"Male":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}, "Female":  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}}
for sex in adult_reconstructed["sex"].unique():
    total = sum(marital_sex_reconstructed[:,sex])
    for mar in adult_old["marital.status"].unique():
        values_mar_reconstructed[sex][mar] = 100* marital_sex_reconstructed[mar][sex]/(total)

###----------------###
###Create the plots###
###----------------###
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