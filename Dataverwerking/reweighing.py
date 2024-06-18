def weighting_educ(column_mf, column_level):
    #Creating the observed data
    column_level = column_level.copy()
    column_mf = column_mf.copy()
    column_level = pre_processing_data_educ(column_level)
    p_obs_male_dict = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "Assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    p_obs_female_dict = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "Assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    female_ob = 0
    male_ob = 0
    for level,gender in zip(column_level, column_mf):
        #Counting all instances per category
        try:
            if gender == "Male":
                p_obs_male_dict[level] += 1
            else:
                p_obs_female_dict[level] += 1
            #Counting the amount of men and women
            if gender == "Male":
                male_ob += 1
            else:
                female_ob += 1
        except:
            pass
    #Changing the dicts used to count into lists
    total = male_ob + female_ob
    p_obs_male = list(p_obs_male_dict.values())
    p_obs_male = [x  /total for x in p_obs_male]
    p_obs_female = list(p_obs_female_dict.values())
    p_obs_female = [x  / total for x in p_obs_female]
    
    #Calculating expected data using data from:
    #https://www.census.gov/data/tables/2018/demo/education-attainment/cps-detailed-tables.html
    total =  249193
    p_exp_male = [x /total for x in [4453,	9306,	36274,	22096,	10489,	24379,	9294,	1800,	2614] ]
    p_exp_female = [x /total for x in [4658,	8756,	35094,	24079,	13613,	27027,	11987,	1401,	1872] ]
    
    #calculating the weights by deviding the expected by the observed. The output is in order of the dicts on the first lines of the function.
    weights_male = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    weights_female = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    for obs_m, exp_m, obs_f, exp_f,key in zip(p_obs_male, p_exp_male, p_obs_female, p_exp_female, p_obs_male_dict):
        weights_male[key] = (exp_m / obs_m)
        weights_female[key] = (exp_f / obs_f)
    
    weight_educ = []
    for level,gender in zip(column_level, column_mf):
            if level == "education":
                pass
            elif gender == "Male":
                weight_educ.append(weights_male[level])
            else:
                weight_educ.append(weights_female[level])
    return weight_educ
    

#Reweighing for marital status
#https://www.census.gov/library/visualizations/interactive/marital-status-in-united-states.html
def weighting_maritalstatus(column_mf, column_mar):
    #Creating the observed data
    column_mar = column_mar.copy()
    column_mf = column_mf.copy()
    column_mar = pre_processing_data_marietal(column_mar)
    possible_status = {"Never-married", "Married-civ-spouse", "Married-spouse-absent", "Separated", "Divorced", "Widowed"}
    p_obs_male_dict = {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    p_obs_female_dict =  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    female_ob = 0
    male_ob = 0
    for i,(status,gender) in enumerate(zip(column_mar, column_mf)):
        #Counting all instances per category
        #The try is because the column name is the first instance and will fail.
        try:
            if gender == "Male":
                p_obs_male_dict[status] += 1
            else:
                p_obs_female_dict[status] += 1
        except:
            pass
        #Counting the amount of men and women
        if gender == "Male":
            male_ob += 1
        else:
            female_ob += 1
    total = male_ob + female_ob
    #Changing the dicts used to count into lists
    p_obs_male = list(p_obs_male_dict.values())
    p_obs_male = [x  /total for x in p_obs_male]
    p_obs_female = list(p_obs_female_dict.values())
    p_obs_female = [x  / total for x in p_obs_female]

    #Calculating expected data using data from:
    male = 87398131
    # percent_male = {"Never-married": 35.5, "Married": 53.1, "Separated": 1.6, "Divorced": 8.9, "Widowed": 0.9}
    female = 78509396
    # percent_female = {"Never-married": 34.2, "Married": 47.5, "Separated": 2.5, "Divorced": 13.0, "Widowed": 2.7}
    total = male + female 
    #The amount of people per group divide by total for expected, done the same as observed on different data.
    # Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    # https://data.census.gov/table/ACSST1Y2018.S1201?t=Marital%20Status%20and%20Marital%20History&y=2018
    p_exp_male = [x /total for x in [0.355 * male, 0.531 * male, 0.016 * male, 0.089 * male, 0.009 * male] ]
    p_exp_female = [x /total for x in [0.342 * female, 0.475 * female, 0.025 * female, 0.130 * female, 0.027 * female]]
    
    #calculating the weights by deviding the expected by the observed. The output is in order of the dicts on the first lines of the function.
    weights_male = {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    weights_female = {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    for obs_m, exp_m, obs_f, exp_f, key in zip(p_obs_male, p_exp_male, p_obs_female, p_exp_female, p_obs_male_dict.keys()):
        weights_male[key]= (exp_m / obs_m)
        weights_female[key]= (exp_f / obs_f)
    
    weight_marital = []
    for level,gender in zip(column_mar, column_mf):
        if level == "marital.status":
            pass
        elif gender == "Male":
            weight_marital.append(weights_male[level])
        else:
            weight_marital.append(weights_female[level])
    
    return weight_marital

def pre_processing_data_marietal(col_process):
    col_processed = col_process.copy()
    for i,(status) in enumerate(col_processed):
        if status[:7] == "Married":
            col_processed[i] = "Married"
    return col_processed

def pre_processing_data_educ(col_process):
    col_processed = col_process.copy()
    possible_levels = {"HS-grad", "Some-college", "Assoc-acdm", "Assoc-voc", "Bachelors", "Masters", "Prof-school", "Doctorate"}
    for i,(level) in enumerate(col_processed):
        #Counting all instances per category
        if not level in possible_levels:
            try:
                if level == "Preschool":
                    col_processed[i] = "8"
                elif level == "Preschool" or int(level[0]) <= 8:
                    col_processed[i] = "8"
                else:
                    col_processed[i] = "11"
            except:
                pass
        elif level in {"Assoc-acdm", "Assoc-voc"}:
             col_processed[i] = "Assoc"
    return col_processed



import os 
import csv

def gemiddelde(col_A, col_B):
    return [(a+b)/2 for a,b in zip(col_A, col_B)]

def getweights():
    gender = []
    educ = []
    status = []
    with open(os.path.join("..","Processed_data",'adult.csv'), newline='') as data:
        spamreader = csv.reader(data, delimiter=',')
        for row in spamreader:
            #[1:-1] because the words look like this: "'word'"
            educ.append(row[2])
            gender.append(row[5])
            status.append(row[3])
    column_educ = weighting_educ(gender, educ)
    column_marital = weighting_maritalstatus(gender, status)
    return gemiddelde(column_educ, column_marital)
