import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import mean_squared_error



if __name__ == '__main__':
    train_data_name = './train_data_linearly_sep.csv'
    train_data = np.genfromtxt(train_data_name, delimiter=',')
    feature_data = train_data[:, 1:-1]
    print(feature_data.shape)
    label_data = train_data[:, -1]

    train_features = feature_data[0:-200, :]
    train_labels = label_data[0:-200]
    val_features = feature_data[-200:, :]
    val_labels = label_data[-200:]
    
    svc_model = LinearSVC(random_state=0, tol=1e-5)
    svc_model.fit(feature_data, label_data)
    for i in range(10):
        print(svc_model.coef_[0][i])
