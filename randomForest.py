import csv
from sklearn.ensemble import RandomForestRegressor

open_path = ""
file_name = ""
save_path = ""

# file location
open_file_location = open_path + file_name
save_file_location = save_path + file_name

def main():
    # reading the file
    with open(open_file_location, "r") as _file:
        feature_names_arr = []
        data_arr = []

        dataset = csv.reader(_file)

        for row in dataset:
            feature_names_arr = row
            break

        for row in dataset:
            data_arr.append(row)

    return feature_names_arr, data_arr

# forest  = RandomForestRegressor(n_estimators=100, max_features= 'auto')
#
# forest.fit()