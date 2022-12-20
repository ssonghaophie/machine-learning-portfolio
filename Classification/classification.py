# import block

# numpy and pandas for wrangling data
import numpy as np
import pandas as pd

# sklearn for classification algorithms and cv
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier

# mse for classification
def compute_mse(true_class, pred_class):
    # make empty 0 matrix
    vec = np.zeros(true_class.shape)
    # index trick to mark elements that are different as 1
    ind = true_class != pred_class
    vec[ind] = 1
    # compute the mean
    mse = np.mean(vec)
    return mse

# cross validation function for classification
def k_fold_CV(data, col_names, k, model):

    #divide the data into the k folds
    k_folds=[]
    num = int(data.shape[0]/k)
    for n in range(k):
        fold = data[n*num:(n+1)*num,:] 
        k_folds.append(fold)
        
    mse_list = []
    #acc_list = []
    
    # for each k iterations
    for f in range(k): 
        # divide test and train sets
        test = k_folds[f] 
        train = np.vstack(k_folds[:f]+k_folds[f+1:])

        # fit the selected model
        if model == "Decision Tree":
            # ccp_alpha = 0.001 for decision tree
            clf = DecisionTreeClassifier(ccp_alpha=0.001, random_state=0) 
        elif model == "SVM":
            clf = svm.SVC(kernel='poly', degree=3,gamma = 'auto',C=1)
        else: 
            return "Error";
        mod = clf.fit(train[:,:-1], train[:,-1])

        # predict how the model does in test
        test_preds = mod.predict(test[:,:-1])
        # compute mse
        mse = compute_mse(test_preds, test[:,-1])
        #acc = clf.score(test[:,:-1], test[:,-1])
        
        # store mse in mse list
        mse_list.append(mse)
        #acc_list.append(acc)

    # average the mse resulted from k different iterations
    mean_mse = np.mean(mse_list)
    #mean_acc = np.mean(acc_list)
    #print("MSE for",k,"fold CV:",mse_list)
        

    return mean_mse #, mean_acc