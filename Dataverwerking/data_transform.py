import pandas as pd 
from sklearn.preprocessing import OneHotEncoder

def cat_to_one_hot(raw_data : pd.DataFrame, cat_feats: list, OH_encoder : OneHotEncoder):
    cat_feats_encoded = OH_encoder.transform(raw_data[cat_feats])
    encoded_data = pd.concat([raw_data.drop(columns=cat_feats), cat_feats_encoded], axis=1)
    return encoded_data