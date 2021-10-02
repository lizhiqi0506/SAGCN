from nested_cv_func import *
from sklearn.svm import SVC


#===== load dataset
random_sorted_sample_df = pd.read_csv('../../data/sample_label_random.csv',index_col=0)
random_sorted_sample = random_sorted_sample_df.values[:,0]
y = random_sorted_sample_df.values[:,1].astype(np.int)
X = pd.read_csv('../../data/meth_matrix_probes_150.csv', index_col=0).loc[:,random_sorted_sample].values.T.astype(float)
print("data loaded")

#===== perform 5x5 nested cv
## svc
param_space_svc = {
    "C": np.logspace(-3, 1, 8, base=2),
    "kernel": ['rbf', 'sigmoid'],
    "gamma": [0.01, 0.1] + ['auto'],
    "probability": [True]
}
model_svc = SVC()
print("========SVC nested cv start===========")
print_time()
nested_cv(X, y, model_svc, param_space_svc, './result_svc.csv')