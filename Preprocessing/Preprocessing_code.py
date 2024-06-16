import folktables
from folktables import ACSDataSource
import numpy as np
import os 

def preprocessing_2018():
    #Determining which info we want
    ACSIncome = folktables.BasicProblem(
        features=[
            'AGEP',
            'COW',
            'SCHL',
            'MAR',
            'OCCP',
            'RELP',
            'WKHP',
            'SEX',
            'RAC1P'
        ],
        target='PINCP',
        target_transform=lambda x: x > 50000,    
        group='RAC1P',
        preprocess= folktables.adult_filter and folktables.employment_filter,
        postprocess=lambda x: np.nan_to_num(x, -1),)
    #Creating mapping to the right category
    ACSIncome_categories_mapping = {
        "COW": {
            "Employee of a private for-profit company or business, or of an individual, for wages, salary, or commissions" : "Private",
            "Employee of a private not-for-profit, tax-exempt, or charitable organization": "Private",
            "Local government employee (city, county, etc.)": "Local-gov",
            "State government employee": "State-gov",
            "Federal government employee": "Federal-gov",
            "Self-employed in own not incorporated business, professional practice, or farm": "Self-emp-not-inc",
            "Self-employed in own incorporated business, professional practice or farm" : 'Self-emp-inc',
            "Working without pay in family business or farm": "Without-pay",
            "Unemployed and last worked 5 years ago or earlier or never worked": "Error",
        },
        "SCHL": {
            "No schooling completed":"Preschool",
            "Nursery school, preschool": "Preschool",
            "Kindergarten" : "Preschool",
            "Grade 1": '1st-4th',
            "Grade 2": '1st-4th',
            "Grade 3" : '1st-4th',
            "Grade 4": '1st-4th',
            "Grade 5" : '5th-6th',
            "Grade 6": '5th-6th',
            "Grade 7": '7th-8th',
            "Grade 8": '7th-8th',
            "Grade 9": '9th',
            "Grade 10": '10th',
            "Grade 11" : '11th',
            "12th grade - no diploma" : '12th',
            "Regular high school diploma": 'HS-grad',
            "GED or alternative credential": 'HS-grad',
            "Some college, but less than 1 year": 'Some-college',
            "1 or more years of college credit, no degree": 'Some-college',
            "Associate's degree": "Assoc", #Needs to be changed in other data
            "Bachelor's degree": "Bachelors",
            "Master's degree": "Masters",
            "Professional degree beyond a bachelor's degree" :"Prof-school",
            "Doctorate degree": "Doctorate",
        },
        "MAR": {
            "Married": "Married", #Needs to be changed in other data
            "Widowed": "Widowed",
            "Divorced": "Divorced",
            "Separated": "Separated",
            "Never married or under 15 years old": "Never-married",
        },
        "RAC1P": {
            "White alone": "White",
            "Black or African American alone": "Black",
            "American Indian alone": 'Amer-Indian-Eskimo',
            "Alaska Native alone": 'Amer-Indian-Eskimo',
            "American Indian and Alaska Native tribes specified; or American Indian or Alaska Native, not specified and no other" : 'Amer-Indian-Eskimo',
            "Asian alone": 'Asian-Pac-Islander',
            "Native Hawaiian and Other Pacific Islander alone": 'Asian-Pac-Islander', #Klopt dit met hawaii?
            "Some Other Race alone": "Other",
            "Two or More Races": "Other",
        },
    }
    ACSIncome_categories = {
        "COW": {
            1.0: "Employee of a private for-profit company or business, or of an individual, for wages, salary, or commissions",
            2.0: "Employee of a private not-for-profit, tax-exempt, or charitable organization",
            3.0: "Local government employee (city, county, etc.)",
            4.0: "State government employee",
            5.0: "Federal government employee",
            6.0: "Self-employed in own not incorporated business, professional practice, or farm",
            7.0: "Self-employed in own incorporated business, professional practice or farm"
            ,
            8.0: "Working without pay in family business or farm",
            9.0: "Unemployed and last worked 5 years ago or earlier or never worked",
        },
        "SCHL": {
            1.0: "No schooling completed",
            2.0: "Nursery school, preschool",
            3.0: "Kindergarten",
            4.0: "Grade 1",
            5.0: "Grade 2",
            6.0: "Grade 3",
            7.0: "Grade 4",
            8.0: "Grade 5",
            9.0: "Grade 6",
            10.0: "Grade 7",
            11.0: "Grade 8",
            12.0: "Grade 9",
            13.0: "Grade 10",
            14.0: "Grade 11",
            15.0: "12th grade - no diploma",
            16.0: "Regular high school diploma",
            17.0: "GED or alternative credential",
            18.0: "Some college, but less than 1 year",
            19.0: "1 or more years of college credit, no degree",
            20.0: "Associate's degree",
            21.0: "Bachelor's degree",
            22.0: "Master's degree",
            23.0: "Professional degree beyond a bachelor's degree",
            24.0: "Doctorate degree",
        },
        "MAR": {
            1.0: "Married",
            2.0: "Widowed",
            3.0: "Divorced",
            4.0: "Separated",
            5.0: "Never married or under 15 years old",
        },
        "SEX": {1.0: "Male", 2.0: "Female"},
        "RAC1P": {
            1.0: "White alone",
            2.0: "Black or African American alone",
            3.0: "American Indian alone",
            4.0: "Alaska Native alone",
            5.0: "American Indian and Alaska Native tribes specified; or American Indian or Alaska Native, not specified and no other",
            6.0: "Asian alone",
            7.0: "Native Hawaiian and Other Pacific Islander alone",
            8.0: "Some Other Race alone",
            9.0: "Two or More Races",
        },
    }
    #Getting data from folktables
    data_source = ACSDataSource(survey_year='2018', horizon='1-Year', survey='person')
    ca_data = data_source.get_data(states=["AL"], download=True)

    ca_features, ca_labels, _ = ACSIncome.df_to_pandas(ca_data, categories=ACSIncome_categories, dummies=False)
    
    #Preprocessing so that the format is the same as the old census data
    for col in ["COW", "SCHL", "MAR", "SEX", "RAC1P"]:
        for i, elem in enumerate(ca_features[col]):
            try:
                ca_features.loc[i, col] = ACSIncome_categories_mapping[col][elem]
            except:
                pass
    for col in ["OCCP", "WKHP"]:
        for i, elem in enumerate(ca_features[col]):
            try:
                ca_features.loc[i, col] = int(ca_features.loc[i, col])
            except:
                pass
    ca_features = ca_features.rename(columns={"AGEP": "age", "COW": "workclass", "SCHL": "education", "MAR": "marital.status", "OCCP": "occupation", "RELP": "relationship", "WKHP": "hours.per.week", "SEX": "sex", "RAC1P": "race"}, errors="Raise")
    ca_features = ca_features.drop(columns=["occupation", "relationship"])
    ca_features.insert(7, "income", ca_labels, True)
    #Dropping all NaN values
    ca_features = ca_features.dropna(how='any')

    for enum,i in enumerate(ca_features["income"]):
        if i:
            ca_features["income"].iloc[enum] = 1
        else:
            ca_features["income"].iloc[enum] = 0
    #Writing to the CSV
    ca_features.to_csv(os.path.join('..', 'processed_data', 'data_2018.csv'), index=False)
    return ca_features


import pandas as pd
def preprocessing_old(csv_file):
    old_data = pd.read_csv(csv_file)
    #removes any rows that contain a '?', maybe do this after selecting the right columns to prevent unnecessary deleting. 
    mask = old_data.applymap(lambda x: '?' in str(x))
    old_data_clean = old_data[~mask.any(axis=1)]
    for i,(educ,status) in enumerate(zip(old_data_clean["education"], old_data_clean["marital.status"])):
        if educ == "education":
            pass
        elif educ[:5] == "Assoc":
            old_data_clean["education"].iloc[i] = "Assoc"
        elif status[:7] == "Married":
            old_data_clean["marital.status"].iloc[i] = "Married"
    old_data_clean =old_data_clean.drop(columns=["fnlwgt", "education.num", "capital.gain", "capital.loss", "native.country", "occupation", "relationship"])
    for enum,i in enumerate(old_data_clean["income"]):
        if i == "<=50K":
            old_data_clean["income"].iloc[enum] = 0
        else:
            old_data_clean["income"].iloc[enum] = 1
    old_data_clean.to_csv(os.path.join('..', 'processed_data', 'adult.csv'), index=False)
    return old_data_clean
 
