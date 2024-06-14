import pandas as pd 

def get_reconstructed_data(csv_file):
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

def get_old_data(csv_file):
    old_data = pd.read_csv(csv_file)
    #removes any rows that contain a '?', maybe do this after selecting the right columns to prevent unnecessary deleting. 
    mask = old_data.applymap(lambda x: '?' in str(x))
    old_data_clean = old_data[~mask.any(axis=1)]
    for i,(educ,status) in enumerate(zip(old_data_clean["education"], old_data_clean["marital.status"])):
        if educ == "education":
            pass
        elif educ[:4] == "Assoc":
            old_data_clean["education", i] = "Assoc"
        elif status[:6] == "Married":
            old_data_clean.iloc["martial.status", i] = "Married"
    old_data_clean =old_data_clean.drop(columns=["fnlwgt", "education.num", "capital.gain", "capital.loss", "native.country"])
    for enum,i in enumerate(old_data_clean["income"]):
        if i == "<=50K":
            old_data_clean.loc[enum, "income"] = False
        else:
            old_data_clean.loc[enum, "income"] = True
    return old_data_clean


