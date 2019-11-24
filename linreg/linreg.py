import csv
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error



if __name__ == '__main__':
    train_data_name = 'train_data_regression.csv'
    test_data_name = 'test_data_regression.csv'
    train_data = np.genfromtxt(train_data_name, delimiter=',')

    feature_data = train_data[:, 1:-1]
    label_data = train_data[:, -1]

    train_features = feature_data[0:-200, :]
    train_labels = label_data[0:-200]
    val_features = feature_data[-200:, :]
    val_labels = label_data[-200:]

    regr = linear_model.LinearRegression()
    regr.fit(feature_data, label_data)
    #regr.fit(train_features, train_labels)
    #pred = regr.predict(val_features)
    #mae = mean_absolute_error(pred, val_labels)

    test_data = np.genfromtxt(test_data_name, delimiter=',')
    test_data = test_data[:, 1:]
    pred = regr.predict(test_data)
    print(pred)
    nums = np.arange(100)
    with open('submit.csv', mode='w') as submit:
        submit_writer = csv.writer(submit, delimiter=',')
        submit_writer.writerow(['', 'Predict'])
        for i in range(100):
            submit_writer.writerow(['%i' % i, '%f' % pred[i]])
        submit_writer.writerow([])
