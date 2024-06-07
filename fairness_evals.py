import pandas as pd 

def positive_rates(model_result : pd.DataFrame, feature: str):
    result = {} 
    for group in model_result[feature].unique():
        all_group = model_result[model_result[feature] == group]
        PR_group = all_group['y_pred'].sum() / len(all_group)
        result[group] = PR_group

    return result

def true_postive_rates(model_result : pd.DataFrame, feature: str):
    result = {} 
    for group in model_result[feature].unique():
        gold_true_group = model_result[(model_result[feature] == group) & (model_result['income'] == 1)]
        if len(gold_true_group)>0:
            TPR_group = gold_true_group['y_pred'].sum() / len(gold_true_group)
            result[group] = TPR_group
        else: 
            print(f'No gold true instances found for {group}')
            result[group] = None

    return result

def true_negative_rate(model_result : pd.DataFrame, feature: str):
    result = {} 
    for group in model_result[feature].unique():
        gold_false_group = model_result[(model_result[feature] == group) & (model_result['income'] == 0)]
        if len(gold_false_group)>0:
            pred_false_of_gold_group = model_result[(model_result[feature] == group) & (model_result['income'] == 0) & (model_result['y_pred'] == 0)]
            TFR_group =  len(pred_false_of_gold_group) / len(gold_false_group)
            result[group] = TFR_group
        else: 
            print(f'No gold false instances found for {group}')
            result[group] = None

    return result
    