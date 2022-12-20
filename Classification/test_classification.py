import pytest
import pandas as pd
import numpy as np
import classification

mbti = pd.read_csv("personality.csv", header=0, encoding='cp1252')
mbti_np = mbti.to_numpy()

#shape check for compute_mse
def test_compute_mse_shape():
    true_class = mbti_np[:,-1]
    pred_class = mbti_np[:,-1]
    
    mse = classification.compute_mse(true_class, pred_class)
    expected = ()
    assert mse.shape == expected


#type check for compute_mse
def test_compute_mse_type():
    true_class = mbti_np[:,-1]
    pred_class = mbti_np[:,-1]

    mse = classification.compute_mse(true_class, pred_class)
    assert isinstance(mse, np.float64)


#shape check for cross validation function
def test_k_fold_CV_shape():
    var_names = list(mbti.columns)[:-1]
    model = "Decision Tree"
    
    CV = classification.k_fold_CV(mbti_np, var_names, 5, model)
    expected = ()
    assert CV.shape == expected


#type check for cross validation function    
def test_k_fold_CV_type():
    var_names = list(mbti.columns)[:-1]
    model = "Decision Tree"
    CV = classification.k_fold_CV(mbti_np, var_names, 5, model)
    assert isinstance(CV, np.float64)
    
    
    
#error check for cross validation function
def test_k_fold_CV_error():
    var_names = list(mbti.columns)[:-1]
    model = "Hello"
    
    CV = classification.k_fold_CV(mbti_np, var_names, 5, model)
    expected = "Error"
    assert CV == expected

