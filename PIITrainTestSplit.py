import pandas as pd
import numpy as np

#class for splitting the data into train, test for building model
class PIITrainTestSplit:

    def split_data(self, input_df, input_data_columns):
        np.random.seed(0)
        Y = pd.factorize(input_df['label'])[0]
        input_df['label'] = pd.Categorical.from_codes(Y, input_data_columns)

        input_df['is_train'] = np.random.uniform(0, 1, len(input_df)) <= .60
        train, test = input_df[input_df['is_train'] == True], input_df[input_df['is_train'] == False]

        y = pd.factorize(train['label'])[0]
        test_y = pd.factorize(test['label'])[0]
        train.drop(['is_train', 'label'], axis=1, inplace=True)
        test.drop(['is_train', 'label'], axis=1, inplace=True)

        return (train, test, y, test_y)