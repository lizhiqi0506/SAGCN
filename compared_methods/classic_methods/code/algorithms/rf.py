from nested_cv_func import *
from sklearn.ensemble import RandomForestClassifier


#===== load dataset
random_sorted_sample_df = pd.read_csv('../../data/sample_label_random.csv',index_col=0)
random_sorted_sample = random_sorted_sample_df.values[:,0]
y = random_sorted_sample_df.values[:,1].astype(np.int)
X = pd.read_csv('../../data/meth_matrix_probes_150.csv', index_col=0).loc[:,random_sorted_sample].values.T.astype(float)
print("data loaded")

#===== perform 5x5 nested cv


## random forest
param_space_rf = {
    "n_estimators": list(range(200,350,25)),  
    "min_samples_split": [2,3,4]
}
model_rf = RandomForestClassifier()
print("========Random Forest nested cv start===========")
print_time()
nested_cv(X, y, model_rf, param_space_rf, './result_rf.csv')