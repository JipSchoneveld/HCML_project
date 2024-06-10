def weighting_educ(column_mf, column_level):
    #Creating the observed data
    column_level = column_level.copy()
    column_mf = column_mf.copy()
    possible_levels = {"HS-grad", "Some-college", "Assoc-acdm", "Assoc-voc", "Bachelors", "Masters", "Prof-school", "Doctorate"}
    p_obs_male_dict = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    p_obs_female_dict = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    female_ob = 0
    male_ob = 0
    for i,(level,gender) in enumerate(zip(column_level, column_mf)):
        #Counting all instances per category
        if not level in possible_levels:
            try:
                if level == "Preschool":
                    if gender == "Male":
                        p_obs_male_dict["8"] += 1
                    else:
                        p_obs_female_dict["8"] += 1
                elif int(level[0]) <= 8:
                    column_level = "8"
                    if gender == "Male":
                        p_obs_male_dict["8"] += 1
                    else:
                        p_obs_female_dict["8"] += 1
                else:
                    if gender == "Male":
                        p_obs_male_dict["11"] += 1
                    else:
                        p_obs_female_dict["11"] += 1  
            except:
                pass
        elif level in {"Assoc-acdm", "Assoc-voc"}:
            if gender == "Male":
                p_obs_male_dict["assoc"] += 1
            else:
                p_obs_female_dict["assoc"] += 1
        else:
            if gender == "Male":
                p_obs_male_dict[level] += 1
            else:
                p_obs_female_dict[level] += 1
        #Counting the amount of men and women
        if gender == "Male":
            male_ob += 1
        else:
            female_ob += 1
    #Changing the dicts used to count into lists
    total = male_ob + female_ob
    p_obs_male = list(p_obs_male_dict.values())
    p_obs_male = [x  /total for x in p_obs_male]
    p_obs_female = list(p_obs_female_dict.values())
    p_obs_female = [x  / total for x in p_obs_female]
    
    #Calculating expected data using data from:
    #https://www.census.gov/data/tables/2022/demo/educational-attainment/cps-detailed-tables.html
    total =  226274
    p_exp_male = [x /total for x in [4041,	6303,	33081,	16085,	10616,	25192,	10156,	1860,	2644] ]
    p_exp_female = [x /total for x in [3895,	5695,	31383,	16900,	13057,	27853,	13725,	1584,	2203] ]
    
    #calculating the weights by deviding the expected by the observed. The output is in order of the dicts on the first lines of the function.
    weights_male = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    weights_female = {"8":0, "11":0, "HS-grad": 0, "Some-college": 0, "assoc": 0, "Bachelors": 0, "Masters": 0, "Prof-school": 0, "Doctorate": 0}
    for obs_m, exp_m, obs_f, exp_f,key in zip(p_obs_male, p_exp_male, p_obs_female, p_exp_female, p_obs_male_dict):
        weights_male[key] = (exp_m / obs_m)
        weights_female[key] = (exp_f / obs_f)
    
    return weights_male, weights_female
    

#Reweighing for marital status
#https://www.census.gov/library/visualizations/interactive/marital-status-in-united-states.html
def weighting_maritalstatus(column_mf, column_mar):
    #Creating the observed data
    possible_status = {"Never-married", "Married-civ-spouse", "Married-spouse-absent", "Separated", "Divorced", "Widowed"}
    p_obs_male_dict = {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    p_obs_female_dict =  {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    female_ob = 0
    male_ob = 0
    for i,(status,gender) in enumerate(zip(column_mar, column_mf)):
        #Counting all instances per category
        if not status in possible_status:
            pass
        else:
            if status == "Married-civ-spouse" or status == "Married-spouse-absent":
                status = "Married"
            
            if gender == "Male":
                p_obs_male_dict[status] += 1
            else:
                p_obs_female_dict[status] += 1
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
    male = 129973543
    female = 136348759
    total = male + female 
    #The amount of people per group divide by total for expected, done the same as observed on different data.
    p_exp_male = [x /total for x in [48052364,64057452,2071170,12365418, 3427139] ]
    p_exp_female = [x /total for x in [41880024,63122995,2963251,16553544,11828945]]
    
    #calculating the weights by deviding the expected by the observed. The output is in order of the dicts on the first lines of the function.
    weights_male = {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    weights_female = {"Never-married": 0, "Married": 0, "Separated": 0, "Divorced": 0, "Widowed": 0}
    for obs_m, exp_m, obs_f, exp_f, key in zip(p_obs_male, p_exp_male, p_obs_female, p_exp_female, p_obs_male_dict.keys()):
        weights_male[key]= (exp_m / obs_m)
        weights_female[key]= (exp_f / obs_f)
    
    return weights_male, weights_female

get_data_weights()
    