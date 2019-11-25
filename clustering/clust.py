import csv
import numpy as np
from sklearn.cluster import KMeans



if __name__ == '__main__':
    train_data_name = './train_data_baseline_contestant.csv'
    train_data = np.genfromtxt(train_data_name, delimiter=',')
    
    feature_data = train_data[:, 1:]
    print(feature_data.shape)

    model = KMeans(n_clusters=2, random_state=0).fit(feature_data)
    labels = model.labels_

    with open('submit.csv', mode='w') as submit:
        submit_writer = csv.writer(submit, delimiter=',')
        submit_writer.writerow(['Num', 'Label'])
        for i in range(1000):
            submit_writer.writerow(['%i' % i, '%i' % labels[i]])
    
