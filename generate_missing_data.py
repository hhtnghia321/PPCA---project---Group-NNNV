import numpy as np
import pandas as pd
import random

def generate_missing_data(data, name_data = 'data', number_values_percol = 50):
    random.seed(20052020)
    true_values = []
    pos_of_values = []
    for i in range(0, data.shape[1]):
        temp = []
        random_na_pos_for_col = random.sample(range(0, data.shape[0]), number_values_percol)
        for item in random_na_pos_for_col:
            temp.append(data[item, i])
            data[item, i] = '?'
        true_values.append(temp)
        pos_of_values.append(random_na_pos_for_col)
    pd.DataFrame(data).to_csv(name_data + str(number_values_percol) + '_navalues.csv', index = False)
    pd.DataFrame(np.array(pos_of_values).T).to_csv(\
            name_data + str(number_values_percol) + '_pos_navalue.csv', index = False)
    print('Done')

if __name__ == "__main__":

    names = ['Sample_code_number', 'Clump_Thickness', 'Uniformity_of_Cell_Size',
         'Uniformity_of_Cell_Shape', 'Marginal_Adhesion', 'Single_Epithelial_Cell_Size',
         'Bare_Nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses', 'Class']
    origin_data = pd.read_csv("breast-cancer-wisconsin.data", names=names, index_col = False)
    #drop columns unnecessary
    origin_data = origin_data.drop(columns = ['Sample_code_number', 'Class'])
    # convert to numpy array to generate missing values data
    origin_data = origin_data.values
    # generate na_values dataset and and record the pos of the na_values ​​in csv file

    generate_missing_data(origin_data, 'breast_cancer', 50)



