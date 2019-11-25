from math import sqrt



## KNN
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

def absolute_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += abs(row1[i] - row2[i])
    return distance

def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        dist = absolute_distance(test_row, train_row)
        distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


## Parsing
# open an input.txt
input_file =  open("input.txt", "r")
input_lines = input_file.readlines()

# remove \n
for line_num, line in enumerate(input_lines):
    line = line[:-1]
    input_lines[line_num] = line
    
# read n, k, t
metadata = input_lines[0].split(" ")
train_data_size = int(metadata[0])
k_neigh = int(metadata[1])
test_data_size = int(metadata[2])
assert((k_neigh <= train_data_size) and
    (1 <= k_neigh) and
    (train_data_size <= 1000) and
    (test_data_size >= 1) and
    (test_data_size <= 100))

# read train data
d_train_data = []
d_num_of_clusters = 0
for iterrr in range(train_data_size):
    data_row = input_lines[iterrr+1].split(" ")
    data_row_list = []
    x_i = float(data_row[0])
    y_i = float(data_row[1])
    sample_class = int(data_row[2])
    assert((x_i >= -1000) and
            (x_i <= 1000) and
            (y_i >= -1000) and
            (y_i <= 1000) and
            (sample_class >= 1) and
            (sample_class <= 10))
    if sample_class > d_num_of_clusters:
        d_num_of_clusters = sample_class
    data_row_list.append(float(data_row[0]))
    data_row_list.append(float(data_row[1]))
    data_row_list.append(sample_class - 1)
    d_train_data.append(data_row_list)

# read test data
d_test_data = []
for iterrr in range(test_data_size):
    data_row = input_lines[iterrr+1+train_data_size].split(" ")
    data_row_list = []
    data_row_list.append(float(data_row[0]))
    data_row_list.append(float(data_row[1]))
    d_test_data.append(data_row_list)


## Performing
with open('output.txt', 'w') as output_file:
    for row in d_test_data:
        prediction = predict_classification(d_train_data, row, k_neigh)
        output_file.write("{}\n".format(prediction+1))
    output_file.close()

